#system
import json
from .stage01_quantification_physiologicalRatios_query import stage01_quantification_physiologicalRatios_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from matplotlib_utilities.matplot import matplot
from SBaaS_base.sbaas_template_io import sbaas_template_io

class stage01_quantification_physiologicalRatios_io(stage01_quantification_physiologicalRatios_query,sbaas_template_io):
    def export_boxAndWhiskersPlot_physiologicalRatios_matplot(self,experiment_id_I,sample_name_abbreviations_I=[],ratio_ids_I=[]):
        '''generate a boxAndWhiskers plot from physiological ratios table'''
        mplot = matplot();
        print('execute_boxAndWhiskersPlot...')
        # get time points
        time_points = [];
        time_points = self.get_timePoint_experimentID_dataStage01PhysiologicalRatiosAverages(experiment_id_I);
        for tp in time_points:
            print('generating boxAndWhiskersPlot for time_point ' + tp);
            if ratio_ids_I:
                ratio_ids = ratio_ids_I;
            else:
                ratio_ids = list(self.ratios.keys());
            for k in ratio_ids:
            #for k,v in self.ratios.iteritems():
                print('generating boxAndWhiskersPlot for ratio ' + k); # get sample_name_abbreviations
                data_plot_mean = [];
                data_plot_var = [];
                data_plot_ci = [];
                data_plot_sna = [];
                data_plot_ratio_ids = [];
                data_plot_data = [];
                data_plot_ratio_units = [];
                if sample_name_abbreviations_I:
                    sample_name_abbreviations = sample_name_abbreviations_I;
                else:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndTimePointAndRatioID_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k);
                for sna in sample_name_abbreviations:
                    print('generating boxAndWhiskersPlot for sample_name_abbreviation ' + sna);
                    # get the data 
                    data = {};
                    data = self.get_data_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k,sna)
                    ratio_values = [];
                    ratio_values = self.get_ratios_experimentIDAndSampleNameAbbreviationAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sna,tp,k)
                    # record data for plotting
                    data_plot_mean.append(data['physiologicalratio_value_ave']);
                    data_plot_var.append(data['physiologicalratio_value_cv']);
                    data_plot_ci.append([data['physiologicalratio_value_lb'],data['physiologicalratio_value_ub']]);
                    data_plot_data.append(ratio_values);
                    data_plot_sna.append(sna);
                    data_plot_ratio_ids.append(k);
                    data_plot_ratio_units.append('');
                # visualize the stats:
                #self.matplot.barPlot(data_plot_ratio_ids[0],data_plot_sna,data_plot_sna[0],'samples',data_plot_mean,data_plot_var);
                mplot.boxAndWhiskersPlot(data_plot_ratio_ids[0],data_plot_sna,data_plot_ratio_units[0],'samples',data_plot_data,data_plot_mean,data_plot_ci);
    def export_scatterLinePlot_physiologicalRatios_matplot(self,experiment_id_I,sample_name_abbreviations_I=[],ratio_ids_I=[]):
        '''Generate a scatter line plot for physiological ratios averages'''
        
        
        mplot = matplot();
        print('Generating scatterLinePlot for physiologicalRatios')
        # get time points
        time_points = [];
        time_points = self.get_timePoint_experimentID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I);
        for tp in time_points:
            print('Generating scatterLinePlot for physiologicalRatios for time_point ' + tp);
            # get physiological ratio_ids
            ratios = {};
            ratios = self.get_ratioIDs_experimentIDAndTimePoint_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,tp);
            for k,v in ratios.items():
                if ratio_ids_I: 
                    if not k in ratio_ids_I:
                        continue;
                print('Generating scatterLinePlot for physiologicalRatios for ratio ' + k);
                # get sample_names
                if sample_name_abbreviations_I:
                    sample_name_abbreviations = sample_name_abbreviations_I;
                else:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndTimePointAndRatioID_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k);
                ratios_num = [];
                ratios_den = [];
                for sna_cnt,sna in enumerate(sample_name_abbreviations):
                    print('Generating scatterLinePlot for physiologicalRatios for sample name abbreviation ' + sna);
                    # get ratios_numerator
                    ratio_num = None;
                    ratio_num = self.get_ratio_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k+'_numerator',sna)
                    if not ratio_num: continue;
                    ratios_num.append(ratio_num);
                    # get ratios_denominator
                    ratio_den = None;
                    ratio_den = self.get_ratio_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k+'_denominator',sna)
                    if not ratio_den: continue;
                    ratios_den.append(ratio_den);
                # plot the data
                mplot.scatterLinePlot(k,k+'_denominator',k+'_numerator',ratios_den,ratios_num,sample_name_abbreviations);

    def export_dataStage01QuantificationPhysiologicalRatios_js(self,experiment_id_I,sample_name_abbreviations_I=[],ratio_ids_I=[],
                                                               data_dir_I = 'tmp'):
        '''Export the data from data_stage01_phyisiogicalRatios for visualization with DDT'''
        print('Generating scatterLinePlot for physiologicalRatios')
        data_replicates = [];
        data_averages = [];
        data_numAndDen = [];
        # get time points
        time_points = [];
        time_points = self.get_timePoint_experimentID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I);
        for tp in time_points:
            print('Generating scatterLinePlot for physiologicalRatios for time_point ' + tp);
            # get physiological ratio_ids
            ratios = {};
            ratios = self.get_ratioIDs_experimentIDAndTimePoint_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,tp);
            for k,v in ratios.items():
                if ratio_ids_I: 
                    if not k in ratio_ids_I:
                        continue;
                print('Generating scatterLinePlot for physiologicalRatios for ratio ' + k);
                # get sample_names
                if sample_name_abbreviations_I:
                    sample_name_abbreviations = sample_name_abbreviations_I;
                else:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndTimePointAndRatioID_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k);
                ratios_num = [];
                ratios_den = [];
                for sna_cnt,sna in enumerate(sample_name_abbreviations):
                    print('Generating scatterLinePlot for physiologicalRatios for sample name abbreviation ' + sna);
                    # get the data 
                    data = {};
                    data = self.get_data_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k,sna)
                    if not data: continue;
                    data_averages.append(data);
                    # get the replicates
                    ratio_values = [];
                    ratio_values = self.get_rows_experimentIDAndSampleNameAbbreviationAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sna,tp,k);
                    for ratio in ratio_values:
                        ratio['sample_name_abbreviation']=sna;
                    data_replicates.extend(ratio_values);
                    ratio_values = [];
                    ratio_values = self.get_rows_experimentIDAndSampleNameAbbreviationAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sna,tp,k+'_numerator');
                    for ratio in ratio_values:
                        ratio['sample_name_abbreviation']=sna;
                    data_replicates.extend(ratio_values);
                    ratio_values = [];
                    ratio_values = self.get_rows_experimentIDAndSampleNameAbbreviationAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(experiment_id_I,sna,tp,k+'_denominator');
                    for ratio in ratio_values:
                        ratio['sample_name_abbreviation']=sna;
                    data_replicates.extend(ratio_values);
                    # get ratios_numerator
                    ratio_num = None;
                    ratio_num = self.get_data_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k+'_numerator',sna)
                    if not ratio_num: continue;
                    # get ratios_denominator
                    ratio_den = None;
                    ratio_den = self.get_data_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(experiment_id_I,tp,k+'_denominator',sna)
                    if not ratio_den: continue;
                    # modify
                    ratio = {};
                    if ratio_num['sample_name_abbreviation']==ratio_den['sample_name_abbreviation']:
                        ratio = {'experiment_id':ratio_num['experiment_id'],
                                'sample_name_abbreviation':ratio_num['sample_name_abbreviation'],
                                'time_point':ratio_num['time_point'],
                                'physiologicalratio_name':ratio_num['physiologicalratio_name'],
                                'physiologicalratio_description':ratio_num['physiologicalratio_description']}
                        ratio['physiologicalratio_id'] = ratio_num['physiologicalratio_id'].replace('_numerator','');
                        ratio['physiologicalratio_value_numerator'] = ratio_num['physiologicalratio_value_ave'];
                        ratio['physiologicalratio_value_denominator'] = ratio_den['physiologicalratio_value_ave'];
                    else:
                        print('physiologicalratio sample_name_shorts do not match');
                    data_numAndDen.append(ratio);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                      'sample_name_abbreviation',
                      'sample_name_short',
                      'time_point',
                      'physiologicalratio_id',
                      'physiologicalratio_name',
                      'physiologicalratio_description',
                    ];
        data1_nestkeys = ['physiologicalratio_id'];
        data1_keymap = {'xdata':'physiologicalratio_id',
                        'ydata':'physiologicalratio_value',
                        #'ydatalb':'physiologicalratio_value_lb',
                        #'ydataub':'physiologicalratio_value_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'sample_name_short',
                        'featureslabel':'physiologicalratio_id'};
        data2_keys = ['experiment_id',
                      'sample_name_abbreviation',
                      'time_point',
                      'physiologicalratio_id',
                      'physiologicalratio_name',
                      'physiologicalratio_description',
                      'physiologicalratio_cv'
                    ];
        data2_nestkeys = ['physiologicalratio_id'];
        data2_keymap = {'xdata':'physiologicalratio_id',
                        'ydata':'physiologicalratio_value_ave',
                        'ydatalb':'physiologicalratio_value_lb',
                        'ydataub':'physiologicalratio_value_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'sample_name_abbreviation',
                        'featureslabel':'physiologicalratio_id'};
        data3_keys = [
                    'experiment_id',
                      'sample_name_abbreviation',
                      'time_point',
                      'physiologicalratio_id',
                      'physiologicalratio_name',
                      'physiologicalratio_description'
                    ];
        data3_nestkeys = ['physiologicalratio_id'];
        data3_keymap = {'xdata':'physiologicalratio_value_denominator',
                        'ydata':'physiologicalratio_value_numerator',
                        'serieslabel':'physiologicalratio_id',
                        'featureslabel':'sample_name_abbreviation'};
        # make the data object
        dataobject_O = [{"data":data_replicates,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data_averages,"datakeys":data2_keys,"datanestkeys":data2_nestkeys},
                        {"data":data_numAndDen,"datakeys":data3_keys,"datanestkeys":data3_nestkeys}];
        # make the tile parameter objects for the replicates and averages
        formtileparameters_replicates_O = {'tileheader':'Filter menu replicates','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters_replicates_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_replicates_O.update(formparameters_replicates_O);
        formtileparameters_averages_O = {'tileheader':'Filter menu averages','tiletype':'html','tileid':"filtermenu2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters_averages_O = {'htmlid':'filtermenuform2',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit2','text':'submit'},"formresetbuttonidtext":{'id':'reset2','text':'reset'},"formupdatebuttonidtext":{'id':'update2','text':'update'}};
        formtileparameters_averages_O.update(formparameters_averages_O);
        # make the svg objects for the replicates data
        svgparameters_replicates_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"physiologicalratio_id","svgy1axislabel":"value",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_replicates_O = {'tileheader':'Replicates','tiletype':'svg','tileid':"tile1",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_replicates_O.update(svgparameters_replicates_O);
        # make the svg objects for the box and whiskers data
        svgparameters_boxAndWhiskers_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data2_keymap],
                            'svgid':'svg2',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":350,"svgheight":350,
                            "svgx1axislabel":"physiologicalratio_id","svgy1axislabel":"value",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_boxAndWhiskers_O = {'tileheader':'Ratio','tiletype':'svg','tileid':"tile2",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_boxAndWhiskers_O.update(svgparameters_boxAndWhiskers_O);
        # make the svg objects for the scatter line plot data
        svgparameters_scatterLinePlot_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data3_keymap,data3_keymap],
                            'svgid':'svg3',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":350,"svgheight":350,
                            "svgx1axislabel":"physiologicalratio_denominator","svgy1axislabel":"physiologicalratio_numerator",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_scatterLinePlot_O = {'tileheader':'Ratio numerator vs. denominator','tiletype':'svg','tileid':"tile3",'rowid':"row4",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_scatterLinePlot_O.update(svgparameters_scatterLinePlot_O);
        # make the tables for the replicates and averages data
        tableparameters_replicates_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_replicates_O = {'tileheader':'replicates data','tiletype':'table','tileid':"tile7",'rowid':"row5",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_replicates_O.update(tableparameters_replicates_O);
        tableparameters_averages_O = {"tabletype":'responsivetable_01',
                    'tableid':'table2',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu2','tableresetbuttonid':'reset2','tablesubmitbuttonid':'submit2'};
        tabletileparameters_averages_O = {'tileheader':'averages data','tiletype':'table','tileid':"tile8",'rowid':"row6",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_averages_O.update(tableparameters_averages_O);
        parametersobject_O = [formtileparameters_replicates_O,
                              formtileparameters_averages_O,
                              svgtileparameters_replicates_O,
                              svgtileparameters_boxAndWhiskers_O,
                              svgtileparameters_scatterLinePlot_O,
                              tabletileparameters_replicates_O,
                              tabletileparameters_averages_O];
        tile2datamap_O = {"filtermenu1":[0],"filtermenu2":[1],
                          "tile1":[0],"tile2":[1],"tile3":[2,2],
                          "tile7":[0],"tile8":[1]};
        filtermenuobject_O = [{"filtermenuid":"filtermenu1","filtermenuhtmlid":"filtermenuform1",
                "filtermenusubmitbuttonid":"submit1","filtermenuresetbuttonid":"reset1",
                "filtermenuupdatebuttonid":"update1"},{"filtermenuid":"filtermenu2","filtermenuhtmlid":"filtermenuform2",
                "filtermenusubmitbuttonid":"submit2","filtermenuresetbuttonid":"reset2",
                "filtermenuupdatebuttonid":"update2"}
                              ];
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        filtermenu_str = 'var ' + 'filtermenu' + ' = ' + json.dumps(filtermenuobject_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_quantification_physiologicalRatios' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
            file.write(filtermenu_str);
   