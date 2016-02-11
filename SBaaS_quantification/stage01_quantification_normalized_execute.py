﻿
from .stage01_quantification_normalized_io import stage01_quantification_normalized_io
from .stage01_quantification_MQResultsTable_query import stage01_quantification_MQResultsTable_query
from SBaaS_LIMS.lims_experiment_query import lims_experiment_query
from SBaaS_LIMS.lims_sample_query import lims_sample_query
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
from SBaaS_LIMS.lims_msMethod_query import lims_msMethod_query
#Resources
from python_statistics.calculate_interface import calculate_interface
#TODO: remove after making add method
from .stage01_quantification_normalized_postgresql_models import *
#TODO: remove after implementing calc in averages
from math import sqrt
import numpy

class stage01_quantification_normalized_execute(stage01_quantification_normalized_io,
                                                stage01_quantification_MQResultsTable_query,
                                                lims_experiment_query,
                                                lims_sample_query,
                                                lims_biologicalMaterial_query,
                                                lims_msMethod_query ):
    def execute_normalizeSamples2Biomass(self,experiment_id_I,biological_material_I=None,conversion_name_I=None,sample_names_I=[],component_names_I=[],use_height_I=False,sample_types_I=['Unknown']):
        '''Normalize calculated concentrations to measured biomass
         Input:
           experiment_id_I
           biological_material_I =  biological material (if None, no normalization is done)
           conversion_name_I = biomass conversion name (if None, no normalization is done)
           use_height_I = if True, use the ion count for peak height instead of the calculated_concentration or height/area ratio
         Output:
           sample_name
           sample_id
           component_group_name
           component_name
           calculated_concentration
           calculated_concentration_units
           used_
        '''
        #TODO: make add method
        data_O=[];
        calc = calculate_interface();
        
        print('execute_normalizeSamples2Biomass...')
        # get sample names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            for st in sample_types_I:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
        # create database table
        for sn in sample_names:
            print('normalizing samples2Biomass for sample_name ' + sn);
            # get component names
            if component_names_I:
                component_names = component_names_I;
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleName(experiment_id_I,sn);
            # get sample id
            sample_id = self.get_sampleID_experimentIDAndSampleName(experiment_id_I,sn);
            if (biological_material_I and conversion_name_I):
                # get physiological parameters
                cvs = None;
                cvs_units = None;
                od600 = None;
                dil = None;
                dil_units = None;
                conversion = None;
                conversion_units = None;
                cvs, cvs_units, od600, dil,dil_units = self.get_CVSAndCVSUnitsAndODAndDilAndDilUnits_sampleName(sn);
                conversion, conversion_units = self.get_conversionAndConversionUnits_biologicalMaterialAndConversionName(biological_material_I,conversion_name_I);
                if not(cvs and cvs_units and od600 and dil and dil_units):
                    print('cvs, cvs_units, or od600 are missing from physiological parameters');
                    print('or dil and dil_units are missing from sample descripton');
                    exit(-1);
                elif not(conversion and conversion_units):
                    print('biological_material or conversion name is incorrect');
                    exit(-1);  
                else:
                    #calculate the cell volume or biomass depending on the conversion units
                    #cell_volume, cell_volume_units = calc.calculate_cellVolume_CVSAndCVSUnitsAndODAndConversionAndConversionUnits(cvs,cvs_units,od600,conversion,conversion_units);
                    cell_volume, cell_volume_units = calc.calculate_biomass_CVSAndCVSUnitsAndODAndConversionAndConversionUnits(cvs,cvs_units,od600,conversion,conversion_units);
                for cn in component_names:
                    print('normalizing samples2Biomass for component_name ' + cn);
                    # get component group name
                    #component_group_name = self.get_componentGroupName_experimentIDAndComponentName(experiment_id_I,cn);
                    component_group_name = self.get_msGroup_componentName_MSComponents(cn);
                    # get the calculated concentration
                    calc_conc = None;
                    calc_conc_units = None;
                    if use_height_I: 
                        calc_conc, calc_conc_units = self.get_peakHeight_sampleNameAndComponentName(sn,cn);
                    else:
                        calc_conc, calc_conc_units = self.get_concAndConcUnits_sampleNameAndComponentName(sn,cn);
                    # calculate the normalized concentration
                    norm_conc = None;
                    norm_conc_units = None;
                    if calc_conc: 
                        norm_conc, norm_conc_units = calc.calculate_conc_concAndConcUnitsAndDilAndDilUnitsAndConversionAndConversionUnits(calc_conc,calc_conc_units,dil,dil_units,cell_volume, cell_volume_units);
                    # update data_stage01_quantification_normalized
                    if norm_conc:
                        #TODO: make add method
                        #data_O.append();
                        row = data_stage01_quantification_normalized(experiment_id_I, sn,sample_id,component_group_name,cn,norm_conc,norm_conc_units,True);
                        self.session.add(row);
            else:
                for cn in component_names:
                    print('normalizing samples2Biomass for component_name ' + cn);
                    # get component group name
                    #component_group_name = self.get_componentGroupName_experimentIDAndComponentName(experiment_id_I,cn);
                    component_group_name = self.get_msGroup_componentName_MSComponents(cn);
                    # get the calculated concentration
                    calc_conc = None;
                    calc_conc_units = None;
                    if use_height_I: 
                        calc_conc, calc_conc_units = self.get_peakHeight_sampleNameAndComponentName(sn,cn);
                    else:
                        calc_conc, calc_conc_units = self.get_concAndConcUnits_sampleNameAndComponentName(sn,cn);
                    #TODO: make add method
                    #data_O.append();
                    row = data_stage01_quantification_normalized(experiment_id_I, sn,sample_id,component_group_name,cn,calc_conc,calc_conc_units,True);
                    self.session.add(row);
            self.session.commit();
    def execute_removeDuplicateDilutions(self,experiment_id_I,component_names_dil_I = []):
        '''remove duplicate dilutions from data_stage01_quantification_normalized
        NOTE: rows are not removed, but the used value is changed to false
        NOTE: priority is given to the 1x dilution (i.e. 10x dilutions are removed
              if a 1x and 10x are both used'''
        # Input:
        #   experiment_id_I = experiment
        #   component_names_dil_I = component names for which the dilution will be prioritized
        
        print('execute_removeDuplicateDilutions...')
        # get sample names
        sample_ids = [];
        sample_ids = self.get_sampleIDs_experimentID_dataStage01Normalized(experiment_id_I);
        for si in sample_ids:
            # get component names
            component_names = [];
            component_names = self.get_componentsNames_experimentIDAndSampleID_dataStage01Normalized(experiment_id_I,si);
            for cn in component_names:
                # get dilutions
                sample_dilutions = [];
                sample_dilutions = self.get_sampleDilutions_experimentIDAndSampleIDAndComponentName_dataStage01Normalized(experiment_id_I,si,cn);
                if len(sample_dilutions)<2: continue;
                # find the minimum and maximum dilution
                min_sample_dilution = min(sample_dilutions);
                max_sample_dilution = max(sample_dilutions);
                for sd in sample_dilutions:
                    # prioritize undiluted samples if not in the dilution list
                    # i.e. diluted samples used_ are set to FALSE
                    if not(cn in component_names_dil_I) and not(sd == min_sample_dilution):
                        # get the sample name
                        sample_name = self.get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(experiment_id_I,si,sd);
                        try:
                            data_update = self.session.query(data_stage01_quantification_normalized).filter(
                                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                                    data_stage01_quantification_normalized.sample_name.like(sample_name),
                                    data_stage01_quantification_normalized.component_name.like(cn)).update(
                                    {'used_': False},synchronize_session=False);
                        except SQLAlchemyError as e:
                            print(e);
                    # prioritize diluted samples if in the dilution list
                    # i.e. undiluted samples used_ are set to FALSE
                    if (cn in component_names_dil_I) and not(sd == max_sample_dilution):
                        # get the sample name
                        sample_name = self.get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(experiment_id_I,si,sd);
                        try:
                            data_update = self.session.query(data_stage01_quantification_normalized).filter(
                                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                                    data_stage01_quantification_normalized.sample_name.like(sample_name),
                                    data_stage01_quantification_normalized.component_name.like(cn)).update(
                                    {'used_': False},synchronize_session=False);
                        except SQLAlchemyError as e:
                            print(e);
        self.session.commit();
    def execute_removeDuplicateComponents(self,experiment_id_I):
        '''remove duplicate components from data_stage01_quantification_normalized
        NOTE: rows are not removed, but the used value is changed to false
        NOTE: priority is given to the primary transition'''
        return
    def execute_analyzeAverages(self,experiment_id_I,sample_name_abbreviations_I=[],sample_names_I=[],component_names_I=[]):
        '''calculate the averages using the formula ave(broth),i - ave(filtrate),i
        NOTE: data_stage01_quantification_normalized must be populated
        Input:
        experiment_id_I
        sample_name_abbreviations_I
        sample_names_I
        component_names_I
        Output:
        sample_name_abbreviation
        component_group_name
        component_name
        concentration average
        concentration CV
        concentration units
        % extracellular
        '''

        #TODO: make add method
        data_O=[];
        calc = calculate_interface();
        
        print('execute_analyzeAverages...')
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01Normalized(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('analyzing averages for sample_name_abbreviation ' + sna);
            # get component names
            if component_names_I:
                component_names = component_names_I
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
            for cn in component_names:
                print('analyzing averages for component_name ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                # get time points
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
                if not time_points: continue;
                for tp in time_points:
                    print('analyzing averages for time_point ' + tp);
                    # get filtrate sample names
                    sample_names = [];
                    sample_description = 'Filtrate';
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(experiment_id_I,sna,sample_description,cn,tp);
                    if sample_names_I: # screen out sample names that are not in the input
                        sample_names = [x for x in sample_names if x in sample_names_I];
                    concs = [];
                    conc_units = None;
                    for sn in sample_names:
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if (not(conc) or conc==0): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates_filtrate = len(concs);
                    conc_average_filtrate = 0.0;
                    conc_var_filtrate = 0.0;
                    conc_cv_filtrate = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        conc_average_filtrate = 0;
                        conc_var_filtrate = 0;
                    elif n_replicates_filtrate<2: 
                        conc_average_filtrate = concs[0];
                        conc_var_filtrate = 0;
                    else: 
                        #conc_average_filtrate, conc_var_filtrate = calc.calculate_ave_var_R(concs);
                        conc_average_filtrate = numpy.mean(numpy.array(concs));
                        conc_var_filtrate = numpy.var(numpy.array(concs));
                        if (conc_average_filtrate <= 0): conc_cv_filtrate = 0;
                        else: conc_cv_filtrate = sqrt(conc_var_filtrate)/conc_average_filtrate*100; 
                    # get broth sample names
                    sample_names = [];
                    sample_description = 'Broth';
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(experiment_id_I,sna,sample_description,cn,tp);
                    if sample_names_I: # screen out sample names that are not in the input
                        sample_names = [x for x in sample_names if x in sample_names_I];
                    concs = [];
                    conc_units = None;
                    for sn in sample_names:
                        print('analyzing averages for sample_name ' + sn);
                        # query concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if (not(conc) or conc==0): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates = len(concs);
                    conc_average_broth = 0.0;
                    conc_var_broth = 0.0;
                    conc_cv_broth = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        continue
                    elif n_replicates<2: 
                        continue
                    else: 
                        #conc_average_broth, conc_var_broth = calc.calculate_ave_var_R(concs);
                        conc_average_broth = numpy.mean(numpy.array(concs));
                        conc_var_broth = numpy.var(numpy.array(concs));
                        if (conc_average_broth <= 0): conc_cv_broth = 0;
                        else: conc_cv_broth = sqrt(conc_var_broth)/conc_average_broth*100; 
                    # calculate average and CV
                    conc_average = 0.0;
                    conc_var = 0.0;
                    conc_cv = 0.0;
                    conc_average = conc_average_broth-conc_average_filtrate;
                    if (conc_average < 0): conc_average = 0;
                    conc_var = conc_var_broth + conc_var_filtrate;
                    if (conc_average <= 0): conc_cv = 0;
                    else: conc_cv = sqrt(conc_var)/conc_average*100;
                    # calculate the % extracellular
                    extracellular_percent = conc_average_filtrate/conc_average_broth*100;
                    # add data to the session
                    #TODO: make add method
                    #data_O.append()
                    row = data_stage01_quantification_averages(experiment_id_I, sna, tp, component_group_name, cn,
                                                   n_replicates, conc_average_broth, conc_cv_broth,
                                                   n_replicates_filtrate, conc_average_filtrate, conc_cv_filtrate,
                                                   n_replicates, conc_average, conc_cv, conc_units, extracellular_percent, True);   
                    self.session.add(row);
        self.session.commit(); 
        #TODO: make add method
        #self.add_data_stage01_quantification_averages
    def execute_analyzeAverages_blanks(self,experiment_id_I,sample_name_abbreviations_I=[],sample_names_I=[],component_names_I=[],blank_sample_names_I=[]):
        '''calculate the averages using the ave(broth),i - ave(blank,broth)
        NOTE: data_stage01_quantification_normalized must be populated
        Input:
        experiment_id_I
        sample_name_abbreviations_I
        sample_names_I
        component_names_I
        blank_sample_names_I = []; if specified, specific blank samples will be used as the filtrate instead of filtrate samples
        Output:
        sample_name_abbreviation
        component_group_name
        component_name
        concentration average
        concentration CV
        concentration units
        % extracellular
        '''

        #TODO: make add method
        data_O=[];
        calc = calculate_interface();
        
        print('execute_analyzeAverages...')
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01Normalized(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('analyzing averages for sample_name_abbreviation ' + sna);
            # get component names
            if component_names_I:
                component_names = component_names_I
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
            for cn in component_names:
                print('analyzing averages for component_name ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                # get time points
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
                if not time_points: continue;
                for tp in time_points:
                    print('analyzing averages for time_point ' + tp);
                    # get blank concentrations
                    if blank_sample_names_I:
                        sample_names = blank_sample_names_I;
                    else:
                        sample_names = [];
                    concs = [];
                    conc_units = None;
                    for sn in sample_names:
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if (not(conc) or conc==0): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates_filtrate = len(concs);
                    conc_average_filtrate = 0.0;
                    conc_var_filtrate = 0.0;
                    conc_cv_filtrate = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        conc_average_filtrate = 0;
                        conc_var_filtrate = 0;
                    elif n_replicates_filtrate<2: 
                        conc_average_filtrate = concs[0];
                        conc_var_filtrate = 0;
                    else: 
                        #conc_average_filtrate, conc_var_filtrate = calc.calculate_ave_var_R(concs);
                        conc_average_filtrate = numpy.mean(numpy.array(concs));
                        conc_var_filtrate = numpy.var(numpy.array(concs));
                        if (conc_average_filtrate <= 0): conc_cv_filtrate = 0;
                        else: conc_cv_filtrate = sqrt(conc_var_filtrate)/conc_average_filtrate*100; 
                    # get broth sample names
                    sample_names = [];
                    sample_description = 'Broth';
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(experiment_id_I,sna,sample_description,cn,tp);
                    if sample_names_I: # screen out sample names that are not in the input
                        sample_names = [x for x in sample_names if x in sample_names_I];
                    concs = [];
                    conc_units = None;
                    for sn in sample_names:
                        print('analyzing averages for sample_name ' + sn);
                        # query concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if (not(conc) or conc==0): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates = len(concs);
                    conc_average_broth = 0.0;
                    conc_var_broth = 0.0;
                    conc_cv_broth = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        continue
                    elif n_replicates<2: 
                        continue
                    else: 
                        #conc_average_broth, conc_var_broth = calc.calculate_ave_var_R(concs);
                        conc_average_broth = numpy.mean(numpy.array(concs));
                        conc_var_broth = numpy.var(numpy.array(concs));
                        if (conc_average_broth <= 0): conc_cv_broth = 0;
                        else: conc_cv_broth = sqrt(conc_var_broth)/conc_average_broth*100; 
                    # calculate average and CV
                    conc_average = 0.0;
                    conc_var = 0.0;
                    conc_cv = 0.0;
                    conc_average = conc_average_broth-conc_average_filtrate;
                    if (conc_average < 0): conc_average = 0;
                    conc_var = conc_var_broth + conc_var_filtrate;
                    if (conc_average <= 0): conc_cv = 0;
                    else: conc_cv = sqrt(conc_var)/conc_average*100;
                    # calculate the % extracellular
                    extracellular_percent = conc_average_filtrate/conc_average_broth*100;
                    # add data to the session
                    #TODO: make add method
                    #data_O.append()
                    row = data_stage01_quantification_averages(experiment_id_I, sna, tp, component_group_name, cn,
                                                   n_replicates, conc_average_broth, conc_cv_broth,
                                                   n_replicates_filtrate, conc_average_filtrate, conc_cv_filtrate,
                                                   n_replicates, conc_average, conc_cv, conc_units, extracellular_percent, True);   
                    self.session.add(row);
        self.session.commit(); 