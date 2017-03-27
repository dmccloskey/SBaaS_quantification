'''TODO:
1. add in sample_name_abbreviation, sample_name_short, time_point, etc. to 
    normalized, replicates/MI, physiologicalRatiosReplicates
2. update tables to include new column data
3. optimize to remove LIMS
4. make add and update functions
5. update executions and io methods to use add/update functions'''

import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_quantification')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')

#make the results table
from SBaaS_quantification.stage01_quantification_analysis_execute import stage01_quantification_analysis_execute
analysis01 = stage01_quantification_analysis_execute(session,engine,pg_settings.datadir_settings);
analysis01.initialize_supportedTables();
analysis01.initialize_tables();

#make the results table
from SBaaS_quantification.stage01_quantification_MQResultsTable_execute import stage01_quantification_MQResultsTable_execute
exmqrt01 = stage01_quantification_MQResultsTable_execute(session,engine,pg_settings.datadir_settings);
exmqrt01.initialize_supportedTables();
exmqrt01.initialize_tables();

# normalize samples to biomass
from SBaaS_quantification.stage01_quantification_normalized_execute import stage01_quantification_normalized_execute
exnorm01 = stage01_quantification_normalized_execute(session,engine,pg_settings.datadir_settings);
exnorm01.initialize_supportedTables();
exnorm01.initialize_tables();

#make the replicates methods table
from SBaaS_quantification.stage01_quantification_replicates_execute import stage01_quantification_replicates_execute
exreps01 = stage01_quantification_replicates_execute(session,engine,pg_settings.datadir_settings);
exreps01.initialize_supportedTables();
exreps01.initialize_dataStage01_quantification_replicates();

#make the quantitation methods table
from SBaaS_quantification.stage01_quantification_peakInformation_execute import stage01_quantification_peakInformation_execute
expeak01 = stage01_quantification_peakInformation_execute(session,engine,pg_settings.datadir_settings);
expeak01.initialize_supportedTables();
expeak01.initialize_tables();

#analyze peakInformation
expeak01.execute_analyzePeakInformation(
        analysis_id_I = ['RapidRIP01_SST01'], 
        experiment_id_I = ['RapidRIP01'],
        sample_names_I = [],
        sample_types_I = ['Standard'],
        peakInfo_I = ['height','retention_time','width_at_50',
                      'signal_2_noise','points_across_baseline'],
        acquisition_date_and_time_I=[]);