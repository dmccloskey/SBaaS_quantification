
from .stage01_quantification_physiologicalRatios_io import stage01_quantification_physiologicalRatios_io
from .stage01_quantification_replicatesMI_query import stage01_quantification_replicatesMI_query
from .stage01_quantification_replicates_query import stage01_quantification_replicates_query
from .stage01_quantification_physiologicalRatios_dependencies import stage01_quantification_physiologicalRatios_dependencies
#TODO: Remove after making add methods
from .stage01_quantification_physiologicalRatios_postgresql_models import *
#TODO: Remove after moving visualization to io
from matplotlib_utilities.matplot import matplot
#Resources
import numpy
from math import sqrt
from python_statistics.calculate_interface import calculate_interface

class stage01_quantification_physiologicalRatios_execute(stage01_quantification_physiologicalRatios_io,
                                                    stage01_quantification_physiologicalRatios_dependencies,
                                                    stage01_quantification_replicatesMI_query):
    def execute_physiologicalRatios_replicates(self,experiment_id_I):
        '''Calculate physiologicalRatios from replicates'''

        calc = calculate_interface();
        print('calculate_physiologicalRatios_replicates...')
        stage01quantificationreplicatesquery = stage01_quantification_replicates_query(self.session,self.engine,self.settings)
        # get sample names short
        sample_names_short = [];
        sample_names_short = stage01quantificationreplicatesquery.get_SampleNameShort_experimentID_dataStage01Replicates(experiment_id_I);
        ratios_calc_O = [];
        for sns in sample_names_short:
            print('calculating physiologicalRatios from replicates for sample_names_short ' + sns);
            # get time points
            time_points = [];
            time_points = stage01quantificationreplicatesquery.get_timePoint_experimentIDAndSampleNameShort_dataStage01Replicates(experiment_id_I,sns);
            for tp in time_points:
                print('calculating physiologicalRatios from replicates for time_point ' + tp);
                for k,v in self.ratios.items():
                    print('calculating physiologicalRatios from replicates for ratio ' + k);
                    ratios_data={};
                    calcratios=True;
                    for cgn in v['component_group_name']:
                        ratios_data[cgn] = None;
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = stage01quantificationreplicatesquery.get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentGroupName_dataStage01Replicates(experiment_id_I,sns,tp,cgn);
                        if not(conc): 
                            calcratios=False;
                            break;
                        ratios_data[cgn]=conc;
                    # calculate the physiologicalratios
                    if not calcratios: continue
                    ratio_calc,num_calc,den_calc = self.calculate_physiologicalRatios(k,ratios_data);
                    # add data to the session
                    row = {"experiment_id":experiment_id_I,
                        "sample_name_short":sns,
                        "time_point":tp,
                        "physiologicalratio_id":k,
                        "physiologicalratio_name":v['name'],
                        "physiologicalratio_value":ratio_calc,
                        "physiologicalratio_description":v['description'],
                        "used_":True,
                        "comment_":None}   
                    data_O.append(row);
                    row = {"experiment_id":experiment_id_I,
                        "sample_name_short":sns,
                        "time_point":tp,
                        "physiologicalratio_id":k+'_numerator',
                        "physiologicalratio_name":v['name']+'_numerator',
                        "physiologicalratio_value":num_calc,
                        "physiologicalratio_description":v['description'].split('/')[0],
                        "used_":True,
                        "comment_":None}   
                    data_O.append(row);
                    row = {"experiment_id":experiment_id_I,
                        "sample_name_short":sns,
                        "time_point":tp,
                        "physiologicalratio_id":k+'_denominator',
                        "physiologicalratio_name":v['name']+'_denominator',
                        "physiologicalratio_value":den_calc,
                        "physiologicalratio_description":v['description'].split('/')[1],
                        "used_":True,
                        "comment_":None}
                    data_O.append(row);
                        
        self.add_rows_table('data_stage01_quantification_physiologicalRatios_replicates',data_O);
    def execute_physiologicalRatios_averages(self,experiment_id_I):
        '''Calculate physiologicalRatios_averages from physiologicalRatios_replicates'''
        calc = calculate_interface();
        
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
    def execute_physiologicalRatios_replicatesMI(self,experiment_id_I):
        '''Calculate physiologicalRatios from replicates MI'''
        calc = calculate_interface();
        print('calculate_physiologicalRatios_replicates...')
        # get sample names short
        sample_names_short = [];
        sample_names_short = self.get_SampleNameShort_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        ratios_calc_O = [];
        for sns in sample_names_short:
            print('calculating physiologicalRatios from replicates for sample_names_short ' + sns);
            # get time points
            time_points = [];
            time_points = self.get_timePoint_experimentIDAndSampleNameShort_dataStage01ReplicatesMI(experiment_id_I,sns);
            for tp in time_points:
                print('calculating physiologicalRatios from replicates for time_point ' + tp);
                for k,v in self.ratios.items():
                    print('calculating physiologicalRatios from replicates for ratio ' + k);
                    ratios_data={};
                    calcratios=True;
                    for cgn in v['component_group_name']:
                        ratios_data[cgn] = None;
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentGroupName_dataStage01ReplicatesMI(experiment_id_I,sns,tp,cgn);
                        if not(conc): 
                            calcratios=False;
                            break;
                        ratios_data[cgn]=conc;
                    # calculate the physiologicalratios
                    if not calcratios: continue
                    ratio_calc,num_calc,den_calc = self.calculate_physiologicalRatios(k,ratios_data);
                    # add data to the session
                    row = data_stage01_quantification_physiologicalRatios_replicates(experiment_id_I,
                                                                                    sns,
                                                                                    tp,
                                                                                    k,
                                                                                    v['name'],
                                                                                    ratio_calc,
                                                                                    v['description'],
                                                                                    True,
                                                                                    None);   
                    self.session.add(row);
                    row = data_stage01_quantification_physiologicalRatios_replicates(experiment_id_I,
                                                                                    sns,
                                                                                    tp,
                                                                                    k+'_numerator',
                                                                                    v['name']+'_numerator',
                                                                                    num_calc,
                                                                                    v['description'].split('/')[0],
                                                                                    True,
                                                                                    None);   
                    self.session.add(row);
                    row = data_stage01_quantification_physiologicalRatios_replicates(experiment_id_I,
                                                                                    sns,
                                                                                    tp,
                                                                                    k+'_denominator',
                                                                                    v['name']+'_denominator',
                                                                                    den_calc,
                                                                                    v['description'].split('/')[1],
                                                                                    True,
                                                                                    None);   
                    self.session.add(row);
        self.session.commit(); 

    