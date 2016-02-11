from .stage01_quantification_replicates_query import stage01_quantification_replicates_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from SBaaS_base.sbaas_template_io import sbaas_template_io

class stage01_quantification_replicates_io(stage01_quantification_replicates_query,sbaas_template_io):
    
    def export_dataStage01Replicates_csv(self, experiment_id_I, filename):
        '''export dataStage01Replicates to csv file'''
        # query the data
        data = [];
        data = self.get_data_experimentID_dataStage01Replicates(experiment_id_I);
        # expand the data file:
        sns = []
        cgn = []
        for d in data:
             sns.append(d['sample_name_short']);
             cgn.append(d['component_group_name']);
        sns_sorted = sorted(set(sns))
        cgn_sorted = sorted(set(cgn))
        concentrations = []
        for c in cgn_sorted:
             row = ['NA' for r in range(len(sns_sorted))];
             cnt = 0;
             for s in sns_sorted:
                 for d in data:
                     if d['sample_name_short'] == s and d['component_group_name'] == c:
                         if d['calculated_concentration']:
                            row[cnt] = d['calculated_concentration'];
                            break;
                 cnt = cnt+1
             concentrations.append(row);
        # write concentrations to file
        export = base_exportData(concentrations);
        export.write_headerAndColumnsAndElements2csv(sns_sorted,cgn_sorted,filename);

   