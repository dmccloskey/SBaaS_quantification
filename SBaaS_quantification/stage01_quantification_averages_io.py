# System
import json
# SBaaS
from .stage01_quantification_averages_query import stage01_quantification_averages_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from SBaaS_base.sbaas_template_io import sbaas_template_io

class stage01_quantification_averages_io(stage01_quantification_averages_query,sbaas_template_io):

    def export_dataStage01AveragesMI_json(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, filename_I):
        '''export dataStage01AveragesMI to json file'''
        # query the data
        data = {};
        data = self.get_concentrations_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01AveragesMI(experiment_id_I, sample_name_abbreviation_I, time_point_I);
        # write json to file
        with open(filename_I, 'w') as outfile:
                json.dump(data, outfile, indent=4);

    def export_dataStage01AveragesMIgeo_json(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, filename_I):
        '''export dataStage01AveragesMI to json file'''
        # query the data
        data = {};
        data = self.get_concentrations_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01AveragesMIgeo(experiment_id_I, sample_name_abbreviation_I, time_point_I);
        # write json to file
        with open(filename_I, 'w') as outfile:
                json.dump(data, outfile, indent=4);
   