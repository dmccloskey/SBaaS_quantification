import json
import re

from .lims_quantitationMethod_postgresql_models import *
#from .lims_msMethod_query import lims_msMethod_query
from SBaaS_LIMS.lims_calibratorsAndMixes_query import lims_calibratorsAndMixes_query
from SBaaS_LIMS.lims_sample_query import lims_sample_query
from .lims_quantitationMethod_query import lims_quantitationMethod_query
from .stage01_quantification_MQResultsTable_query import stage01_quantification_MQResultsTable_query

# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from SBaaS_base.sbaas_template_io import sbaas_template_io

class lims_quantitationMethod_io(lims_quantitationMethod_query,
                                 stage01_quantification_MQResultsTable_query,
                                 lims_calibratorsAndMixes_query,
                                #lims_msMethod_query,
                                lims_sample_query,
                                sbaas_template_io
                                ):
        
    def export_calibrationConcentrations(self, data, filename):
        '''export calibration curve concentrations'''

        # write calibration curve concentrations to file
        export = base_exportData(data);
        export.write_dict2csv(filename);

    def import_quantitationMethod_add(self,QMethod_id_I, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_quantitationMethod(QMethod_id_I, data.data);
        data.clear_data();

    def export_quantitationMethod_js(self,QMethod_id_I,component_names_I=[],data_dir_I='tmp'):
        '''Export the quantitation and calibrators to ddt'''
        #get the calibrator data
        data_1 = [];
        data_2 = [];
        data_1a = [];
        # get the sample names that were used to generate the calibration curve:
        if component_names_I:
            component_names = component_names_I;
        else:
            component_names = [];
            component_names = self.get_components(QMethod_id_I);
        for cn in component_names:
            # get the quant method parameters for each component
            fit,weighting,use_area = self.get_quantMethodParameters(QMethod_id_I,cn);
            # get the sample names for that component
            sample_names = [];
            sample_names = self.get_sampleNames_QMethodIDAndComponentNameAndSampleType(QMethod_id_I,cn,sample_type_I='Standard');
            if not sample_names: continue;
            concentrations = []
            ratios = [];
            for sn in sample_names:
                # get the quant method rows
                row = {};
                row = self.get_row_sampleNameAndComponentName(sn,cn);
                if row and not row is None and not row['concentration_ratio'] is None:
                    if use_area: row['ratio'] = row['area_ratio'];
                    else: row['ratio'] = row['height_ratio'];
                    row['acquisition_date_and_time'] = self.convert_datetime2string(row['acquisition_date_and_time'])
                    row['component_name'] = re.escape(row['component_name']);
                    data_1.append(row);
                    concentrations.append(row['concentration_ratio']);
                    ratios.append(row['ratio']);
            if not concentrations: continue;
            # get the quant method statistics
            row = {};
            row = self.get_row_QMethodIDAndComponentNamequantitationMethod(QMethod_id_I,cn);
            if row:
                row['component_name'] = re.escape(row['component_name']);
                data_2.append(row);
                # generate the line of best fit
                min_ratio = min(ratios);
                max_ratio = max(ratios);
                index_min = [cnt for cnt,x in enumerate(ratios) if x == min_ratio][0];
                index_max = [cnt for cnt,x in enumerate(ratios) if x == max_ratio][0];
                conc_min = min(concentrations);
                conc_max = max(concentrations);
                sample_name_min = sample_names[index_min];
                sample_name_max = sample_names[index_max];
                data_1a.append({'concentration_ratio':row['lloq'],
                        'ratio':min_ratio,
                        'component_name':re.escape(cn),
                        'sample_name':sample_name_min});
                data_1a.append({'concentration_ratio':row['uloq'],
                        'ratio':max_ratio,
                        'component_name':re.escape(cn),
                        'sample_name':sample_name_max});
                
        # dump chart parameters to a js files
        data1_keys = [
                    'concentration_ratio',
                    'sample_name',
                    'component_name',
                    'ratio',
                    ];
        data1_nestkeys = ['component_name'];
        data1_keymap = {'xdata':'concentration_ratio',
                        'ydata':'ratio',
                        'serieslabel':'component_name',
                        'featureslabel':'sample_name'};
        data2_keys = ['id'
                    'q1_mass',
                    'q3_mass',
                    'met_id',
                    'component_name',
                    'is_name',
                    'fit',
                    'weighting',
                    'intercept',
                    'slope',
                    'correlation',
                    'use_area',
                    'lloq',
                    'uloq',
                    'points',
                    ];
        data2_nestkeys = ['component_name'];
        data2_keymap = {'xdata':'concentration_ratio',
                        'ydata':'ratio',
                        'serieslabel':'component_name',
                        'featureslabel':None};
        parameters = {"chart1margin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                    "chart1width":500,"chart1height":350,
                  "chart1title":"Metric Plot", "chart1x1axislabel":"sample_name","chart1y1axislabel":"measurement"}
        # make the data object
        dataobject_O = [{"data":data_1,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data_1a,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":data_2,"datakeys":data2_keys,"datanestkeys":data2_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-4"};
        formparameters_O = {'htmlid':'filtermenuform1','htmltype':'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'scatterlineplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                            "svgwidth":500,"svgheight":350,
                            "svgx1axislabel":"concentration_ratio","svgy1axislabel":"measurement_ratio",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'Regression','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-8"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'Regression Statistics','tiletype':'table','tileid':"tile3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0,1],"tile3":[2]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage01_resequencing_mutationsAnnotated' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);