# System
import json
# SBaaS
from .stage01_quantification_outliers_query import stage01_quantification_outliers_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from SBaaS_base.sbaas_template_io import sbaas_template_io

class stage01_quantification_outliers_io(stage01_quantification_outliers_query,
                                                   sbaas_template_io):
    def export_data_stage01_quantification_outliersDeviation_replicates_csv(self, analysis_id_I, filename_O,
                        experiment_id_I='%',
                        sample_name_short_I='%',
                        time_point_I='%',
                        component_name_I='%',
                        calculated_concentration_units_I='%'):
        '''export data_stage01_quantification_outliers to .csv'''

        data = [];
        data = self.get_rows_unique_dataStage01QuantificationOutliersDeviationReplicates(analysis_id_I,
                        experiment_id_I,
                        sample_name_short_I,
                        time_point_I,
                        component_name_I,
                        calculated_concentration_units_I);
        if data:
            # write data to file
            export = base_exportData(data);
            export.write_dict2csv(filename_O);
   