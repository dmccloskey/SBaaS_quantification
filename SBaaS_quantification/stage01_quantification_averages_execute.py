
from .stage01_quantification_averages_io import stage01_quantification_averages_io
from .stage01_quantification_replicatesMI_query import stage01_quantification_replicatesMI_query
from .stage01_quantification_normalized_query import stage01_quantification_normalized_query
#TODO: Remove after making add methods
from .stage01_quantification_averages_postgresql_models import *
#Resources
import numpy
from math import sqrt
from python_statistics.calculate_interface import calculate_interface

class stage01_quantification_averages_execute(stage01_quantification_averages_io,
                                              stage01_quantification_replicatesMI_query,
                                              stage01_quantification_normalized_query):
    
    def execute_calculateAverages_replicates(self,experiment_id_I,sample_name_abbreviations_I=[]):
        '''Calculate the averages from replicates MI'''
        
        print('execute_calculateAverages_replicates...')
        data_O = [];
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
                    row = {
                        "experiment_id":experiment_id_I, 
                        "sample_name_abbreviation":sna, 
                        "time_point":tp, 
                        "component_group_name":component_group_name, 
                        "component_name":cn,
                        "n_replicates":n_replicates, 
                        "calculated_concentration_average":conc_average, 
                        "calculated_concentration_cv":conc_cv, 
                        "calculated_concentration_units":conc_units, 
                        "used_":True
                        };   
                    data_O.append(row);
        self.add_rows_table('data_stage01_quantification_averagesMI',data_O)
    def execute_calculateGeoAverages_replicates(
        self,
        experiment_id_I,
        sample_name_abbreviations_I=[],
        time_points_I=[],
        calculated_concentration_units_I=[],
        ):
        '''Calculate the averages from replicates MI in ln space'''

        calc = calculate_interface();

        print(' execute_calculateGeoAverages_replicates...')
        data_O = [];
        # get unique calculated_concentration_units/sample_name_abbreviations/component_names/component_group_names/time_points
        unique_rows = [];
        unique_rows = self.get_sampleNameAbbreviationsAndCalculatedConcentrationUnitsAndTimePointsAndComponentNames_experimentID_dataStage01QuantificationReplicatesMI(
            experiment_id_I,
            sample_name_abbreviations_I,
            time_points_I,
            calculated_concentration_units_I,
            exp_type_I=4)
        for unique_row in unique_rows:
            # get sample names short
            sample_names_short = [];
            sample_names_short = self.get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndComponentNameAndTimePointAndCalculatedConcentrationUnits_dataStage01ReplicatesMI(
                experiment_id_I,
                unique_row['sample_name_abbreviation'],
                unique_row['component_name'],
                unique_row['time_point'],
                unique_row['calculated_concentration_units']
                );
            concs = [];
            conc_units = None;
            for sns in sample_names_short:
                # concentrations and units
                conc = None;
                conc = self.get_calculatedConcentration_experimentIDAndSampleNameShortAndTimePointAndComponentNameAndCalculatedConcentrationUnits_dataStage01ReplicatesMI(
                    experiment_id_I,
                    sns,
                    unique_row['time_point'],
                    unique_row['component_name'],
                    unique_row['calculated_concentration_units']
                    );
                if (not(conc) or conc==0): continue;
                # calculate the ln of the concentration
                # and convert to M from mM or uM
                if (unique_row['calculated_concentration_units'] == 'mM'): 
                    conc_units = 'M'; 
                    conc = conc*1e-3;
                elif (unique_row['calculated_concentration_units'] == 'uM'):
                    conc_units = 'M'; 
                    conc = conc*1e-6;
                elif (unique_row['calculated_concentration_units'] == 'uM'):
                    conc_units = 'M'; 
                    conc = conc*1e-6;
                elif (unique_row['calculated_concentration_units'] == 'umol*gDW-1'):
                    conc_units = 'M'; 
                    #conc_units = 'mol*gDW-1';
                    conc = conc*1e-6;
                elif (unique_row['calculated_concentration_units'] == 'height_ratio' \
                    or unique_row['calculated_concentration_units'] == 'area_ratio'):
                    continue;
                else:
                    print('units of ' + str(unique_row['calculated_concentration_units']) + ' are not supported')
                    exit(-1);
                concs.append(conc);
            n_replicates = len(concs);
            conc_average = 0.0;
            conc_var = 0.0;
            conc_lb = 0.0;
            conc_ub = 0.0;
            # calculate average and CV of concentrations
            if (not(concs)): 
                continue
            elif n_replicates<2: 
                continue
            else: 
                conc_average, conc_var, conc_lb, conc_ub = calc.calculate_ave_var_geometric(concs);

            # add data to the session
            row = {"experiment_id":experiment_id_I, 
                "sample_name_abbreviation":unique_row['sample_name_abbreviation'], 
                "time_point":unique_row['time_point'], 
                "component_group_name":unique_row['component_group_name'], 
                "component_name":unique_row['component_name'],
                "n_replicates":n_replicates, 
                "calculated_concentration_average":conc_average, 
                "calculated_concentration_var":conc_var, 
                "calculated_concentration_lb":conc_lb, 
                "calculated_concentration_ub":conc_ub, 
                "calculated_concentration_units":conc_units, 
                "used_":True
                };   
            data_O.append(row);
        self.add_rows_table('data_stage01_quantification_averagesmigeo',data_O)
    def execute_calculateGeoAverages_replicates_v1(
        self,
        experiment_id_I,
        sample_name_abbreviations_I=[],
        ):
        '''Calculate the averages from replicates MI in ln space'''

        calc = calculate_interface();

        print(' execute_calculateGeoAverages_replicates...')
        data_O = [];
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I;
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01ReplicatesMI(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('calculating the geometric average from replicates for sample_name_abbreviation ' + sna);
            # get component names
            component_names = [];
            component_names = self.get_componentNames_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,sna);
            # get time points
            time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(experiment_id_I,sna);
            for cn in component_names:
                print('calculating the geometric average from replicates for component_names ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                for tp in time_points:
                    print('calculating the geometric average from replicates for time_points ' + tp);
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
                        if (not(conc) or conc==0): continue;
                        # calculate the ln of the concentration
                        # and convert to M from mM or uM
                        if (conc_unit == 'mM'): 
                            conc_units = 'M'; 
                            conc = conc*1e-3;
                        elif (conc_unit == 'uM'):
                            conc_units = 'M'; 
                            conc = conc*1e-6;
                        elif (conc_unit == 'uM'):
                            conc_units = 'M'; 
                            conc = conc*1e-6;
                        elif (conc_unit == 'umol*gDW-1'):
                            conc_units = 'mol*gDW-1';
                            conc = conc*1e-6;
                        elif (conc_unit == 'height_ratio' or conc_unit == 'area_ratio'):
                            continue;
                        else:
                            print('units of ' + str(conc_unit) + ' are not supported')
                            exit(-1);
                        concs.append(conc);
                    n_replicates = len(concs);
                    conc_average = 0.0;
                    conc_var = 0.0;
                    conc_lb = 0.0;
                    conc_ub = 0.0;
                    # calculate average and CV of concentrations
                    if (not(concs)): 
                        continue
                    elif n_replicates<2: 
                        continue
                    else: 
                        conc_average, conc_var, conc_lb, conc_ub = calc.calculate_ave_var_geometric(concs);

                    # add data to the session
                    row = {"experiment_id":experiment_id_I, 
                        "sample_name_abbreviation":sna, 
                        "time_point":tp, 
                        "component_group_name":component_group_name, 
                        "component_name":cn,
                        "n_replicates":n_replicates, 
                        "calculated_concentration_average":conc_average, 
                        "calculated_concentration_var":conc_var, 
                        "calculated_concentration_lb":conc_lb, 
                        "calculated_concentration_ub":conc_ub, 
                        "calculated_concentration_units":conc_units, 
                        "used_":True
                        };   
                    data_O.append(row);
        self.add_rows_table('data_stage01_quantification_averagesMIgeo',data_O)
    