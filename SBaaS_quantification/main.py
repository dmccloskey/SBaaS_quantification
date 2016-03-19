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
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')

#make the results table
from SBaaS_quantification.stage01_quantification_MQResultsTable_execute import stage01_quantification_MQResultsTable_execute
exmqrt01 = stage01_quantification_MQResultsTable_execute(session,engine,pg_settings.datadir_settings);
#exmqrt01.drop_dataStage01_quantification_MQResultsTable();
#exmqrt01.initialize_dataStage01_quantification_MQResultsTable();
#exmqrt01.execute_deleteExperimentFromMQResultsTable('chemoCLim01',sample_types_I = ['Quality Control','Unknown','Standard','Blank'])
#exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_140521_Quantification_chemoCLim01_calibrators01.csv');
#exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_Quantification_chemoCLim01_samples02.csv');
#exmqrt01.export_dataStage01MQResultsTable_metricPlot_js('chemoCLim01',component_names_I = ['fdp.fdp_1.Light'],measurement_I='calculated_concentration');

##export a metric plot
#exmqrt01.export_dataStage01MQResultsTable_metricPlot_js(
#    'ALEsKOs01',
#    sample_names_I = ['141219_0_QC_Broth-1',
#        '141219_0_QC_Broth-2',
#        '141219_0_QC_Broth-3',
#        '141219_0_QC_Broth-4',
#        '141219_0_QC_Broth-5',
#        '141219_0_QC_Broth-7',
#        '141219_0_QC_Broth-8',
#        '141219_0_QC_Broth-9',
#        '141219_0_QC_Broth-10',
#        '141219_0_QC_Broth-11',
#        '141219_0_QC_Broth-12',
#        '141219_0_QC_Broth-13',
#        '141219_0_QC_Broth-14',
#        '141219_0_QC_Broth-15',
#        '141219_0_QC_Broth-16',
#        '141219_0_QC_Broth-17',
#        '141219_0_QC_Broth-18',
#        '141219_0_QC_Broth-19',
#        '141219_0_QC_Broth-20',
#        '141219_0_QC_Broth-21',
#        '141219_0_QC_Broth-22',
#        '141219_0_QC_Broth-23',
#        '141219_0_QC_Broth-24',
#        '141219_0_QC_Broth-25',
#        '141219_0_QC_Broth-26',
#        '141219_0_QC_Broth-27',
#        '141219_0_QC_Broth-28',
#        '141219_0_QC_Broth-29',
#        '141219_0_QC_Broth-30',
#        '141219_0_QC_Broth-31',
#        '141219_0_QC_Broth-32',
#        '141219_0_QC_Broth-33',
#        '141219_0_QC_Broth-34',
#    ],
#    component_names_I = ['fdp.fdp_1.Light',
#                         'gthrd.gthrd_1.Light',
#                         'nadph.nadph_1.Light',
#                         'icit.icit_2.Light',
#                         'gln-L.gln-L_1.Light'],
#    measurement_I='calculated_concentration')

# normalize samples to biomass
from SBaaS_quantification.stage01_quantification_normalized_execute import stage01_quantification_normalized_execute
exnorm01 = stage01_quantification_normalized_execute(session,engine,pg_settings.datadir_settings);
exnorm01.initialize_supportedTables();
exnorm01.initialize_dataStage01_quantification_normalized();

# normalize samples to the measured biomass of the experiment
exnorm01.execute_normalizeSamples2Biomass(
    'IndustrialStrains02',
    biological_material_I='MG1655',
    conversion_name_I='gDW2OD_lab',
    sample_names_I = [],
    component_names_I = []);