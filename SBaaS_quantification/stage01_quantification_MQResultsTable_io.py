#system
import json
#SBaaS
from .stage01_quantification_MQResultsTable_query import stage01_quantification_MQResultsTable_query
#from .stage01_quantification_analysis_query import stage01_quantification_analysis_query
from ddt_python.ddt_container import ddt_container
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from quantification_analysis.MQResultsTable import MQResultsTable
from ddt_python.ddt_container_filterMenuAndChart2dAndTable import ddt_container_filterMenuAndChart2dAndTable
import copy

class stage01_quantification_MQResultsTable_io(stage01_quantification_MQResultsTable_query,
                                               sbaas_template_io):

    def import_dataStage01MQResultsTable_add(self,filename):
        '''table adds'''
        ##OPTION1:
        #data = base_importData();
        #data.read_csv(filename);
        #data.format_data();
        #self.add_dataStage01MQResultsTable(data.data);
        #data.clear_data();
        #OPTION2: 
        resultstable = MQResultsTable();
        resultstable.import_resultsTable(filename);
        self.add_dataStage01MQResultsTable(resultstable.resultsTable);
    
    def import_dataStage01MQResultsTable_update(self,filename):
        '''table updates'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01MQResultsTable(data.data);
        data.clear_data();

    def export_dataStage01MQResultsTable_csv(self):
        pass;

    def export_dataStage01MQResultsTable_metricPlot_js(self,experiment_id_I,sample_names_I=[],component_names_I=[],measurement_I='calculated_concentration',data_dir_I="tmp"):
        ''' export a metric plot
        INPUT:
        experiment_id_I = experiment_id
        sample_names_I = sample_names
        component_names_I = component names
        measurement_I = measurement to plot, supports calculated_concentration, height_ratio, area_ratio, height, area, rt'''

        # get the data:
        data_O = [];
        cnt = 0;
        #Query unique sample_name/component_name for the analysis
        # get sample names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            sample_types = ['Quality Control','Unknown','Standard','Blank'];
            for st in sample_types:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
        # create database table
        for sn in sample_names:
            # get component names
            if component_names_I:
                component_names = component_names_I;
            else:
                component_names = [];
                component_names = self.get_componentsNames_experimentIDAndSampleName(experiment_id_I,sn);
            for cn in component_names:
                # get the row
                rows = {};
                rows = self.get_row_sampleNameAndComponentName(sn,cn);
                if rows:
                    rows['acquisition_date_and_time'] = self.convert_datetime2string(rows['acquisition_date_and_time'])
                    rows['index_'] = cnt;
                    rows['experiment_id']=experiment_id_I;
                    data_O.append(rows);
                    cnt+=1;
        # get the sample_names_I    
        # dump chart parameters to a js files
        data1_keys = [
                    'experiment_id',
                    'sample_name',
                    'component_name',
                    measurement_I,
                    'acquisition_date_and_time',
                    'sample_type',
                    ];
        data1_nestkeys = ['component_name'];
        data1_keymap = {'xdata':'index_',
                        'ydata':measurement_I,
                        'serieslabel':'component_name',
                        'featureslabel':'sample_name'};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Metric Plot", "chart1x1axislabel":"sample_name","chart1y1axislabel":"measurement"}
        # make the data object
        dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"sample_name","svgy1axislabel":"measurement_value",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Metric Plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Metric plot','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,1],"tile3":[0]};
        # dump the data to a json file
        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
    def export_dataStage01MQResultsTable_js(
            self,analysis_id_I,
            features_I=[
                'calculated_concentration',
                'height_ratio',
                'retention_time'],
            include_IS_I=False,
            data_dir_I="tmp"):
        ''' export a metric plot
        INPUT:
        experiment_id_I = experiment_id
        sample_names_I = sample_names
        component_names_I = component names
        features_I = features to plot,
            supports calculated_concentration, height_ratio,
            area_ratio, height, area, retention_time
        '''

        #quantification_analysis_query = stage01_quantification_analysis_query(self.session,self.engine,self.settings)

        # get the data:
        data_O = [];
        data_dict_O = {};
        data_tmp = [];
        data_tmp = self.getRowsJoin_analysisID_dataStage01QuantificationMQResultsTable(analysis_id_I);
        # make a unique index for each component
        component_names = list(set([d['component_name'] for d in data_tmp]));
        component_names_dict = {d:0 for d in component_names};
        for d in data_tmp:
            tmp = {};
            tmp['acquisition_date_and_time'] = self.convert_datetime2string(d['acquisition_date_and_time'])
            tmp['sample_name'] = d['sample_name'];
            tmp['sample_type'] = d['sample_type'];
            #tmp['experiment_id'] = d['experiment_id'];
            #tmp['analysis_id'] = d['analysis_id'];
            tmp['analysis_id']=analysis_id_I;
            tmp['component_name'] = d['component_name'];
            tmp['component_group_name'] = d['component_group_name'];
            tmp['component_index'] = component_names_dict[d['component_name']];
            for m in features_I:
                if not m in data_dict_O: data_dict_O[m]=[];
                if m in d.keys() and not d[m] is None:
                    tmp1 = copy.copy(tmp);
                    tmp1['feature_name'] = m;
                    tmp1['feature_value'] = d[m];
                    data_dict_O[m].append(tmp1);
                    data_O.append(tmp1);
            component_names_dict[d['component_name']]+=1;
        # dump chart parameters to a js files
        data1_keys = [
                    'analysis_id',
                    'sample_name',
                    'component_name',
                    'feature_name',
                    'acquisition_date_and_time',
                    'sample_type',
                    ];
        data1_nestkeys = ['component_name'];
        data1_keymap = {'xdata':'component_index',
                        'ydata':'feature_value',
                        'serieslabel':'component_name',
                        'featureslabel':'sample_name'};
        svgkeymap1 = [[data1_keymap,data1_keymap] for k in data_dict_O.keys()]
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Metric Plot", "chart1x1axislabel":"sample_name","chart1y1axislabel":"measurement"}
        ## make the data object
        #dataobject_O = [{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},{"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        ## make the tile parameter objects
        #formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
        #    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        #formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        #formtileparameters_O.update(formparameters_O);
        #svgparameters_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
        #                    'svgid':'svg1',
        #                    "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
        #                    "svgwidth":500,"svgheight":350,
        #                    "svgx1axislabel":"sample_name","svgy1axislabel":"measurement_value",
        #		'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        #svgtileparameters_O = {'tileheader':'Metric Plot','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
        #    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        #svgtileparameters_O.update(svgparameters_O);
        #tableparameters_O = {"tabletype":'responsivetable_01',
        #            'tableid':'table1',
        #            "tablefilters":None,
        #            "tableclass":"table  table-condensed table-hover",
        #   'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        #tabletileparameters_O = {'tileheader':'Metric plot','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
        #    'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        #tabletileparameters_O.update(tableparameters_O);
        #parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        #tile2datamap_O = {"filtermenu1":[0],"tile2":[0,1],"tile3":[0]};
        ## dump the data to a json file
        #ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = None);
        #if data_dir_I=='tmp':
        #    filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        #elif data_dir_I=='data_json':
        #    data_json_O = ddtutilities.get_allObjects_js();
        #    return data_json_O;
        #with open(filename_str,'w') as file:
        #    file.write(ddtutilities.get_allObjects());
        
        nsvgtable = ddt_container_filterMenuAndChart2dAndTable();
        nsvgtable.make_filterMenuAndChart2dAndTable(
                data_filtermenu=data_O,
                data_filtermenu_keys=data1_keys,
                data_filtermenu_nestkeys=data1_nestkeys,
                data_filtermenu_keymap=data1_keymap,
                data_svg_keys=None,
                data_svg_nestkeys=None,
                data_svg_keymap=None,
                data_table_keys=None,
                data_table_nestkeys=None,
                data_table_keymap=None,
                data_svg=data_dict_O,
                data_table=None,
                #svgtype='scatterlineplot2d_01',
                svgtype='scatterplot2d_01',
                tabletype='responsivetable_01',
                svgx1axislabel='',
                svgy1axislabel='',
                tablekeymap = [data1_keymap],
                svgkeymap = [], #calculated on the fly
                formtile2datamap=[0],
                tabletile2datamap=[0],
                svgtile2datamap=[], #calculated on the fly
                svgfilters=None,
                svgtileheader='Metric Plot',
                tablefilters=None,
                tableheaders=None,
                svgparameters_I = parameters
                );

        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = nsvgtable.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(nsvgtable.get_allObjects());