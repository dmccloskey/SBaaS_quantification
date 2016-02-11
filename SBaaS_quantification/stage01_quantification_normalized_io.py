﻿#System
import json
#SBaaS
from .stage01_quantification_normalized_query import stage01_quantification_normalized_query
from ddt_python.ddt_container import ddt_container
from SBaaS_base.sbaas_template_io import sbaas_template_io
#other queries
from .stage01_quantification_MQResultsTable_query import stage01_quantification_MQResultsTable_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from python_statistics.calculate_interface import calculate_interface

class stage01_quantification_normalized_io(stage01_quantification_normalized_query,sbaas_template_io):
    def import_dataStage01Normalized_update_unique(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01Normalized_unique(data.data);
        data.clear_data();
    def import_dataStage01Normalized_update_id(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01Normalized_id(data.data,used_comment_only_I=True);
        data.clear_data();
    def export_checkCVAndExtracelluar_averages_csv(self,experiment_id_I,filename,cv_threshold_I=20,extracellular_threshold_I=50):
        '''check the CV and % Extracellular of the averages table
        INPUT:
        experiment_id_I = experiment_id
        cv_threshold_I = float, % cv tolerance
        extracellular_threshold_I = float, % extracellular threshold
        '''
        
        print('execute_checkCVAndExtracelluar_averages...')
        # query data for the view
        check = [];
        check = self.get_checkCVAndExtracellular_averages(experiment_id_I,cv_threshold_I=cv_threshold_I,extracellular_threshold_I=extracellular_threshold_I);
        ## create and populate the view
        #for n in range(len(check)):
        #    if check[n]:
        #        row = data_stage01_quantification_checkCVAndExtracellular_averages(check[n]['experiment_id'],
        #                                              check[n]['sample_name_abbreviation'],
        #                                              check[n]['component_group_name'],
        #                                              check[n]['time_point'],
        #                                              check[n]['component_name'],
        #                                              check[n]['n_replicates_broth'],
        #                                              check[n]['calculated_concentration_broth_average'],
        #                                              check[n]['calculated_concentration_broth_cv'],
        #                                              check[n]['n_replicates_filtrate'],
        #                                              check[n]['calculated_concentration_filtrate_average'],
        #                                              check[n]['calculated_concentration_filtrate_cv'],
        #                                              check[n]['n_replicates'],
        #                                              check[n]['calculated_concentration_average'],
        #                                              check[n]['calculated_concentration_cv'],
        #                                              check[n]['calculated_concentration_units'],
        #                                              check[n]['extracellular_percent'],
        #                                              check[n]['used']);
        #        self.session.add(row);
        #self.session.commit();
        if check:
            export = base_exportData(check);
            export.write_dict2csv(filename);
        else:
            print("all components are within the %CV and %Extracellular tolerance");

    def export_dataStage01Normalized_csv(self,filename,experiment_id_I=[],sample_name_I=[],
                        component_name_I=[],
                        calculated_concentration_units_I=[],
                        used__I=True):
        '''export data_stage01_quantification_normalized to csv'''
        print('export data_stage01_quantification_normalized to csv...')
        # query data for the view
        data = [];
        if experiment_id_I:
            for experiment_id in experiment_id_I:
                if experiment_id_I and sample_name_I:
                    for sample_name in sample_name_I:
                        if experiment_id_I and sample_name_I and component_name_I:
                            for component_name in component_name_I:
                                if experiment_id_I and sample_name_I and component_name_I and calculated_concentration_units_I:
                                    for ccu in calculated_concentration_units_I:
                                        data_tmp = [];
                                        data_tmp = self.get_rows_uniqueAndUsed_dataStage01QuantificationNormalized(experiment_id_I=experiment_id,
                                                sample_name_I=sample_name,
                                                component_name_I=component_name,
                                                calculated_concentration_units_I=ccu,
                                                used__I=used__I);
                                        data.extend(data_tmp)
                                else:
                                    data_tmp = [];
                                    data_tmp = self.get_rows_uniqueAndUsed_dataStage01QuantificationNormalized(experiment_id_I=experiment_id,
                                                sample_name_I=sample_name,
                                                component_name_I=component_name,
                                                calculated_concentration_units_I='%',
                                                used__I=used__I);
                                    data.extend(data_tmp);
                        else:
                            data_tmp = [];
                            data_tmp = self.get_rows_uniqueAndUsed_dataStage01QuantificationNormalized(experiment_id_I=experiment_id,
                                            sample_name_I=sample_name,
                                            component_name_I='%',
                                            calculated_concentration_units_I='%',
                                            used__I=used__I);
                            data.extend(data_tmp);
                else:
                    data_tmp = [];
                    data_tmp = self.get_rows_uniqueAndUsed_dataStage01QuantificationNormalized(experiment_id_I=experiment_id,
                                    sample_name_I='%',
                                    component_name_I='%',
                                    calculated_concentration_units_I='%',
                                    used__I=used__I);
                    data.extend(data_tmp);
        else:
            data = self.get_rows_uniqueAndUsed_dataStage01QuantificationNormalized(experiment_id_I='%',
                        sample_name_I='%',
                        component_name_I='%',
                        calculated_concentration_units_I='%',
                        used__I=True);
        if data:
            export = base_exportData(data);
            export.write_dict2csv(filename);
        else:
            print("no rows found");
    
    def export_dataStage01Averages_csv(self):
        '''export data_stage01_quantification_averages to csv'''
        pass

    def export_dataStage01NormalizedAndAverages_js(self,experiment_id_I,sample_name_abbreviations_I=[],sample_names_I=[],component_names_I=[],
                                                   cv_threshold_I=40,extracellular_threshold_I=80,
                                                   data_dir_I='tmp'):
        '''export data_stage01_quantification_normalized and averages for visualization with ddt'''

        calc = calculate_interface();
        
        print('export_dataStage01Normalized_js...')
        data_norm_broth = [];
        data_norm_filtrate = [];
        data_norm_combined = [];
        data_ave = [];
        # get sample_name_abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01Normalized(experiment_id_I);
        # create database table
        for sna in sample_name_abbreviations:
            print('exporting sample_name_abbreviation ' + sna);
            # get component names
            if component_names_I:
                component_names = component_names_I
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
            for cn in component_names:
                print('exporting component_name ' + cn);
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(experiment_id_I,cn);
                # get time points
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(experiment_id_I,sna);
                for tp in time_points:
                    print('exporting time_point ' + tp);
                    # get the averages and %CV samples
                    row = {};
                    #row = self.get_row_experimentIDAndSampleNameAbbreviationAndTimePointAndComponentName_dataStage01Averages(experiment_id_I,sna,tp,cn);
                    row = self.get_row_experimentIDAndSampleNameAbbreviationAndTimePointAndComponentNameAndCalculatedConcentrationCVAndExtracellularPercent_dataStage01Averages(experiment_id_I,
                                                                        sna,tp,cn,
                                                                        cv_threshold_I=cv_threshold_I,
                                                                        extracellular_threshold_I=extracellular_threshold_I);
                    if not row: continue;
                    stdev = calc.convert_cv2StDev(row['calculated_concentration_filtrate_average'],row['calculated_concentration_filtrate_cv']);
                    row['calculated_concentration_filtrate_lb'] = row['calculated_concentration_filtrate_average']-stdev;
                    row['calculated_concentration_filtrate_ub'] = row['calculated_concentration_filtrate_average']+stdev;
                    stdev = calc.convert_cv2StDev(row['calculated_concentration_broth_average'],row['calculated_concentration_broth_cv']);
                    row['calculated_concentration_broth_lb'] = row['calculated_concentration_broth_average']-stdev;
                    row['calculated_concentration_broth_ub'] = row['calculated_concentration_broth_average']+stdev;
                    stdev = calc.convert_cv2StDev(row['calculated_concentration_average'],row['calculated_concentration_cv']);
                    row['calculated_concentration_lb'] = row['calculated_concentration_average']-stdev;
                    row['calculated_concentration_ub'] = row['calculated_concentration_average']+stdev;
                    data_ave.append(row);
                    # get filtrate sample names
                    sample_names = [];
                    sample_description = 'Filtrate';
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(experiment_id_I,sna,sample_description,cn,tp);
                    if sample_names_I: # screen out sample names that are not in the input
                        sample_names = [x for x in sample_names if x in sample_names_I];
                    for sn in sample_names:
                        # get the row
                        row = None;
                        row = self.get_row_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if not(row): continue;
                        row['sample_name_abbreviation'] = sna;
                        data_norm_filtrate.append(row);
                        data_norm_combined.append(row);
                    # get filtrate sample names
                    sample_names = [];
                    sample_description = 'Broth';
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(experiment_id_I,sna,sample_description,cn,tp);
                    if sample_names_I: # screen out sample names that are not in the input
                        sample_names = [x for x in sample_names if x in sample_names_I];
                    for sn in sample_names:
                        # get the row
                        row = None;
                        row = self.get_row_sampleNameAndComponentName_dataStage01Normalized(sn,cn);
                        if not(row): continue;
                        row['sample_name_abbreviation'] = sna;
                        data_norm_broth.append(row);
                        data_norm_combined.append(row);
        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                      'sample_name',
                      'sample_id',
                      'sample_name_abbreviation',
                      'component_group_name',
                      'component_name',
                      'calculated_concentration_units'
                    ];
        data1_nestkeys = ['component_name'];
        data1_keymap = {'xdata':'component_name',
                        'ydata':'calculated_concentration',
                        #'ydatalb':'peakInfo_lb',
                        #'ydataub':'peakInfo_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'sample_name',
                        'featureslabel':'component_name'};
        data2_keys = ['experiment_id',
                      'sample_name_abbreviation',
                      'time_point',
                      'component_group_name',
                      'component_name',
                      'calculated_concentration_units',
                      'extracellular_percent',
                      'calculated_concentration_broth_cv'
                    ];
        data2_nestkeys = ['component_name'];
        data2_keymap = {'xdata':'component_name',
                        'ydata':'calculated_concentration_broth_average',
                        'ydatalb':'calculated_concentration_broth_lb',
                        'ydataub':'calculated_concentration_broth_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'sample_name_abbreviation',
                        'featureslabel':'component_name'};
        data3_keys = ['experiment_id',
                      'sample_name_abbreviation',
                      'time_point',
                      'component_group_name',
                      'component_name',
                      'calculated_concentration_units',
                      'extracellular_percent',
                      'calculated_concentration_filtrate_cv'
                    ];
        data3_nestkeys = ['component_name'];
        data3_keymap = {'xdata':'component_name',
                        'ydata':'calculated_concentration_filtrate_average',
                        'ydatalb':'calculated_concentration_filtrate_lb',
                        'ydataub':'calculated_concentration_filtrate_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'sample_name_abbreviation',
                        'featureslabel':'component_name'};
        data4_keys = ['experiment_id',
                      'sample_name_abbreviation',
                      'time_point',
                      'component_group_name',
                      'component_name',
                      'calculated_concentration_units',
                      'extracellular_percent',
                      'calculated_concentration_cv'
                    ];
        data4_nestkeys = ['component_name'];
        data4_keymap = {'xdata':'component_name',
                        'ydata':'calculated_concentration_average',
                        'ydatalb':'calculated_concentration_lb',
                        'ydataub':'calculated_concentration_ub',
                        #'ydatamin':None,
                        #'ydatamax':None,
                        #'ydataiq1':None,
                        #'ydataiq3':None,
                        #'ydatamedian':None,
                        'serieslabel':'sample_name_abbreviation',
                        'featureslabel':'component_name'};
        # make the data object
        dataobject_O = [{"data":data_norm_broth,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data_norm_filtrate,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data_norm_combined,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data_ave,"datakeys":data2_keys,"datanestkeys":data2_nestkeys},
                        {"data":data_ave,"datakeys":data3_keys,"datanestkeys":data3_nestkeys},
                        {"data":data_ave,"datakeys":data4_keys,"datanestkeys":data4_nestkeys}];
        # make the tile parameter objects for the normalized and averages
        formtileparameters_normalized_O = {'tileheader':'Filter menu normalized','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters_normalized_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_normalized_O.update(formparameters_normalized_O);
        formtileparameters_averages_O = {'tileheader':'Filter menu averages','tiletype':'html','tileid':"filtermenu2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters_averages_O = {'htmlid':'filtermenuform2',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit2','text':'submit'},"formresetbuttonidtext":{'id':'reset2','text':'reset'},"formupdatebuttonidtext":{'id':'update2','text':'update'}};
        formtileparameters_averages_O.update(formparameters_averages_O);
        # make the svg objects for the normalized data
        svgparameters_broth_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":250,"svgheight":250,
                            "svgx1axislabel":"component_name","svgy1axislabel":"concentration",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_broth_O = {'tileheader':'Broth data','tiletype':'svg','tileid':"tile1",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        svgtileparameters_broth_O.update(svgparameters_broth_O);
        svgparameters_filtrate_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg2',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":250,"svgheight":250,
                            "svgx1axislabel":"component_name","svgy1axislabel":"concentration",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_filtrate_O = {'tileheader':'Filtrate data','tiletype':'svg','tileid':"tile2",'rowid':"row2",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        svgtileparameters_filtrate_O.update(svgparameters_filtrate_O);
        svgparameters_combined_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap],
                            'svgid':'svg3',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":250,"svgheight":250,
                            "svgx1axislabel":"component_name","svgy1axislabel":"concentration",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_combined_O = {'tileheader':'Broth-Filtrate data','tiletype':'svg','tileid':"tile3",'rowid':"row2",'colid':"col3",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        svgtileparameters_combined_O.update(svgparameters_combined_O);
        # make the svg objects for the averages data
        svgparameters_averages_broth_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data2_keymap],
                            'svgid':'svg4',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":250,"svgheight":250,
                            "svgx1axislabel":"component_name","svgy1axislabel":"concentration",
    						'svgformtileid':'filtermenu2','svgresetbuttonid':'reset2','svgsubmitbuttonid':'submit2'};
        svgtileparameters_averages_broth_O = {'tileheader':'Broth data','tiletype':'svg','tileid':"tile4",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        svgtileparameters_averages_broth_O.update(svgparameters_averages_broth_O);
        svgparameters_averages_filtrate_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data3_keymap],
                            'svgid':'svg5',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":250,"svgheight":250,
                            "svgx1axislabel":"component_name","svgy1axislabel":"concentration",
    						'svgformtileid':'filtermenu2','svgresetbuttonid':'reset2','svgsubmitbuttonid':'submit2'};
        svgtileparameters_averages_filtrate_O = {'tileheader':'Filtrate data','tiletype':'svg','tileid':"tile5",'rowid':"row3",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        svgtileparameters_averages_filtrate_O.update(svgparameters_averages_filtrate_O);
        svgparameters_averages_combined_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data4_keymap],
                            'svgid':'svg6',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":250,"svgheight":250,
                            "svgx1axislabel":"component_name","svgy1axislabel":"concentration",
    						'svgformtileid':'filtermenu2','svgresetbuttonid':'reset2','svgsubmitbuttonid':'submit2'};
        svgtileparameters_averages_combined_O = {'tileheader':'Broth-Filtrate data','tiletype':'svg','tileid':"tile6",'rowid':"row3",'colid':"col3",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        svgtileparameters_averages_combined_O.update(svgparameters_averages_combined_O);
        # make the tables for the normalized and averages data
        tableparameters_normalized_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_normalized_O = {'tileheader':'normalized data','tiletype':'table','tileid':"tile7",'rowid':"row4",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_normalized_O.update(tableparameters_normalized_O);
        tableparameters_averages_O = {"tabletype":'responsivetable_01',
                    'tableid':'table2',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu2','tableresetbuttonid':'reset2','tablesubmitbuttonid':'submit2'};
        tabletileparameters_averages_O = {'tileheader':'averages data','tiletype':'table','tileid':"tile8",'rowid':"row5",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_averages_O.update(tableparameters_averages_O);
        parametersobject_O = [formtileparameters_normalized_O,
                              formtileparameters_averages_O,
                              svgtileparameters_broth_O,
                              svgtileparameters_filtrate_O,
                              svgtileparameters_combined_O,
                              svgtileparameters_averages_broth_O,
                              svgtileparameters_averages_filtrate_O,
                              svgtileparameters_averages_combined_O,
                              tabletileparameters_normalized_O,
                              tabletileparameters_averages_O];
        tile2datamap_O = {"filtermenu1":[2],"filtermenu2":[5],
                          "tile1":[0],"tile2":[1],"tile3":[2],
                          "tile4":[3],"tile5":[4],"tile6":[5],
                          "tile7":[2],"tile8":[5]};
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
        #
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = filtermenuobject_O);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            #data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            #file.write(data_str);
            #file.write(parameters_str);
            #file.write(tile2datamap_str);
            file.write(ddtutilities.get_allObjects());