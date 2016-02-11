import sys
#sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
sys.path.append('C:/Users/dmccloskey/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings.ini';
filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_base/settings.ini';
pg_settings = postgresql_settings(filename);

## make a new database and user from the settings file
#pg_orm = postgresql_orm();
#pg_orm.create_newDatabaseAndUserFromSettings(
#            # default login made when installing postgresql
#            database_I='postgres',user_I='postgres',password_I='18dglass',host_I="localhost:5432",
#            # new settings
#            settings_I=pg_settings.database_settings,
#            # privileges for the new user
#            privileges_O=['ALL PRIVILEGES'],tables_O=['ALL TABLES'],schema_O='public');

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_LIMS')
path2Lims = pg_settings.datadir_settings['drive']+'/SBaaS_LIMS';
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_quantification')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')

# initialize the biologicalMaterial
from SBaaS_LIMS.lims_biologicalMaterial_io import lims_biologicalMaterial_io
limsbiomat = lims_biologicalMaterial_io(session,engine,pg_settings.datadir_settings);
limsbiomat.drop_lims_biologicalMaterial();
limsbiomat.initialize_lims_biologicalMaterial();
limsbiomat.reset_lims_biologicalMaterial();
limsbiomat.import_biologicalMaterialMassVolumeConversion_add(path2Lims+'/SBaaS_LIMS/'+'data/tests/analysis_quantification/140826_biologicalMaterial_massVolumeConversion_MG1655.csv');

# initialize the sample information
from SBaaS_LIMS.lims_sample_execute import lims_sample_execute
limssample = lims_sample_execute(session,engine,pg_settings.datadir_settings);
limssample.drop_lims_sample();
limssample.initialize_lims_sample();
limssample.reset_lims_sample();

# initialize the experiment
from SBaaS_LIMS.lims_experiment_execute import lims_experiment_execute
limsexperiment = lims_experiment_execute(session,engine,pg_settings.datadir_settings);
limsexperiment.drop_lims_experimentTypes();
limsexperiment.initialize_lims_experimentTypes();
limsexperiment.reset_lims_experimentTypes();
limsexperiment.drop_lims_experiment();
limsexperiment.initialize_lims_experiment();
limsexperiment.reset_lims_experiment('chemoCLim01');
limsexperiment.execute_deleteExperiments(['chemoCLim01']);
limsexperiment.execute_makeExperimentFromSampleFile('data/tests/analysis_quantification/150727_Quantification_chemoCLim01_sampleFile01.csv',1,[10.0]);
limsexperiment.execute_makeExperimentFromCalibrationFile('data/tests/analysis_quantification/150805_Quantification_chemoCLim01_calibrationFile01.csv');
# export the analyst acquisition batch files
limsexperiment.execute_makeBatchFile('chemoCLim01', '150805','data/tests/analysis_quantification/150727_Quantification_chemoCLim01.txt',experiment_type_I=4);

#make the results table
from SBaaS_quantification.stage01_quantification_MQResultsTable_execute import stage01_quantification_MQResultsTable_execute
exmqrt01 = stage01_quantification_MQResultsTable_execute(session,engine,pg_settings.datadir_settings);
exmqrt01.drop_dataStage01_quantification_MQResultsTable();
exmqrt01.initialize_dataStage01_quantification_MQResultsTable();
exmqrt01.execute_deleteExperimentFromMQResultsTable('chemoCLim01',sample_types_I = ['Quality Control','Unknown','Standard','Blank'])
exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_140521_Quantification_chemoCLim01_calibrators01.csv');
exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_Quantification_chemoCLim01_samples02.csv');
exmqrt01.export_dataStage01MQResultsTable_metricPlot_js('chemoCLim01',component_names_I = ['fdp.fdp_1.Light'],measurement_I='calculated_concentration');

#initialize the lims calibrators for quantitative experiments
from SBaaS_LIMS.lims_calibratorsAndMixes_execute import lims_calibratorsAndMixes_execute
limscalandmix = lims_calibratorsAndMixes_execute(session,engine,pg_settings.datadir_settings);
limscalandmix.drop_lims_calibratorsAndMixes();
limscalandmix.initialize_lims_calibratorsAndMixes();
limscalandmix.reset_lims_calibratorsAndMixes();
limscalandmix.import_calibratorConcentrations_add(path2Lims+'/SBaaS_LIMS/'+'data/tests/analysis_quantification/140827_calibratorConcentrations.csv');
#limscalandmix.export_calibratorConcentrations_csv(path2Lims+'/SBaaS_LIMS/'+'data/tests/analysis_quantification/140827_calibratorConcentrations_check.csv');

#make the quantitation methods table (move to SBaaS_quantification)
from SBaaS_quantification.lims_quantitationMethod_execute import lims_quantitationMethod_execute
exquant01 = lims_quantitationMethod_execute(session,engine,pg_settings.datadir_settings);
exquant01.drop_lims_quantitationMethod();
exquant01.initialize_lims_quantitationMethod();
exquant01.reset_lims_quantitationMethod(quantitation_method_id_I='140521-v02');
exquant01.import_quantitationMethod_add('140521-v02','data/tests/analysis_quantification/150805_140521_Quantification_chemoCLim01_QMethod01.csv');
exquant01.execute_quantitationMethodUpdate(quant_method_ids_I = ['140521-v02']);
exquant01.export_quantitationMethod_js('140521-v02');