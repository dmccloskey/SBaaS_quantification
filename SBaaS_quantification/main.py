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

#make the averages methods table
from SBaaS_quantification.stage01_quantification_averages_execute import stage01_quantification_averages_execute
exave01 = stage01_quantification_averages_execute(session,engine,pg_settings.datadir_settings);
exave01.initialize_supportedTables();
exave01.initialize_tables();

#calculate the geometric averages
exave01.execute_calculateGeoAverages_replicates(
    'IndustrialStrains03',
    calculated_concentration_units_I=['umol*gDW-1']);
    #'BloodProject01',
    #calculated_concentration_units_I=['uM']);