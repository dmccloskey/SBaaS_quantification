from .stage01_quantification_outliers_io import stage01_quantification_outliers_io
from SBaaS_quantification.stage01_quantification_replicates_query import stage01_quantification_replicates_query
# resources
from r_statistics.r_interface import r_interface
from matplotlib_utilities.matplot import matplot
# remove after making add methods
from .stage01_quantification_outliers_postgresql_models import *

class stage01_quantification_outliers_execute(stage01_quantification_outliers_io,
                                                   stage01_quantification_replicates_query):
    def execute_calculateOutliersDeviation_dataStage01QuantificationReplicates(self,analysis_id_I,concentration_units_I=[]):
        '''calculate outliers based on their deviation
        INPUT:
        OUTPUT:
        '''

        print('execute_getDataStage01ReplicatesMI...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data_transformed = [];
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            for row in analysis_info:
                concentration_units_tmp = [];
                concentration_units_tmp = self.get_concentrationUnits_experimentID_dataStage01Replicates(row['experiment_id']);
                concentration_units.extend(concentration_units_tmp);
            concentration_units = list(set(concentration_units));
        for cu in concentration_units:
            print('calculating glogNormalization for concentration_units ' + cu);
        
        
        print('execute_calculateAverages_replicates...')
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I;
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01Replicates(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('calculating averages from replicates for sample_name_abbreviation ' + sna);
            # get component names
            component_names = [];
            component_names = self.get_componentNames_experimentIDAndSampleNameAbbreviation_dataStage01Replicates(experiment_id_I,sna);
            for cn in component_names:
                print('calculating averages from replicates for component_name ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                # get time points
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Replicates(experiment_id_I,sna);
                for tp in time_points:
                    print('calculating averages from replicates for time_point ' + tp);
                    # get sample names short
                    sample_names_short = [];
                    sample_names_short = self.get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndComponentNameAndTimePoint_dataStage01Replicates(experiment_id_I,sna,cn,tp);
                    concs = [];
                    conc_units = None;
                    for sns in sample_names_short:
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentName_dataStage01Replicates(experiment_id_I,sns,tp,cn);
                        if (not(conc) or conc==0): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates = len(concs);
                    conc_average = 0.0;
                    conc_var = 0.0;
                    conc_cv = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        continue
                    elif n_replicates<2: 
                        continue
                    else: 
                        conc_average = numpy.mean(numpy.array(concs));
                        conc_var = numpy.var(numpy.array(concs));
                        if (conc_average <= 0): conc_cv = 0;
                        else: conc_cv = sqrt(conc_var)/conc_average*100; 

                    # add data to the session
                    row = data_stage01_quantification_averagesMI(experiment_id_I, sna, tp, component_group_name, cn,
                                                   n_replicates, conc_average, conc_cv, conc_units, True);   
                    self.session.add(row);
            self.session.commit(); 
    def execute_calculateOutliersDeviation_dataStage01QuantificationReplicatesMI(self,analysis_id_I,concentration_units_I=[]):
        '''calculate outliers based on their deviation
        INPUT:
        OUTPUT:
        '''

        print('execute_getDataStage01ReplicatesMI...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data_transformed = [];
        if concentration_units_I:
            concentration_units = concentration_units_I;
        else:
            concentration_units = [];
            for row in analysis_info:
                concentration_units_tmp = [];
                concentration_units_tmp = self.get_concentrationUnits_experimentID_dataStage01ReplicatesMI(row['experiment_id']);
                concentration_units.extend(concentration_units_tmp);
            concentration_units = list(set(concentration_units));
        for cu in concentration_units:
            print('calculating glogNormalization for concentration_units ' + cu);
        
        print('execute_calculateAverages_replicates...')
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I;
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('calculating averages from replicates for sample_name_abbreviation ' + sna);
            # get component names
            component_names = [];
            component_names = self.get_componentNames_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,sna);
            for cn in component_names:
                print('calculating averages from replicates for component_name ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                # get time points
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,sna);
                for tp in time_points:
                    print('calculating averages from replicates for time_point ' + tp);
                    # get sample names short
                    sample_names_short = [];
                    sample_names_short = self.get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndComponentNameAndTimePoint_dataStage01ReplicatesMI(experiment_id_I,sna,cn,tp);
                    concs = [];
                    conc_units = None;
                    for sns in sample_names_short:
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentName_dataStage01ReplicatesMI(experiment_id_I,sns,tp,cn);
                        if (not(conc) or conc==0): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates = len(concs);
                    conc_average = 0.0;
                    conc_var = 0.0;
                    conc_cv = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        continue
                    elif n_replicates<2: 
                        continue
                    else: 
                        conc_average = numpy.mean(numpy.array(concs));
                        conc_var = numpy.var(numpy.array(concs));
                        if (conc_average <= 0): conc_cv = 0;
                        else: conc_cv = sqrt(conc_var)/conc_average*100; 

                    # add data to the session
                    row = data_stage01_quantification_averagesMI(experiment_id_I, sna, tp, component_group_name, cn,
                                                   n_replicates, conc_average, conc_cv, conc_units, True);   
                    self.session.add(row);
            self.session.commit(); 
    def execute_calculateOutliersDeviation_dataStage01PhysiologicalRatios(self,analysis_id_I):
        '''calculate outliers based on their deviation
        INPUT:
        OUTPUT:
        '''

        print('execute_getDataStage01ReplicatesMI...')
        
        # get the analysis information
        analysis_info = [];
        analysis_info = self.get_rows_analysisID_dataStage02QuantificationAnalysis(analysis_id_I);
        # query metabolomics data from the experiment
        data = [];
        # get all of the samples in the simulation
        for row in analysis_info:
            data_tmp = [];
            data_tmp = self.get_RExpressionData_AnalysisIDAndExperimentIDAndSampleNameShortAndTimePoint_dataStage01PhysiologicalRatiosReplicates(analysis_id_I,row['experiment_id'], row['sample_name_short'], row['time_point']);
            data.extend(data_tmp)
        # upload data
        for d in data:
            row = None;
        
        print('calculate_physiologicalRatios_averages...')
        # get sample_name_abbreviations
        sample_name_abbreviations = [];
        sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('calculating physiologicalRatios from replicates for sample_name_abbreviation ' + sna);
            # get time points
            time_points = [];
            time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sna);
            for tp in time_points:
                print('calculating physiologicalRatios from replicates for time_point ' + tp);
                # get ratio information
                ratio_info = {};
                ratio_info = self.get_ratioIDs_experimentIDAndTimePoint_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,tp)
                #for k,v in self.ratios.iteritems():
                for k,v in ratio_info.items():
                    print('calculating physiologicalRatios from replicates for ratio ' + k);
                    # get sample names short
                    sample_names_short = [];
                    sample_names_short = self.get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndRatioIDAndTimePoint_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sna,k,tp);
                    ratios = [];
                    for sns in sample_names_short:
                        # get ratios
                        ratio = None;
                        ratio = self.get_ratio_experimentIDAndSampleNameShortAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sns,tp,k);
                        if not ratio: continue;
                        ratios.append(ratio);
                    n_replicates = len(ratios);
                    ratio_average = 0.0;
                    ratio_var = 0.0;
                    ratio_cv = 0.0;
                    ratio_lb = 0.0;
                    ratio_ub = 0.0;
                    # calculate average and CV of ratios
                    if (not(ratios)): 
                        continue
                    elif n_replicates<2: 
                        continue
                    else: 
                        ratio_average,ratio_var,ratio_lb,ratio_ub = calc.calculate_ave_var(ratios);
                        if (ratio_average <= 0): ratio_cv = 0;
                        else: ratio_cv = sqrt(ratio_var)/ratio_average*100; 
                    # add data to the session
                    row = data_stage01_quantification_physiologicalRatios_averages(experiment_id_I, 
                                                                               sna,
                                                                               tp,
                                                                               k,
                                                                               v['name'],
                                                                               ratio_average,
                                                                               ratio_cv,
                                                                               ratio_lb,
                                                                               ratio_ub,
                                                                               v['description'],
                                                                               True,
                                                                               None);   
                    self.session.add(row);
        self.session.commit(); 

