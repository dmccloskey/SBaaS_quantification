#Resources
import numpy

from .stage01_quantification_replicatesMI_io import stage01_quantification_replicatesMI_io
from .stage01_quantification_normalized_query import stage01_quantification_normalized_query
from .stage01_quantification_QCs_query import stage01_quantification_QCs_query
from .stage01_quantification_replicates_query import stage01_quantification_replicates_query
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#TODO: remove after making add method
from .stage01_quantification_replicates_postgresql_models import *
#TODO: remove after refactor
from r_statistics.r_interface import r_interface
from python_statistics.calculate_interface import calculate_interface

class stage01_quantification_replicatesMI_execute(stage01_quantification_replicatesMI_io,
                                                stage01_quantification_normalized_query,
                                                stage01_quantification_QCs_query,
                                                stage01_quantification_replicates_query,
                                                lims_biologicalMaterial_query):    
    def execute_calculateMissingValues_replicates(self,experiment_id_I,sample_name_abbreviations_I=[],r_calc_I=None):
        '''calculate estimates for missing replicates values using AmeliaII from R
        INPUT:
        experiment_id_I
        sample_name_abbreviations_I'''
        
        if r_calc_I: r_calc = r_calc_I;
        else: r_calc = r_interface();

        print('execute_calculateMissingValues_replicates...')
        # get sample name abbreviations
        if sample_name_abbreviations_I:
            sample_names_abbreviation = sample_name_abbreviations_I;
        else:
            sample_names_abbreviation = [];
            sample_names_abbreviation = self.get_sampleNameAbbreviations_experimentID_dataStage01Replicates(experiment_id_I);
        # for each sample name abbreviation
        for sna in sample_names_abbreviation:
            print('calculating missing values for sample_name_abbreviation ' + sna);
            # get time points
            time_points = [];
            time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Replicates(experiment_id_I,sna);
            for tp in time_points:
                print('calculating missing values for time_point ' + tp);
                # get sample names short
                sample_names_short = []
                sample_names_short = self.get_SampleNameShort_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01Replicates(experiment_id_I,sna,tp);
                data = [];
                for sns in sample_names_short:
                    print('calculating missing values for sample_name_abbreviation ' + sns);
                    # get sample names short, component names, and concentrations
                    data_tmp = [];
                    data_tmp = self.get_data_experimentIDAndSampleNameShortAndTimePoint_dataStage01Replicates(experiment_id_I,sns,tp);
                    data.extend(data_tmp);
                # compute missing values
                dataListUpdated = [];
                sns_NA = [];
                cn_NA = [];
                cc_NA = [];
                sns_NA, cn_NA, cc_NA = r_calc.calculate_missingValues(data);
                for n in range(len(sns_NA)):
                    component_group_name = None;
                    calculated_concentration_units = None;
                    component_group_name, calculated_concentration_units = self.get_componentGroupNameAndConcUnits_experimentIDAndComponentNameAndSampleNameAbbreviationAndTimePoint_dataStage01Replicates(experiment_id_I,cn_NA[n],sna,tp);
                    # update data_stage01_quantification_replicatesMI
                    row = data_stage01_quantification_replicatesMI(experiment_id_I,sns_NA[n],tp,component_group_name,cn_NA[n],"AmeliaII",None,cc_NA[n],calculated_concentration_units,True,None);
                    self.session.add(row);
            self.session.commit(); 

    def execute_calculateMissingComponents_replicates(self,experiment_id_I,biological_material_I=None,conversion_name_I=None,sample_names_short_I=[]):
        '''calculate estimates for samples in which a component was not found for any of the replicates'''
        
        calc = calculate_interface();

        print('execute_calculateMissingComponents_replicates...')
        data_O=[];
        # get all sample names short
        if sample_names_short_I:
            sample_names_short = sample_names_short_I;
        else:
            sample_names_short = [];
            sample_names_short = self.get_sampleNameShort_experimentIDAndSampleDescription_dataStage01Normalized(experiment_id_I,'Broth');
        # get component names
        component_names = []
        component_names = self.get_componentNames_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        # get time points
        time_points = [];
        time_points = self.get_timePoint_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        for tp in time_points:
            print('calculating missing components for time_point ' + tp);
            for cn in component_names:
                print('calculating missing components for component_name ' + cn);
                component_group_name = None;
                calculated_concentration_units = None;
                component_group_name, calculated_concentration_units = self.get_componentGroupNameAndConcUnits_experimentIDAndComponentName_dataStage01Replicates(experiment_id_I,cn);
                for sns in sample_names_short:
                    print('calculating missing components for sample_name_short ' + sns);
                    # get calculated concentration
                    calculated_concentration = None;
                    calculated_concentration = self.get_calculatedConcentration_experimentIDAndSampleNameShortAndTimePointAndComponentName_dataStage01ReplicatesMI(experiment_id_I,sns,tp,cn);
                    if calculated_concentration: continue
                    # get the lloq
                    lloq = None;
                    conc_units = None;
                    lloq, conc_units = self.get_lloq_ExperimentIDAndComponentName_dataStage01LLOQAndULOQ(experiment_id_I,cn);
                    if not lloq:
                        print('lloq not found'); 
                        continue
                    # normalize the lloq
                    if (biological_material_I and conversion_name_I):
                        # get physiological parameters
                        cvs = None;
                        cvs_units = None;
                        od600 = None;
                        dil = None;
                        dil_units = None;
                        conversion = None;
                        conversion_units = None;
                        cvs, cvs_units, od600, dil,dil_units = self.get_CVSAndCVSUnitsAndODAndDilAndDilUnits_sampleNameShort(experiment_id_I,sns);
                        conversion, conversion_units = self.get_conversionAndConversionUnits_biologicalMaterialAndConversionName(biological_material_I,conversion_name_I);
                        if not(cvs and cvs_units and od600 and dil and dil_units):
                            print('cvs, cvs_units, or od600 are missing from physiological parameters');
                            print('or dil and dil_units are missing from sample descripton');
                            exit(-1);
                        elif not(conversion and conversion_units):
                            print('biological_material or conversion name is incorrect');
                            exit(-1);  
                        else:
                            #calculate the cell volume
                            cell_volume, cell_volume_units = self.calculate.calculate_biomass_CVSAndCVSUnitsAndODAndConversionAndConversionUnits(cvs,cvs_units,od600,conversion,conversion_units);
                            # calculate the normalized concentration
                            norm_conc = None;
                            norm_conc_units = None;
                            norm_conc, norm_conc_units = self.calculate.calculate_conc_concAndConcUnitsAndDilAndDilUnitsAndConversionAndConversionUnits(lloq,conc_units,dil,dil_units,cell_volume, cell_volume_units);
                            if norm_conc:
                                norm_conc = norm_conc/2;
                                # update data_stage01_quantification_normalized
                            #    dataListUpdated_I.append({'experiment_id':experiment_id_I,
                            #        'sample_name_short':sns,
                            #        'time_point':tp,
                            #        'component_group_name':component_group_name,
                            #        'component_name':cn,
                            #        'calculated_concentration':norm_conc,
                            #        'calculated_concentration_units':norm_conc_units,
                            #        'used_':True,
                            #        'comment_':None});
                                # populate data_stage01_quantification_replicatesMI
                                row = data_stage01_quantification_replicatesMI(experiment_id_I,sns,tp,component_group_name,cn,norm_conc,"lloq",None,norm_conc_units,True,None);
                                self.session.add(row);
                    else:
                        calc_conc = lloq/2;
                        # populate data_stage01_quantification_replicatesMI
                        #dataListUpdated_I.append({'experiment_id':experiment_id_I,
                        #        'sample_name_short':sns,
                        #        'time_point':tp,
                        #        'component_group_name':component_group_name,
                        #        'component_name':cn,
                        #        'calculated_concentration':calc_conc,
                        #        'calculated_concentration_units':conc_units,
                        #        'used_':True,
                        #        'comment_':None});
                        row = data_stage01_quantification_replicatesMI(experiment_id_I,sns,tp,component_group_name,cn,"lloq",None,calc_conc,conc_units,True);
                        self.session.add(row);
        #self.update_dataStage01ReplicatesMI(dataListUpdated_I);
        self.session.commit();
        #self.add_rows_table('data_stage01_quantification_replicatesMI',data_O)