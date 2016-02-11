#Resources
import numpy

from .stage01_quantification_replicates_io import stage01_quantification_replicates_io
from .stage01_quantification_normalized_query import stage01_quantification_normalized_query
from .stage01_quantification_QCs_query import stage01_quantification_QCs_query
from SBaaS_LIMS.lims_biologicalMaterial_query import lims_biologicalMaterial_query
#TODO: remove after making add method
from .stage01_quantification_replicates_postgresql_models import *
#TODO: remove after refactor
from r_statistics.r_interface import r_interface
from python_statistics.calculate_interface import calculate_interface

class stage01_quantification_replicates_execute(stage01_quantification_replicates_io,
                                                stage01_quantification_normalized_query,
                                                stage01_quantification_QCs_query,
                                                lims_biologicalMaterial_query):
    def execute_analyzeReplicates(self,experiment_id_I,sample_name_abbreviations_I=[],sample_names_I=[],component_names_I=[]):
        '''calculate the replicates by subtracting out the filtrate
        NOTE: data_stage01_quantification_normalized must be populated'''
        # Input:
        #   experiment_id
        # Output:
        #   sample_name_short
        #   component_group_name
        #   component_name
        #   concentration
        #   concentration units
        
        print('execute_analyzeReplicates...')
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01Normalized(experiment_id_I);
        # create database table
        for sna in sample_name_abbreviations:
            print('analyzing replicates for sample_name_abbreviation ' + sna);
            # get component names
            if component_names_I:
                component_names = component_names_I
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
            for cn in component_names:
                print('analyzing replicates for component_name ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                # get time points
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
                for tp in time_points:
                    print('analyzing replicates for time_point ' + tp);
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
                        if not(conc): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates = len(concs);
                    conc_average_filtrate = 0.0;
                    conc_var_filtrate = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): conc_average_filtrate = 0;
                    elif n_replicates<2: conc_average_filtrate = concs[0];
                    else: 
                        conc_average_filtrate = numpy.mean(numpy.array(concs));
                        conc_var_filtrate = numpy.var(numpy.array(concs));
                    # get filtrate sample names
                    sample_names = [];
                    sample_description = 'Broth';
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(experiment_id_I,sna,sample_description,cn,tp);
                    if sample_names_I: # screen out sample names that are not in the input
                        sample_names = [x for x in sample_names if x in sample_names_I];
                    for sn in sample_names:
                        print('analyzing replicates for sample_name ' + sn);
                        # query concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if (not(conc) or conc==0): continue # record all replicate broth samples whether they were measured or not 
                                                             # needed for MI2 later on
                        if (conc_unit): conc_units = conc_unit;
                        # subract out filtrate average from each broth
                        conc_broth = 0.0;
                        if conc:
                            conc_broth = conc-conc_average_filtrate;
                            if (conc_broth < 0 ): conc_broth = None;
                        else: conc_broth = None;
                        # get sample name short
                        sample_name_short = self.get_sampleNameShort_experimentIDAndSampleName_dataStage01Normalized(experiment_id_I, sn);
                        # add data to the session 
                        row = data_stage01_quantification_replicates(experiment_id_I, sample_name_short, tp, component_group_name, cn,
                                                                conc_broth, conc_units, True,None);
                        self.session.add(row);
            self.session.commit();    