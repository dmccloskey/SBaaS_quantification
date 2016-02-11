# System
import json,re
# SBaaS
from .stage01_quantification_peakInformation_query import stage01_quantification_peakInformation_query
from .stage01_quantification_MQResultsTable_query import stage01_quantification_MQResultsTable_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from matplotlib_utilities.matplot import matplot
from SBaaS_base.sbaas_template_io import sbaas_template_io

class stage01_quantification_peakInformation_io(stage01_quantification_peakInformation_query,
                                                stage01_quantification_MQResultsTable_query,
                                                sbaas_template_io):
    def export_scatterLinePlot_peakInformation_matplot(self,experiment_id_I,sample_names_I=[],
                            sample_types_I=['Standard'],
                            component_names_I=[],
                            peakInfo_I = ['retention_time'],
                            acquisition_date_and_time_I=[None,None],
                            x_title_I='Time [hrs]',y_title_I='Retention Time [min]',y_data_type_I='acquisition_date_and_time',
                            plot_type_I='single',
                            filename_O = 'tmp',
                            figure_format_O = 'png'):
        '''Analyze retention-time, height, s/n, and assymetry'''

        #INPUT:
        #   experiment_id_I
        #   sample_names_I
        #   sample_types_I
        #   component_names_I
        #   peakInfo_I
        #   acquisition_date_and_time_I = ['%m/%d/%Y %H:%M','%m/%d/%Y %H:%M']
        #   y_data_type_I = 'acquisition_date_and_time' or 'count'
        #   plot_type_I = 'single', 'multiple', or 'sub'

        print('export_peakInformation...')

        #TODO: remove after refactor
        mplot = matplot();
        
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
        component_names_all = [];
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
            # get sample description
            desc = {};
            desc = self.get_description_experimentIDAndSampleID_sampleDescription(experiment_id_I,sn);
            # get component names
            if component_names_I:
                component_names = component_names_I;
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleName(experiment_id_I,sn);
            component_names_all.extend(component_names);
            for cn in component_names:
                # get rt, height, s/n
                sst_data = {};
                sst_data = self.get_peakInfo_sampleNameAndComponentName(sn,cn,acquisition_date_and_time);
                if sst_data:
                    tmp = {};
                    tmp.update(sst_data);
                    tmp.update(desc);
                    tmp.update({'sample_name':sn});
                    data_O.append(tmp);
        # Plot data over time
        if component_names_I:
            # use input order
            component_names_unique = component_names_I;
        else:
            # use alphabetical order
            component_names_unique = list(set(component_names_all));
            component_names_unique.sort();
        if plot_type_I == 'single':
            for cn in component_names_unique:
                data_parameters = {};
                data_parameters_stats = {};
                for parameter in peakInfo_I:
                    data_parameters[parameter] = [];
                    acquisition_date_and_times = [];
                    acquisition_date_and_times_hrs = [];
                    sample_names_parameter = [];
                    sample_types_parameter = [];
                    component_group_name = None;
                    for sn_cnt,sn in enumerate(sample_names):
                        for d in data_O:
                            if d['sample_name'] == sn and d['component_name'] == cn and d[parameter]:
                                data_parameters[parameter].append(d[parameter]);
                                acquisition_date_and_times.append(d['acquisition_date_and_time'])
                                acquisition_date_and_times_hrs.append(d['acquisition_date_and_time'].year*8765.81277 + d['acquisition_date_and_time'].month*730.484  + d['acquisition_date_and_time'].day*365.242 + d['acquisition_date_and_time'].hour + d['acquisition_date_and_time'].minute / 60. + d['acquisition_date_and_time'].second / 3600.); #convert using datetime object
                                sample_names_parameter.append(sn);
                                sample_types_parameter.append(sample_types[sn_cnt])
                                component_group_name = d['component_group_name'];
                    # normalize time
                    acquisition_date_and_times_hrs.sort();
                    t_start = min(acquisition_date_and_times_hrs);
                    for t_cnt,t in enumerate(acquisition_date_and_times_hrs):
                        if y_data_type_I == 'acquisition_date_and_time':acquisition_date_and_times_hrs[t_cnt] = t - t_start;
                        elif y_data_type_I == 'count':acquisition_date_and_times_hrs[t_cnt] = t_cnt;
                    title = cn + '\n' + parameter;
                    filename = filename_O + '_' + experiment_id_I + '_' + cn + '_' + parameter + figure_format_O;
                    mplot.scatterLinePlot(title,x_title_I,y_title_I,acquisition_date_and_times_hrs,data_parameters[parameter],fit_func_I='lowess',show_eqn_I=False,show_r2_I=False,filename_I=filename,show_plot_I=False);
        if plot_type_I == 'multiple':
             for parameter in peakInfo_I:
                data_parameters = [];
                acquisition_date_and_times = [];
                acquisition_date_and_times_hrs = [];
                sample_names_parameter = [];
                sample_types_parameter = [];
                component_group_names = [];
                component_names = [];
                for cn_cnt,cn in enumerate(component_names_unique):
                    data = [];
                    acquisition_date_and_time = [];
                    acquisition_date_and_time_hrs = [];
                    sample_name_parameter = [];
                    sample_type_parameter = [];
                    for sn_cnt,sn in enumerate(sample_names):
                        for d in data_O:
                            if d['sample_name'] == sn and d['component_name'] == cn and d[parameter]:
                                data.append(d[parameter])
                                acquisition_date_and_time.append(d['acquisition_date_and_time'])
                                acquisition_date_and_time_hrs.append(d['acquisition_date_and_time'].year*8765.81277 + d['acquisition_date_and_time'].month*730.484  + d['acquisition_date_and_time'].day*365.242 + d['acquisition_date_and_time'].hour + d['acquisition_date_and_time'].minute / 60. + d['acquisition_date_and_time'].second / 3600.); #convert using datetime object
                                sample_name_parameter.append(sn);
                                sample_type_parameter.append(sample_types[sn_cnt])
                                if sn_cnt == 0:
                                    component_group_names.append(d['component_group_name']);
                                    component_names.append(d['component_name']);
                    # normalize time
                    acquisition_date_and_time_hrs.sort();
                    t_start = min(acquisition_date_and_time_hrs);
                    for t_cnt,t in enumerate(acquisition_date_and_time_hrs):
                        if y_data_type_I == 'acquisition_date_and_time':acquisition_date_and_time_hrs[t_cnt] = t - t_start;
                        elif y_data_type_I == 'count':acquisition_date_and_time_hrs[t_cnt] = t_cnt;
                    data_parameters.append(data);
                    acquisition_date_and_times.append(acquisition_date_and_time)
                    acquisition_date_and_times_hrs.append(acquisition_date_and_time_hrs);
                    sample_names_parameter.append(sample_name_parameter);
                    sample_types_parameter.append(sample_type_parameter)
                title = parameter;
                filename = filename_O + '_' + experiment_id_I + '_' + parameter + figure_format_O;
                mplot.multiScatterLinePlot(title,x_title_I,y_title_I,acquisition_date_and_times_hrs,data_parameters,data_labels_I=component_group_names,fit_func_I=None,show_eqn_I=False,show_r2_I=False,filename_I=filename,show_plot_I=False);
    def export_scatterLinePlot_peakResolution_matplot(self,experiment_id_I,sample_names_I=[],sample_types_I=['Standard'],component_name_pairs_I=[],
                            peakInfo_I = ['rt_dif','resolution'],
                            acquisition_date_and_time_I=[None,None],
                            x_title_I='Time [hrs]',y_title_I='Retention Time [min]',y_data_type_I='acquisition_date_and_time',
                            plot_type_I='single'):
        '''Analyze resolution for critical pairs'''
        #Input:
        #   experiment_id_I
        #   sample_names_I
        #   sample_types_I
        #   component_name_pairs_I = [[component_name_1,component_name_2],...]
        #   acquisition_date_and_time_I = ['%m/%d/%Y %H:%M','%m/%d/%Y %H:%M']

        #TODO: remove after refactor
        mplot = matplot();

        print('export_peakInformation_resolution...')
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
        if plot_type_I == 'single':
            for cnp in component_name_pairs_I:
                data_parameters = {};
                data_parameters_stats = {};
                for parameter in peakInfo_I:
                    data_parameters[parameter] = [];
                    acquisition_date_and_times = [];
                    acquisition_date_and_times_hrs = [];
                    sample_names_parameter = [];
                    sample_types_parameter = [];
                    component_group_name_pair = None;
                    for sn_cnt,sn in enumerate(sample_names):
                        for d in data_O:
                            if d['sample_name'] == sn and d['component_name_pair'] == cnp and d[parameter]:
                                data_parameters[parameter].append(d[parameter]);
                                acquisition_date_and_times.append(d['acquisition_date_and_time'])
                                acquisition_date_and_times_hrs.append(d['acquisition_date_and_time'].year*8765.81277 + d['acquisition_date_and_time'].month*730.484  + d['acquisition_date_and_time'].day*365.242 + d['acquisition_date_and_time'].hour + d['acquisition_date_and_time'].minute / 60. + d['acquisition_date_and_time'].second / 3600.); #convert using datetime object
                                sample_names_parameter.append(sn);
                                sample_types_parameter.append(sample_types[sn_cnt])
                                component_group_name_pair = d['component_group_name_pair'];
                    # normalize time
                    acquisition_date_and_times_hrs.sort();
                    t_start = min(acquisition_date_and_times_hrs);
                    for t_cnt,t in enumerate(acquisition_date_and_times_hrs):
                        if y_data_type_I == 'acquisition_date_and_time':acquisition_date_and_times_hrs[t_cnt] = t - t_start;
                        elif y_data_type_I == 'count':acquisition_date_and_times_hrs[t_cnt] = t_cnt;
                    title = cn + '\n' + parameter;
                    filename = 'data/_output/' + experiment_id_I + '_' + cn + '_' + parameter + '.png'
                    mplot.scatterLinePlot(title,x_title_I,y_title_I,acquisition_date_and_times_hrs,data_parameters[parameter],fit_func_I='lowess',show_eqn_I=False,show_r2_I=False,filename_I=filename,show_plot_I=False);
        if plot_type_I == 'multiple':
             for parameter in peakInfo_I:
                data_parameters = [];
                acquisition_date_and_times = [];
                acquisition_date_and_times_hrs = [];
                sample_names_parameter = [];
                sample_types_parameter = [];
                component_group_names_pair = [];
                component_names_pair = [];
                for cnp_cnt,cnp in enumerate(component_name_pairs_I):
                    data = [];
                    acquisition_date_and_time = [];
                    acquisition_date_and_time_hrs = [];
                    sample_name_parameter = [];
                    sample_type_parameter = [];
                    for sn_cnt,sn in enumerate(sample_names):
                        for d in data_O:
                            if d['sample_name'] == sn and d['component_name_pair'] == cnp and d[parameter]:
                                data.append(d[parameter])
                                acquisition_date_and_time.append(d['acquisition_date_and_time'])
                                acquisition_date_and_time_hrs.append(d['acquisition_date_and_time'].year*8765.81277 + d['acquisition_date_and_time'].month*730.484  + d['acquisition_date_and_time'].day*365.242 + d['acquisition_date_and_time'].hour + d['acquisition_date_and_time'].minute / 60. + d['acquisition_date_and_time'].second / 3600.); #convert using datetime object
                                sample_name_parameter.append(sn);
                                sample_type_parameter.append(sample_types[sn_cnt])
                                if sn_cnt == 0:
                                    component_group_names_pair.append(d['component_group_name_pair']);
                                    component_names_pair.append(d['component_name_pair']);
                    # normalize time
                    acquisition_date_and_time_hrs.sort();
                    t_start = min(acquisition_date_and_time_hrs);
                    for t_cnt,t in enumerate(acquisition_date_and_time_hrs):
                        if y_data_type_I == 'acquisition_date_and_time':acquisition_date_and_time_hrs[t_cnt] = t - t_start;
                        elif y_data_type_I == 'count':acquisition_date_and_time_hrs[t_cnt] = t_cnt;
                    data_parameters.append(data);
                    acquisition_date_and_times.append(acquisition_date_and_time)
                    acquisition_date_and_times_hrs.append(acquisition_date_and_time_hrs);
                    sample_names_parameter.append(sample_name_parameter);
                    sample_types_parameter.append(sample_type_parameter)
                # create data labels
                data_labels = [];
                for component_group_names in component_group_names_pair:
                    data_labels.append(component_group_names[0] + '/' + component_group_names[1]);
                title = parameter;
                filename = 'data/_output/' + experiment_id_I + '_' + parameter + '.eps'
                mplot.multiScatterLinePlot(title,x_title_I,y_title_I,acquisition_date_and_times_hrs,data_parameters,data_labels_I=data_labels,fit_func_I=None,show_eqn_I=False,show_r2_I=False,filename_I=filename,show_plot_I=False);
    
    def export_boxAndWhiskersPlot_peakInformation_matplot(self,experiment_id_I,
                            peakInfo_parameter_I = ['height','retention_time','width_at_50','signal_2_noise'],
                            component_names_I=[],
                            filename_O = 'tmp',
                            figure_format_O = '.png'):
        '''generate a boxAndWhiskers plot from peakInformation table'''

        #TODO: remove after refactor
        mplot = matplot();

        print('export_boxAndWhiskersPlot...')
        if peakInfo_parameter_I:
            peakInfo_parameter = peakInfo_parameter_I;
        else:
            peakInfo_parameter = [];
            peakInfo_parameter = self.get_peakInfoParameter_experimentID_dataStage01PeakInformation(experiment_id_I);
        for parameter in peakInfo_parameter:
            data_plot_mean = [];
            data_plot_cv = [];
            data_plot_ci = [];
            data_plot_parameters = [];
            data_plot_component_names = [];
            data_plot_data = [];
            data_plot_units = [];
            if component_names_I:
                component_names = component_names_I;
            else:
                component_names = [];
                component_names = self.get_componentNames_experimentIDAndPeakInfoParameter_dataStage01PeakInformation(experiment_id_I,parameter);
            for cn in component_names:
                print('generating boxAndWhiskersPlot for component_name ' + cn); 
                # get the data 
                data = {};
                data = self.get_row_experimentIDAndPeakInfoParameterComponentName_dataStage01PeakInformation(experiment_id_I,parameter,cn)
                if data and data['peakInfo_ave']:
                    # record data for plotting
                    data_plot_mean.append(data['peakInfo_ave']);
                    data_plot_cv.append(data['peakInfo_cv']);
                    data_plot_ci.append([data['peakInfo_lb'],data['peakInfo_ub']]);
                    data_plot_data.append(data['peakInfo_data']);
                    data_plot_parameters.append(parameter);
                    data_plot_component_names.append(data['component_group_name']);
                    data_plot_units.append('Retention_time [min]');
            # visualize the stats:
            data_plot_se = [(x[1]-x[0])/2 for x in data_plot_ci]
            filename = filename_O + '_' + experiment_id_I + '_' + parameter + figure_format_O;
            mplot.boxAndWhiskersPlot(data_plot_parameters[0],data_plot_component_names,data_plot_units[0],'samples',data_plot_data,data_plot_mean,data_plot_ci,filename_I=filename,show_plot_I=False);
    def export_boxAndWhiskersPlot_peakResolution_matplot(self,experiment_id_I,component_name_pairs_I=[],
                            peakInfo_parameter_I = ['rt_dif','resolution'],
                            filename_O = 'tmp',
                            figure_format_O = '.png'):
        '''generate a boxAndWhiskers plot from peakResolution table'''

        #TODO: remove after refactor
        mplot = matplot();

        print('export_boxAndWhiskersPlot...')
        if peakInfo_parameter_I:
            peakInfo_parameter = peakInfo_parameter_I;
        else:
            peakInfo_parameter = [];
            peakInfo_parameter = self.get_peakInfoParameter_experimentID_dataStage01PeakResolution(experiment_id_I);
        for parameter in peakInfo_parameter:
            data_plot_mean = [];
            data_plot_cv = [];
            data_plot_ci = [];
            data_plot_parameters = [];
            data_plot_component_names = [];
            data_plot_data = [];
            data_plot_units = [];
            if component_name_pairs_I:
                component_name_pairs = component_name_pairs_I;
            else:
                component_name_pairs = [];
                component_name_pairs = self.get_componentNamePairs_experimentIDAndPeakInfoParameter_dataStage01PeakResolution(experiment_id_I,parameter);
            for cn in component_name_pairs:
                # get the data 
                data = {};
                data = self.get_row_experimentIDAndPeakInfoParameterComponentName_dataStage01PeakResolution(experiment_id_I,parameter,cn)
                if data and data['peakInfo_ave']:
                    # record data for plotting
                    data_plot_mean.append(data['peakInfo_ave']);
                    data_plot_cv.append(data['peakInfo_cv']);
                    data_plot_ci.append([data['peakInfo_lb'],data['peakInfo_ub']]);
                    data_plot_data.append(data['peakInfo_data']);
                    data_plot_parameters.append(parameter);
                    data_plot_component_names.append(data['component_group_name_pair'][0]+'/'+data['component_group_name_pair'][0]);
                    data_plot_units.append('Retention_time [min]');
            # visualize the stats:
            data_plot_se = [(x[1]-x[0])/2 for x in data_plot_ci]
            filename = filename_O + '_' + experiment_id_I + '_' + parameter + figure_format_O;
            mplot.boxAndWhiskersPlot(data_plot_parameters[0],data_plot_component_names,data_plot_units[0],'samples',data_plot_data,data_plot_mean,data_plot_ci,filename_I=filename,show_plot_I=False);

            
    def export_boxAndWhiskersPlot_peakInformation_js(self,experiment_id_I,
                            peakInfo_parameter_I = ['height','retention_time','width_at_50','signal_2_noise'],
                            component_names_I=[],
                            data_dir_I='tmp'):
        '''Export data for a box and whiskers plot from peakInformation
        INPUT:
        experiment_id_I
        peakInfo_paramters_I,
        component_names_I,
        data_dir_I
        '''

        print('export_boxAndWhiskersPlot...')
        data_O = [];
        if peakInfo_parameter_I:
            peakInfo_parameter = peakInfo_parameter_I;
        else:
            peakInfo_parameter = [];
            peakInfo_parameter = self.get_peakInfoParameter_experimentID_dataStage01PeakInformation(experiment_id_I);
        for parameter in peakInfo_parameter:
            if component_names_I:
                component_names = component_names_I;
            else:
                component_names = [];
                component_names = self.get_componentNames_experimentIDAndPeakInfoParameter_dataStage01PeakInformation(experiment_id_I,parameter);
            for cn in component_names:
                print('generating boxAndWhiskersPlot for component_name ' + cn); 
                # get the data 
                row = [];
                row = self.get_row_experimentIDAndPeakInfoParameterComponentName_dataStage01PeakInformation(experiment_id_I,parameter,cn);
                if row:
                    #TODO: fix type in database 'acqusition_date_and_times'
                    tmp_list = [];
                    for d in row['acqusition_date_and_times']:
                        tmp = None;
                        tmp = self.convert_datetime2string(d);
                        tmp_list.append(tmp);
                    row['acqusition_date_and_times'] = tmp_list;
                    row['component_name'] = re.escape(row['component_name']);
                    data_O.append(row);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'component_group_name',
                    'component_name',
                    'peakInfo_parameter',
                    #'peakInfo_ave',
                    #'peakInfo_cv',
                    #'peakInfo_lb',
                    #'peakInfo_ub',
                    #'peakInfo_units',
                    'sample_names',
                    'sample_types',
                    #'acqusition_date_and_times'
                    ];
        data1_nestkeys = ['component_name'];
        data1_keymap = {'xdata':'component_name',
                        'ydata':'peakInfo_ave',
                        'ydatalb':'peakInfo_lb',
                        'ydataub':'peakInfo_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'peakInfo_parameter',
                        'featureslabel':'component_name'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"component_name",
                            "svgy1axislabel":"parameter_value",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Custom box and whiskers plot',
                               'tiletype':'svg',
                               'tileid':"tile2",
                               'rowid':"row1",
                               'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'peakInformation','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage02_isotopomer_fittedNetFluxes' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
    def export_boxAndWhiskersPlot_peakResolution_js(self,experiment_id_I,
                            component_name_pairs_I=[],
                            peakInfo_parameter_I = ['rt_dif','resolution'],
                            data_dir_I='tmp'):
        '''Export data for a box and whiskers plot'''

        print('export_boxAndWhiskersPlot...')
        data_O=[];
        if peakInfo_parameter_I:
            peakInfo_parameter = peakInfo_parameter_I;
        else:
            peakInfo_parameter = [];
            peakInfo_parameter = self.get_peakInfoParameter_experimentID_dataStage01PeakResolution(experiment_id_I);
        for parameter in peakInfo_parameter:
            if component_name_pairs_I:
                component_name_pairs = component_name_pairs_I;
            else:
                component_name_pairs = [];
                component_name_pairs = self.get_componentNamePairs_experimentIDAndPeakInfoParameter_dataStage01PeakResolution(experiment_id_I,parameter);
            for cn in component_name_pairs:
                # get the data 
                row = {};
                row = self.get_row_experimentIDAndPeakInfoParameterComponentName_dataStage01PeakResolution(experiment_id_I,parameter,cn)
                if row and row['peakInfo_ave']:
                    #TODO: fix type in database 'acqusition_date_and_times'
                    tmp_list = [];
                    for d in row['acqusition_date_and_times']:
                        tmp = None;
                        tmp = self.convert_datetime2string(d);
                        tmp_list.append(tmp);
                    row['acqusition_date_and_times'] = tmp_list;
                    data_O.append(row);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                    'component_group_name_pair',
                    'component_name_pair',
                    'peakInfo_parameter',
                    #'peakInfo_ave',
                    #'peakInfo_cv',
                    #'peakInfo_lb',
                    #'peakInfo_ub',
                    #'peakInfo_units',
                    'sample_names',
                    'sample_types',
                    #'acqusition_date_and_times'
                    ];
        data1_nestkeys = ['component_name_pair'];
        data1_keymap = {'xdata':'component_name_pair',
                        'ydata':'peakInfo_ave',
                        'ydatalb':'peakInfo_lb',
                        'ydataub':'peakInfo_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'peakInfo_parameter',
                        'featureslabel':'component_name_pair'};
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"component_name_pair","svgy1axislabel":"parameter_value",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Custom box and whiskers plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'peakResolution','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage02_isotopomer_fittedNetFluxes' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
   