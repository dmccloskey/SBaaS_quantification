from .stage01_quantification_QCs_query import stage01_quantification_QCs_query
from .lims_quantitationMethod_query import lims_quantitationMethod_query
from .stage01_quantification_MQResultsTable_query import stage01_quantification_MQResultsTable_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from SBaaS_base.sbaas_template_io import sbaas_template_io

class stage01_quantification_QCs_io(stage01_quantification_QCs_query,
                                    lims_quantitationMethod_query,
                                    stage01_quantification_MQResultsTable_query,
                                    sbaas_template_io):
    
    def export_checkLLOQAndULOQ_csv(self,experiment_id_I,filename='checkLLOQAndULOQ.csv'):
        '''export LLOQ and ULOQ check'''

        #TODO change to export method for .csv and .js
        
        print('export_checkLLOQAndULOQ...')
        # query data for the view
        check = [];
        check = self.get_checkLLOQAndULOQ(experiment_id_I);
        ## create and populate the view
        #for n in range(len(check)):
        #    if check[n]:
        #        row = data_stage01_quantification_checkLLOQAndULOQ(experiment_id_I,
        #                                              check[n]['sample_name'],
        #                                              check[n]['component_group_name'],
        #                                              check[n]['component_name'],
        #                                              check[n]['calculated_concentration'],
        #                                              check[n]['conc_units'],
        #                                              check[n]['correlation'],
        #                                              check[n]['lloq'],
        #                                              check[n]['uloq'],
        #                                              check[n]['points'],
        #                                              check[n]['used']);
        #        self.session.add(row);
        #self.session.commit();
        if check:
            export = base_exportData(check);
            export.write_dict2csv(filename);
        else:
            print("all components are within the lloq and uloq");
    def export_checkCV_QCs_csv(self,experiment_id_I,filename='checkCV_QCs.csv'):
        '''Export the QCs table'''
        print('execute_checkCV_QCs...')
        return;
    def export_checkCV_dilutions_csv(self,experiment_id_I,filename='checkCV_dilutions.csv'):
        '''Export the dilutions table'''

        #TODO change to export method for .csv and .js
        
        print('execute_checkCV_dilutions...')
        # query data for the view
        check = [];
        check = self.get_checkCV_dilutions(experiment_id_I);
        ## create and populate the view
        #for n in range(len(check)):
        #    if check[n]:
        #        row = data_stage01_quantification_checkCV_dilutions(check[n]['experiment_id'],
        #                                              check[n]['sample_id'],
        #                                              check[n]['component_group_name'],
        #                                              check[n]['component_name'],
        #                                              check[n]['n_replicates'],
        #                                              check[n]['calculated_concentration_average'],
        #                                              check[n]['calculated_concentration_cv'],
        #                                              check[n]['calculated_concentration_units']);
        #        self.session.add(row);
        #self.session.commit();
        export = base_exportData(check);
        export.write_dict2csv(filename);
    def export_checkISMatch_csv(self,experiment_id_I,filename='checkISMatch.csv'):
        '''check that the internal standard used in the data file
        matches that of the calibration method'''

        '''SELECT 
          experiment.id,
          data_stage01_quantification_mqresultstable.sample_name, 
          data_stage01_quantification_mqresultstable.component_name, 
          data_stage01_quantification_mqresultstable.is_name,
          quantitation_method.is_name
        FROM 
          public.data_stage01_quantification_mqresultstable, 
          public.experiment, 
          public.quantitation_method
        WHERE 
          experiment.id LIKE 'ibop_rbc02' AND 
          experiment.sample_name LIKE data_stage01_quantification_mqresultstable.sample_name AND 
          (data_stage01_quantification_mqresultstable.sample_type LIKE 'Unknown' OR
          data_stage01_quantification_mqresultstable.sample_type LIKE 'Quality Control') AND 
          experiment.quantitation_method_id LIKE quantitation_method.id AND 
          quantitation_method.component_name LIKE data_stage01_quantification_mqresultstable.component_name AND 
          data_stage01_quantification_mqresultstable.used_ AND
          NOT data_stage01_quantification_mqresultstable.is_ AND
          data_stage01_quantification_mqresultstable.is_name NOT LIKE quantitation_method.is_name;'''

        #TODO change to export method for .csv and .js

        print('execute_checkISMatch...')
        # query data for the view
        check = [];
        check = self.get_checkISMatch(experiment_id_I);
        ## create and populate the view
        #for n in range(len(check)):
        #    if check[n]:
        #        row = data_stage01_quantification_checkISMatch(experiment_id_I,
        #                                              check[n]['sample_name'],
        #                                              check[n]['component_name'],
        #                                              check[n]['IS_name_samples'],
        #                                              check[n]['IS_name_calibrators']);
        #        self.session.add(row);
        #self.session.commit();
        if check:
            print("IS mismatches found");
            export = base_exportData(check);
            export.write_dict2csv(filename);
        else:
            print("No IS mismatches found");
   