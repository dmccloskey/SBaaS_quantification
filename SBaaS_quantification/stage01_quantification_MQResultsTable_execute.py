
from .stage01_quantification_MQResultsTable_io import stage01_quantification_MQResultsTable_io
from SBaaS_LIMS.lims_experiment_query import lims_experiment_query

class stage01_quantification_MQResultsTable_execute(stage01_quantification_MQResultsTable_io,
                                                    lims_experiment_query):

    def execute_deleteExperimentFromMQResultsTable(self,experiment_id_I,sample_types_I = ['Quality Control','Unknown'],sample_names_I = []):
        '''delete rows in data_stage01_MQResultsTable by sample name and sample type 
        (default = Quality Control and Unknown) from the experiment'''
        
        print('deleting rows in data_stage01_MQResultsTable by sample_name and sample_type...');
        dataDeletes = [];
        # get sample_names
        if sample_names_I:
            sample_names = sample_names_I;
        else:
            sample_names = [];
            for st in sample_types_I:
                sample_names_tmp = [];
                sample_names_tmp = self.get_sampleNames_experimentIDAndSampleType(experiment_id_I,st);
                sample_names.extend(sample_names_tmp);
        for sn in sample_names:
            # format into a dictionary list
            print('deleting sample_name ' + sn);
            dataDeletes.append({'sample_name':sn});
        # delete rows based on sample_names
        self.delete_row_sampleName(dataDeletes);