﻿from .stage01_quantification_peakInformation_io import stage01_quantification_peakInformation_io
from SBaaS_LIMS.lims_experiment_query import lims_experiment_query
#Resources
from python_statistics.calculate_interface import calculate_interface
#TODO: remove after refactoring io
from .stage01_quantification_peakInformation_postgresql_models import *
from math import sqrt

class stage01_quantification_peakInformation_execute(stage01_quantification_peakInformation_io,
                                                    lims_experiment_query):
    def execute_analyzePeakInformation(self,experiment_id_I=[],analysis_id_I=[],
                            sample_names_I=[],sample_ids_I=[],
                            sample_types_I=['Standard'],
                            component_names_I=[],
                            peakInfo_I = ['height','retention_time','width_at_50','signal_2_noise'],
                            acquisition_date_and_time_I=[None,None]):
        '''Analyze retention-time, height, s/n, and assymetry
        INPUT:
        experiment_id_I
        sample_names_I
        sample_types_I
        component_names_I
        peakInfo_I
        acquisition_date_and_time_I = ['%m/%d/%Y %H:%M','%m/%d/%Y %H:%M']
        '''

        print('execute_peakInformation...')
        
        #convert string date time to datetime
        # e.g. time.strptime('4/15/2014 15:51','%m/%d/%Y %H:%M')
        acquisition_date_and_time = [];
        if acquisition_date_and_time_I and acquisition_date_and_time_I[0] and acquisition_date_and_time_I[1]:
            for dateandtime in acquisition_date_and_time_I:
                time_struct = strptime(dateandtime,'%m/%d/%Y %H:%M')
                dt = datetime.fromtimestamp(mktime(time_struct))
                acquisition_date_and_time.append(dt);
        else: acquisition_date_and_time=[None,None]
        data_O = [];

        data_O = self.get_rows_dataStage01QuantificationMQResultsTable(
            analysis_id_I = analysis_id_I,
            experiment_id_I = experiment_id_I,
            sample_name_I = sample_names_I,
            sample_id_I = sample_ids_I,
            sample_type_I = sample_types_I,
            component_name_I = component_names_I,
            acquisition_date_and_time_I = acquisition_date_and_time,
            )

        component_names_all = [d['component_name'] for d in data_O];
        sample_names = [d['sample_name'] for d in data_O];
        sample_types = [d['sample_type'] for d in data_O];

        #component_names_all = []
        ## get sample names
        #if sample_names_I and sample_types_I and len(sample_types_I)==1:
        #    sample_names = sample_names_I;
        #    sample_types = [sample_types_I[0] for sn in sample_names];
        #else:
        #    sample_names = [];
        #    sample_types = [];
        #    for st in sample_types_I:
        #        sample_names_tmp = [];
        #        sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
        #        sample_names.extend(sample_names_tmp);
        #        sample_types_tmp = [];
        #        sample_types_tmp = [st for sn in sample_names_tmp];
        #        sample_types.extend(sample_types_tmp);
        #print(str(len(sample_names)) + ' total samples');
        #for sn in sample_names:
        #    print('analyzing peakInformation for sample_name ' + sn);
        #    # get sample description
        #    desc = {};
        #    desc = self.get_description_experimentIDAndSampleID_sampleDescription(experiment_id_I,sn);
        #    # get component names
        #    if component_names_I:
        #        component_names = component_names_I;
        #    else:
        #        component_names = [];
        #        component_names = self.get_componentsNames_experimentIDAndSampleName(experiment_id_I,sn);
        #    component_names_all.extend(component_names);
        #    for cn in component_names:
        #        # get rt, height, s/n
        #        sst_data = {};
        #        sst_data = self.get_peakInfo_sampleNameAndComponentName(sn,cn,acquisition_date_and_time);
        #        if sst_data:
        #            tmp = {};
        #            tmp.update(sst_data);
        #            tmp.update(desc);
        #            tmp.update({'sample_name':sn});
        #            data_O.append(tmp);
        #TODO:
        # 1. optimize using pandas or numpy
        # calculate statistics for specific parameters
        data_add = [];
        component_names_unique = list(set(component_names_all));
        component_names_unique.sort();
        # math utilities
        from math import sqrt
        calc = calculate_interface();
        for cn in component_names_unique:
            data_parameters = {};
            data_parameters_stats = {};
            for parameter in peakInfo_I:
                data_parameters[parameter] = [];
                data_parameters_stats[parameter] = {'ave':None,'var':None,'cv':None,'lb':None,'ub':None};
                acquisition_date_and_times = [];
                sample_names_parameter = [];
                sample_types_parameter = [];
                component_group_name = None;
                for sn_cnt,sn in enumerate(sample_names):
                    for d in data_O:
                        if d['sample_name'] == sn and d['component_name'] == cn and d[parameter]:
                            data_parameters[parameter].append(d[parameter]);
                            acquisition_date_and_times.append(d['acquisition_date_and_time'])
                            sample_names_parameter.append(sn);
                            sample_types_parameter.append(sample_types[sn_cnt])
                            component_group_name = d['component_group_name'];
                ave,var,lb,ub = None,None,None,None;
                if len(data_parameters[parameter])>1:
                    ave,var,lb,ub = calc.calculate_ave_var(data_parameters[parameter]);
                if ave:
                    cv = sqrt(var)/ave*100;
                    data_parameters_stats[parameter] = {'ave':ave,'var':var,'cv':cv,'lb':lb,'ub':ub};
                    # add data to the DB
                    row = {'experiment_id':experiment_id_I,
                        'component_group_name':component_group_name,
                        'component_name':cn,
                        'peakInfo_parameter':parameter,
                        'peakInfo_ave':data_parameters_stats[parameter]['ave'],
                        'peakInfo_cv':data_parameters_stats[parameter]['cv'],
                        'peakInfo_lb':data_parameters_stats[parameter]['lb'],
                        'peakInfo_ub':data_parameters_stats[parameter]['ub'],
                        'peakInfo_units':None,
                        'sample_names':sample_names_parameter,
                        'sample_types':sample_types_parameter,
                        'acqusition_date_and_times':acquisition_date_and_times,
                        'peakInfo_data':data_parameters[parameter],
                        'used_':True,
                        'comment_':None,};
                    data_add.append(row);
        self.add_rows_table('data_stage01_quantification_peakInformation',data_add);
    def execute_analyzePeakResolution(self,experiment_id_I,sample_names_I=[],sample_types_I=['Standard'],component_name_pairs_I=[],
                            acquisition_date_and_time_I=[None,None]):
        '''Analyze resolution for critical pairs
        Input:
        experiment_id_I
        sample_names_I
        sample_types_I
        component_name_pairs_I = [[component_name_1,component_name_2],...]
        acquisition_date_and_time_I = ['%m/%d/%Y %H:%M','%m/%d/%Y %H:%M']
        '''

        print('execute_peakInformation_resolution...')
        #convert string date time to datetime
        # e.g. time.strptime('4/15/2014 15:51','%m/%d/%Y %H:%M')
        acquisition_date_and_time = [];
        if acquisition_date_and_time_I and acquisition_date_and_time_I[0] and acquisition_date_and_time_I[1]:
            for dateandtime in acquisition_date_and_time_I:
                time_struct = strptime(dateandtime,'%m/%d/%Y %H:%M')
                dt = datetime.fromtimestamp(mktime(time_struct))
                acquisition_date_and_time.append(dt);
        else: acquisition_date_and_time=[None,None]
        data_O = [];
        component_names_pairs_all = [];
        # get sample names
        if sample_names_I and sample_types_I and len(sample_types_I)==1:
            sample_names = sample_names_I;
            sample_types = [sample_types_I[0] for sn in sample_names];
        else:
            sample_names = [];
            sample_types = [];
            for st in sample_types_I:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
                sample_types_tmp = [];
                sample_types_tmp = [st for sn in sample_names_tmp];
                sample_types.extend(sample_types_tmp);
        for sn in sample_names:
            print('analyzing peakInformation for sample_name ' + sn);
            for component_name_pair in component_name_pairs_I:
                # get critical pair data
                cpd1 = {};
                cpd2 = {};
                cpd1 = self.get_peakInfo_sampleNameAndComponentName(sn,component_name_pair[0],acquisition_date_and_time);
                cpd2 = self.get_peakInfo_sampleNameAndComponentName(sn,component_name_pair[1],acquisition_date_and_time);
                if cpd1 and cpd2 and cpd1['retention_time'] and cpd2['retention_time']:
                    # calculate the RT difference and resolution
                    rt_dif = 0.0;
                    rt_dif = abs(cpd1['retention_time']-cpd2['retention_time'])
                    resolution = 0.0;
                    resolution = rt_dif/(0.5*(cpd1['width_at_50']+cpd2['width_at_50']));
                    # record data
                    data_O.append({'component_name_pair':component_name_pair,
                                   'rt_dif':rt_dif,
                                   'resolution':resolution,
                                   'component_group_name_pair':[cpd1['component_group_name'],cpd2['component_group_name']],
                                   'sample_name':sn,
                                   'acquisition_date_and_time':cpd1['acquisition_date_and_time']});
        #TODO:
        # 1. make a calculation method
        # calculate statistics for specific parameters
        data_add = [];
        calc = calculate_interface();
        for cnp in component_name_pairs_I:
            data_parameters = {};
            data_parameters_stats = {};
            for parameter in ['rt_dif','resolution']:
                data_parameters[parameter] = [];
                data_parameters_stats[parameter] = {'ave':None,'var':None,'cv':None,'lb':None,'ub':None};
                acquisition_date_and_times = [];
                sample_names_parameter = [];
                sample_types_parameter = [];
                component_group_name_pair = None;
                for sn_cnt,sn in enumerate(sample_names):
                    for d in data_O:
                        if d['sample_name'] == sn and d['component_name_pair'] == cnp and d[parameter]:
                            data_parameters[parameter].append(d[parameter]);
                            acquisition_date_and_times.append(d['acquisition_date_and_time'])
                            sample_names_parameter.append(sn);
                            sample_types_parameter.append(sample_types[sn_cnt])
                            component_group_name_pair = d['component_group_name_pair'];
                ave,var,lb,ub = None,None,None,None;
                if len(data_parameters[parameter])>1:ave,var,lb,ub = calc.calculate_ave_var(data_parameters[parameter]);
                if ave:
                    cv = sqrt(var)/ave*100;
                    data_parameters_stats[parameter] = {'ave':ave,'var':var,'cv':cv,'lb':lb,'ub':ub};
                    # add data to the database:
                    row = {'experiment_id':experiment_id_I,
                        'component_group_name_pair':component_group_name_pair,
                        'component_name_pair':cnp,
                        'peakInfo_parameter':parameter,
                        'peakInfo_ave':data_parameters_stats[parameter]['ave'],
                        'peakInfo_cv':data_parameters_stats[parameter]['cv'],
                        'peakInfo_lb':data_parameters_stats[parameter]['lb'],
                        'peakInfo_ub':data_parameters_stats[parameter]['ub'],
                        'peakInfo_units':None,
                        'sample_names':sample_names_parameter,
                        'sample_types':sample_types_parameter,
                        'acqusition_date_and_times':acquisition_date_and_times,
                        'peakInfo_data':data_parameters[parameter],
                        'used_':True,
                        'comment_':None,};
                    data_add.append(row);
        self.add_rows_table('data_stage01_quantification_peakResolution',data_add);

    