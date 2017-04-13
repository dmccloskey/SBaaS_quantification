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

sample_name_abbreviations_str = 'RBC_140,RBC_141,RBC_142,RBC_143,RBC_150,RBC_151,RBC_152,RBC_153,RBC_154,RBC_155,RBC_30,RBC_31,RBC_32,RBC_33,RBC_34,RBC_35,RBC_36,RBC_37,RBC_38,RBC_39,RBC_40,RBC_42,S01_D01_RBC_25C_0hr,S01_D01_RBC_25C_22hr,S01_D01_RBC_25C_2hr,S01_D01_RBC_25C_6.5hr,S01_D01_RBC_37C_22hr,S01_D02_RBC_25C_0hr,S01_D02_RBC_25C_22hr,S01_D02_RBC_25C_2hr,S01_D02_RBC_25C_6.5hr,S01_D02_RBC_37C_22hr,S01_D03_RBC_25C_0hr,S01_D03_RBC_25C_22hr,S01_D03_RBC_25C_2hr,S01_D03_RBC_25C_6.5hr,S01_D03_RBC_37C_22hr,S01_D04_RBC_25C_0hr,S01_D04_RBC_25C_22hr,S01_D04_RBC_25C_2hr,S01_D04_RBC_25C_6.5hr,S01_D04_RBC_37C_22hr,S01_D05_RBC_25C_0hr,S01_D05_RBC_25C_22hr,S01_D05_RBC_25C_2hr,S01_D05_RBC_25C_6.5hr,S01_D05_RBC_37C_22hr,S02_D01_RBC_25C_0hr,S02_D01_RBC_25C_22hr,S02_D01_RBC_25C_2hr,S02_D01_RBC_25C_6.5hr,S02_D01_RBC_37C_22hr,S02_D02_RBC_25C_0hr,S02_D02_RBC_25C_22hr,S02_D02_RBC_25C_2hr,S02_D02_RBC_25C_6.5hr,S02_D02_RBC_37C_22hr,S02_D03_RBC_25C_0hr,S02_D03_RBC_25C_22hr,S02_D03_RBC_25C_2hr,S02_D03_RBC_25C_6.5hr,S02_D03_RBC_37C_22hr,S02_D04_RBC_25C_0hr,S02_D04_RBC_25C_22hr,S02_D04_RBC_25C_2hr,S02_D04_RBC_25C_6.5hr,S02_D04_RBC_37C_22hr,S02_D05_RBC_25C_0hr,S02_D05_RBC_25C_22hr,S02_D05_RBC_25C_2hr,S02_D05_RBC_25C_6.5hr,S02_D05_RBC_37C_22hr'
# sample_name_abbreviations_str = 'PLT_140,PLT_141,PLT_142,PLT_143,PLT_150,PLT_151,PLT_152,PLT_153,PLT_154,PLT_155,PLT_30,PLT_31,PLT_32,PLT_33,PLT_34,PLT_35,PLT_36,PLT_37,PLT_38,PLT_39,PLT_40,PLT_42,S01_D01_PLT_25C_0hr,S01_D01_PLT_25C_22hr,S01_D01_PLT_25C_2hr,S01_D01_PLT_25C_6.5hr,S01_D01_PLT_37C_22hr,S01_D02_PLT_25C_0hr,S01_D02_PLT_25C_22hr,S01_D02_PLT_25C_2hr,S01_D02_PLT_25C_6.5hr,S01_D02_PLT_37C_22hr,S01_D03_PLT_25C_0hr,S01_D03_PLT_25C_22hr,S01_D03_PLT_25C_2hr,S01_D03_PLT_25C_6.5hr,S01_D03_PLT_37C_22hr,S01_D04_PLT_25C_0hr,S01_D04_PLT_25C_22hr,S01_D04_PLT_25C_2hr,S01_D04_PLT_25C_6.5hr,S01_D04_PLT_37C_22hr,S01_D05_PLT_25C_0hr,S01_D05_PLT_25C_22hr,S01_D05_PLT_25C_2hr,S01_D05_PLT_25C_6.5hr,S01_D05_PLT_37C_22hr,S02_D01_PLT_25C_0hr,S02_D01_PLT_25C_22hr,S02_D01_PLT_25C_2hr,S02_D01_PLT_25C_6.5hr,S02_D01_PLT_37C_22hr,S02_D02_PLT_25C_0hr,S02_D02_PLT_25C_22hr,S02_D02_PLT_25C_2hr,S02_D02_PLT_25C_6.5hr,S02_D02_PLT_37C_22hr,S02_D03_PLT_25C_0hr,S02_D03_PLT_25C_22hr,S02_D03_PLT_25C_2hr,S02_D03_PLT_25C_6.5hr,S02_D03_PLT_37C_22hr,S02_D04_PLT_25C_0hr,S02_D04_PLT_25C_22hr,S02_D04_PLT_25C_2hr,S02_D04_PLT_25C_6.5hr,S02_D04_PLT_37C_22hr,S02_D05_PLT_25C_0hr,S02_D05_PLT_25C_22hr,S02_D05_PLT_25C_2hr,S02_D05_PLT_25C_6.5hr,S02_D05_PLT_37C_22hr'
sample_name_abbreviations = sample_name_abbreviations_str.split(',')

exreps01.execute_analyzeReplicates('BloodProject01',
      sample_name_abbreviations_I = sample_name_abbreviations)

#make the quantitation methods table
from SBaaS_quantification.stage01_quantification_peakInformation_execute import stage01_quantification_peakInformation_execute
expeak01 = stage01_quantification_peakInformation_execute(session,engine,pg_settings.datadir_settings);
expeak01.initialize_supportedTables();
expeak01.initialize_tables();

#make the quantitation methods table (move to SBaaS_quantification)
from SBaaS_quantification.lims_quantitationMethod_execute import lims_quantitationMethod_execute
exquant01 = lims_quantitationMethod_execute(session,engine,pg_settings.datadir_settings);
exquant01.initialize_supportedTables();
exquant01.initialize_tables();

#make the QC methods tables
from SBaaS_quantification.stage01_quantification_QCs_execute import stage01_quantification_QCs_execute
exqcs01 = stage01_quantification_QCs_execute(session,engine,pg_settings.datadir_settings);
exqcs01.initialize_supportedTables();
exqcs01.initialize_tables();

#import time as time
##analyze the LLOQ
#st = time.time();
#exqcs01.execute_LLOQAndULOQ('BloodProject01',                            
#    calculated_concentration_units_I=['uM'],
#    sample_names_I = ['150601_0_BloodProject01_RBC_140_Broth-1'],
#    sample_types_I = ['Unknown']
#    );
#elapsed_time = time.time() - st;
#print("Elapsed time: %.2fs" % elapsed_time)