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
from SBaaS_quantification.stage01_quantification_MQResultsTable_execute import stage01_quantification_MQResultsTable_execute
exmqrt01 = stage01_quantification_MQResultsTable_execute(session,engine,pg_settings.datadir_settings);
exmqrt01.initialize_supportedTables();
exmqrt01.initialize_dataStage01_quantification_MQResultsTable();
#exmqrt01.drop_dataStage01_quantification_MQResultsTable();
#exmqrt01.initialize_dataStage01_quantification_MQResultsTable();
#exmqrt01.execute_deleteExperimentFromMQResultsTable('chemoCLim01',sample_types_I = ['Quality Control','Unknown','Standard','Blank'])
#exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_140521_Quantification_chemoCLim01_calibrators01.csv');
#exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_Quantification_chemoCLim01_samples02.csv');
#exmqrt01.export_dataStage01MQResultsTable_metricPlot_js('chemoCLim01',component_names_I = ['fdp.fdp_1.Light'],measurement_I='calculated_concentration');

#exmqrt01.import_dataStage01MQResultsTable_update(
#        pg_settings.datadir_settings['workspace_data']+'/_input/160331_Quantification_ALEsKOs01_updates02.csv');

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
sampleName_componentName_listDict = [
    {'sample_names':['140716_0_OxicEvo04pgiEcoliGlcM9_Broth-6-10.0x'],
     'component_names':['glutacon.glutacon_1.Light']},
    {'sample_names':['141022_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-1-10.0x',
                     '141024_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-2-10.0x',
                     '141024_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-3-10.0x',
                     '141022_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-4-10.0x',
                     '141024_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-5-10.0x',
                     '141024_3_OxicEvo04pgiEvo02J03EcoliGlcM9_Broth-6-10.0x'],
     'component_names':['orn.orn_1.Light']},
    {'sample_names':['140801_11_OxicEvo04pgiEvo07EPEcoliGlcM9_Broth-5'],
     'component_names':['dctp.dctp_1.Light']},
    {'sample_names':['140808_11_OxicEvo04tpiAEvo02EPEcoliGlcM9_Broth-6-10.0x'],
     'component_names':['glu-L.glu-L_1.Light']},
    ]
#for row in sampleName_componentName_listDict:
#    exnorm01.reset_dataStage01_quantification_normalized(
#        experiment_id_I='ALEsKOs01',
#        sample_names_I = row['sample_names'],
#        component_names_I = row['component_names'])
#    exnorm01.execute_normalizeSamples2Biomass(
#        'ALEsKOs01',
#        biological_material_I='MG1655',
#        conversion_name_I='gDW2OD_lab',
#        sample_names_I = row['sample_names'],
#        component_names_I = row['component_names'])

# normalize samples to biomass
from SBaaS_quantification.stage01_quantification_normalized_execute import stage01_quantification_normalized_execute
exnorm01 = stage01_quantification_normalized_execute(session,engine,pg_settings.datadir_settings);
exnorm01.initialize_supportedTables();
exnorm01.initialize_tables();

## reset previous normalizations
#sampleName_componentName_listDict = [
#    {'sample_names':['150601_0_BloodProject01_PLT_30_Broth-1','150601_0_BloodProject01_PLT_30_Broth-1-10.0x','150601_0_BloodProject01_PLT_30_Broth-2','150601_0_BloodProject01_PLT_30_Broth-2-10.0x','150601_0_BloodProject01_PLT_30_Broth-3','150601_0_BloodProject01_PLT_30_Broth-3-10.0x','150601_0_BloodProject01_PLT_30_Broth-4','150601_0_BloodProject01_PLT_30_Broth-4-10.0x','150601_0_BloodProject01_PLT_30_Broth-5','150601_0_BloodProject01_PLT_30_Broth-5-10.0x','150601_0_BloodProject01_PLT_30_Broth-6','150601_0_BloodProject01_PLT_30_Broth-6-10.0x','150601_0_BloodProject01_PLT_31_Broth-1','150601_0_BloodProject01_PLT_31_Broth-1-10.0x','150601_0_BloodProject01_PLT_31_Broth-2','150601_0_BloodProject01_PLT_31_Broth-2-10.0x','150601_0_BloodProject01_PLT_31_Broth-3','150601_0_BloodProject01_PLT_31_Broth-3-10.0x','150601_0_BloodProject01_PLT_31_Broth-4','150601_0_BloodProject01_PLT_31_Broth-4-10.0x','150601_0_BloodProject01_PLT_31_Broth-5','150601_0_BloodProject01_PLT_31_Broth-5-10.0x','150601_0_BloodProject01_PLT_31_Broth-6','150601_0_BloodProject01_PLT_31_Broth-6-10.0x','150601_0_BloodProject01_PLT_32_Broth-1','150601_0_BloodProject01_PLT_32_Broth-1-10.0x','150601_0_BloodProject01_PLT_32_Broth-2','150601_0_BloodProject01_PLT_32_Broth-2-10.0x','150601_0_BloodProject01_PLT_32_Broth-3','150601_0_BloodProject01_PLT_32_Broth-3-10.0x','150601_0_BloodProject01_PLT_32_Broth-4','150601_0_BloodProject01_PLT_32_Broth-4-10.0x','150601_0_BloodProject01_PLT_32_Broth-5','150601_0_BloodProject01_PLT_32_Broth-5-10.0x','150601_0_BloodProject01_PLT_32_Broth-6','150601_0_BloodProject01_PLT_32_Broth-6-10.0x','150601_0_BloodProject01_PLT_33_Broth-1','150601_0_BloodProject01_PLT_33_Broth-1-10.0x','150601_0_BloodProject01_PLT_33_Broth-2','150601_0_BloodProject01_PLT_33_Broth-2-10.0x','150601_0_BloodProject01_PLT_33_Broth-3','150601_0_BloodProject01_PLT_33_Broth-3-10.0x','150601_0_BloodProject01_PLT_33_Broth-4','150601_0_BloodProject01_PLT_33_Broth-4-10.0x','150601_0_BloodProject01_PLT_33_Broth-5','150601_0_BloodProject01_PLT_33_Broth-5-10.0x','150601_0_BloodProject01_PLT_33_Broth-6','150601_0_BloodProject01_PLT_33_Broth-6-10.0x','150601_0_BloodProject01_PLT_34_Broth-1','150601_0_BloodProject01_PLT_34_Broth-1-10.0x','150601_0_BloodProject01_PLT_34_Broth-2','150601_0_BloodProject01_PLT_34_Broth-2-10.0x','150601_0_BloodProject01_PLT_34_Broth-3','150601_0_BloodProject01_PLT_34_Broth-3-10.0x','150601_0_BloodProject01_PLT_34_Broth-4','150601_0_BloodProject01_PLT_34_Broth-4-10.0x','150601_0_BloodProject01_PLT_34_Broth-5','150601_0_BloodProject01_PLT_34_Broth-5-10.0x','150601_0_BloodProject01_PLT_34_Broth-6','150601_0_BloodProject01_PLT_34_Broth-6-10.0x','150601_0_BloodProject01_PLT_35_Broth-1','150601_0_BloodProject01_PLT_35_Broth-1-10.0x','150601_0_BloodProject01_PLT_35_Broth-2','150601_0_BloodProject01_PLT_35_Broth-2-10.0x','150601_0_BloodProject01_PLT_35_Broth-3','150601_0_BloodProject01_PLT_35_Broth-3-10.0x','150601_0_BloodProject01_PLT_35_Broth-4','150601_0_BloodProject01_PLT_35_Broth-4-10.0x','150601_0_BloodProject01_PLT_35_Broth-5','150601_0_BloodProject01_PLT_35_Broth-5-10.0x','150601_0_BloodProject01_PLT_35_Broth-6','150601_0_BloodProject01_PLT_35_Broth-6-10.0x','150601_0_BloodProject01_PLT_36_Broth-1','150601_0_BloodProject01_PLT_36_Broth-1-10.0x','150601_0_BloodProject01_PLT_36_Broth-2','150601_0_BloodProject01_PLT_36_Broth-2-10.0x','150601_0_BloodProject01_PLT_36_Broth-3','150601_0_BloodProject01_PLT_36_Broth-3-10.0x','150601_0_BloodProject01_PLT_36_Broth-4','150601_0_BloodProject01_PLT_36_Broth-4-10.0x','150601_0_BloodProject01_PLT_36_Broth-5','150601_0_BloodProject01_PLT_36_Broth-5-10.0x','150601_0_BloodProject01_PLT_36_Broth-6','150601_0_BloodProject01_PLT_36_Broth-6-10.0x','150601_0_BloodProject01_PLT_37_Broth-1','150601_0_BloodProject01_PLT_37_Broth-1-10.0x','150601_0_BloodProject01_PLT_37_Broth-2','150601_0_BloodProject01_PLT_37_Broth-2-10.0x','150601_0_BloodProject01_PLT_37_Broth-3','150601_0_BloodProject01_PLT_37_Broth-3-10.0x','150601_0_BloodProject01_PLT_37_Broth-4','150601_0_BloodProject01_PLT_37_Broth-4-10.0x','150601_0_BloodProject01_PLT_37_Broth-5','150601_0_BloodProject01_PLT_37_Broth-5-10.0x','150601_0_BloodProject01_PLT_37_Broth-6','150601_0_BloodProject01_PLT_37_Broth-6-10.0x','150601_0_BloodProject01_PLT_38_Broth-1','150601_0_BloodProject01_PLT_38_Broth-1-10.0x','150601_0_BloodProject01_PLT_38_Broth-2','150601_0_BloodProject01_PLT_38_Broth-2-10.0x','150601_0_BloodProject01_PLT_38_Broth-3','150601_0_BloodProject01_PLT_38_Broth-3-10.0x','150601_0_BloodProject01_PLT_38_Broth-4','150601_0_BloodProject01_PLT_38_Broth-4-10.0x','150601_0_BloodProject01_PLT_38_Broth-5','150601_0_BloodProject01_PLT_38_Broth-5-10.0x','150601_0_BloodProject01_PLT_38_Broth-6','150601_0_BloodProject01_PLT_38_Broth-6-10.0x','150601_0_BloodProject01_PLT_39_Broth-1','150601_0_BloodProject01_PLT_39_Broth-1-10.0x','150601_0_BloodProject01_PLT_39_Broth-2','150601_0_BloodProject01_PLT_39_Broth-2-10.0x','150601_0_BloodProject01_PLT_39_Broth-3','150601_0_BloodProject01_PLT_39_Broth-3-10.0x','150601_0_BloodProject01_PLT_39_Broth-4','150601_0_BloodProject01_PLT_39_Broth-4-10.0x','150601_0_BloodProject01_PLT_39_Broth-5','150601_0_BloodProject01_PLT_39_Broth-5-10.0x','150601_0_BloodProject01_PLT_39_Broth-6','150601_0_BloodProject01_PLT_39_Broth-6-10.0x','150601_0_BloodProject01_PLT_40_Broth-1','150601_0_BloodProject01_PLT_40_Broth-1-10.0x','150601_0_BloodProject01_PLT_40_Broth-2','150601_0_BloodProject01_PLT_40_Broth-2-10.0x','150601_0_BloodProject01_PLT_40_Broth-3','150601_0_BloodProject01_PLT_40_Broth-3-10.0x','150601_0_BloodProject01_PLT_40_Broth-4','150601_0_BloodProject01_PLT_40_Broth-4-10.0x','150601_0_BloodProject01_PLT_40_Broth-5','150601_0_BloodProject01_PLT_40_Broth-5-10.0x','150601_0_BloodProject01_PLT_40_Broth-6','150601_0_BloodProject01_PLT_40_Broth-6-10.0x','150601_0_BloodProject01_PLT_42_Broth-1','150601_0_BloodProject01_PLT_42_Broth-1-10.0x','150601_0_BloodProject01_PLT_42_Broth-2','150601_0_BloodProject01_PLT_42_Broth-2-10.0x','150601_0_BloodProject01_PLT_42_Broth-3','150601_0_BloodProject01_PLT_42_Broth-3-10.0x','150601_0_BloodProject01_PLT_42_Broth-4','150601_0_BloodProject01_PLT_42_Broth-4-10.0x','150601_0_BloodProject01_PLT_42_Broth-5','150601_0_BloodProject01_PLT_42_Broth-5-10.0x','150601_0_BloodProject01_PLT_42_Broth-6','150601_0_BloodProject01_PLT_42_Broth-6-10.0x'],
#     'component_names':[]},
#    ]
## reset previous normalizations
#for row in sampleName_componentName_listDict:
#    exnorm01.reset_dataStage01_quantification_normalized(
#        experiment_id_I='BloodProject01',
#        sample_names_I = row['sample_names'],
#        component_names_I = row['component_names'])
#    exnorm01.execute_normalizeSamples2Biomass(
#        'BloodProject01',
#        biological_material_I=None,
#        conversion_name_I=None,
#        sample_names_I = row['sample_names'],
#        component_names_I = row['component_names'])

blank_sample_names = [];

sample_name_abbreviations_str = 'PLT_30,PLT_31,PLT_32,PLT_33,PLT_34,PLT_35\
PLT_36,PLT_37,PLT_38,PLT_39,PLT_40,PLT_42'
sample_name_abbreviations = sample_name_abbreviations_str.split(',');

##reset previous average calculations
#exnorm01.reset_dataStage01_quantification_averages(
#     'BloodProject01',
#     sample_name_abbreviations_I=sample_name_abbreviations);
## calculate replicates using the formula ave(broth),i - ave(blanks,broth) for specific samples
#exnorm01.execute_analyzeAverages_blanks(
#    'BloodProject01',
#    blank_sample_names_I=blank_sample_names,
#    sample_name_abbreviations_I=sample_name_abbreviations);
# export the data to ddt
#exnorm01.export_dataStage01NormalizedAndAverages_js(
#        'BloodProject01',
#        sample_name_abbreviations_I=sample_name_abbreviations,
#        sample_names_I=[],
#        component_names_I=[],
#        cv_threshold_I=40,
#        extracellular_threshold_I=80,
#        data_dir_I='tmp'
#    );

#check for duplicate dilutions
exnorm01.execute_findDuplicateDilutions(
        'BloodProject01',
        );

#make the replicates methods table
from SBaaS_quantification.stage01_quantification_replicates_execute import stage01_quantification_replicates_execute
exreps01 = stage01_quantification_replicates_execute(session,engine,pg_settings.datadir_settings);
exreps01.initialize_supportedTables();
exreps01.initialize_dataStage01_quantification_replicates();

sample_name_abbreviations_str = 'PLT_30,PLT_31,PLT_32,PLT_33,PLT_34,PLT_35\
PLT_36,PLT_37,PLT_38,PLT_39,PLT_40,PLT_42'
sample_name_abbreviations = sample_name_abbreviations_str.split(',');

sample_name_shorts_str = ''
sample_name_shorts = sample_name_shorts_str.split(',');
sample_name_shorts = [];

sample_names_str = ''
sample_names = sample_names_str.split(',');
sample_names = []

component_names_str = ''
component_names = component_names_str.split(',');
component_names = []

sampleNameShorts_componentName_listDict = [
    {'sample_name_shorts':sample_name_shorts,
     'component_names':component_names},
    ]
sampleNames_sampleNameAbbreviations_componentName_listDict = [
    {'sample_names':sample_names,
    'sample_name_abbreviations':sample_name_abbreviations,
     'component_names':component_names},
    ]
for row in sampleNameShorts_componentName_listDict:
    #reset previous calculations
    exreps01.reset_dataStage01_quantification_replicates(
        'BloodProject01',
        sample_name_short_I=row['sample_name_shorts'],
        component_names_I=row['component_names'],
        );
for row in sampleNames_sampleNameAbbreviations_componentName_listDict:
    # calculate replicates using the formula broth,i - ave(filtrate) for specific samples
    exreps01.execute_analyzeReplicates(
        'BloodProject01',
        sample_name_abbreviations_I=row['sample_name_abbreviations'],
        component_names_I=row['component_names'],
        sample_names_I=row['sample_names'],
        );

from SBaaS_quantification.stage01_quantification_physiologicalRatios_execute import stage01_quantification_physiologicalRatios_execute
exphysratio01 = stage01_quantification_physiologicalRatios_execute(session,engine,pg_settings.datadir_settings);
exphysratio01.initialize_supportedTables();
exphysratio01.initialize_dataStage01_quantification_physiologicalRatios();

#calculate the physiological ratios for replicates and averages
#exphysratio01.execute_physiologicalRatios_replicates('ALEsKOs01');
#exphysratio01.export_dataStage01QuantificationPhysiologicalRatios_js('ALEsKOs01',
#                sample_name_abbreviations_I=['OxicEvo04pgiEvo02J03EcoliGlc'],
#                ratio_ids_I=[],
#                data_dir_I = 'tmp');

#make the quantitation methods table (move to SBaaS_quantification)
from SBaaS_quantification.lims_quantitationMethod_execute import lims_quantitationMethod_execute
exquant01 = lims_quantitationMethod_execute(session,engine,pg_settings.datadir_settings);
exquant01.initialize_supportedTables();
exquant01.initialize_lims_quantitationMethod();

##export the method
#exquant01.export_quantitationMethod_js('141220');

#make the missing values table
from SBaaS_quantification.stage01_quantification_replicatesMI_execute import stage01_quantification_replicatesMI_execute
exrepsMI01 = stage01_quantification_replicatesMI_execute(session,engine,pg_settings.datadir_settings);
exrepsMI01.initialize_supportedTables();
exrepsMI01.initialize_tables();

##import values from dataPreProcessing
#exrepsMI01.import_rows_table_add_csv(
#    table_I="data_stage01_quantification_replicatesmi",
#    filename_I=pg_settings.datadir_settings['workspace_data']+'/_input/160410_Quantification_ALEsKOs01_imputedValues01.csv')

#make the averages methods table
from SBaaS_quantification.stage01_quantification_averages_execute import stage01_quantification_averages_execute
exave01 = stage01_quantification_averages_execute(session,engine,pg_settings.datadir_settings);
exave01.initialize_supportedTables();
exave01.initialize_tables();

##calculate the geometric averages
#exave01.execute_calculateGeoAverages_replicates(
#    'ALEsKOs01',
#    #sample_name_abbreviations_I=['OxicEvo04EcoliGlc','OxicEvo04Evo01EPEcoliGlc','OxicEvo04Evo02EPEcoliGlc','OxicEvo04gndEcoliGlc','OxicEvo04gndEvo01EPEcoliGlc','OxicEvo04gndEvo02EPEcoliGlc','OxicEvo04gndEvo03EPEcoliGlc','OxicEvo04pgiEcoliGlc','OxicEvo04pgiEvo01EPEcoliGlc','OxicEvo04pgiEvo01J01EcoliGlc','OxicEvo04pgiEvo01J02EcoliGlc','OxicEvo04pgiEvo02EPEcoliGlc','OxicEvo04pgiEvo02J01EcoliGlc','OxicEvo04pgiEvo02J02EcoliGlc','OxicEvo04pgiEvo02J03EcoliGlc','OxicEvo04pgiEvo03EPEcoliGlc','OxicEvo04pgiEvo03J01EcoliGlc','OxicEvo04pgiEvo03J02EcoliGlc','OxicEvo04pgiEvo03J03EcoliGlc','OxicEvo04pgiEvo04EPEcoliGlc','OxicEvo04pgiEvo04J01EcoliGlc','OxicEvo04pgiEvo04J02EcoliGlc','OxicEvo04pgiEvo04J03EcoliGlc','OxicEvo04pgiEvo05EPEcoliGlc','OxicEvo04pgiEvo05J01EcoliGlc','OxicEvo04pgiEvo05J02EcoliGlc','OxicEvo04pgiEvo05J03EcoliGlc','OxicEvo04pgiEvo06EPEcoliGlc','OxicEvo04pgiEvo06J01EcoliGlc','OxicEvo04pgiEvo06J02EcoliGlc','OxicEvo04pgiEvo06J03EcoliGlc','OxicEvo04pgiEvo07EPEcoliGlc','OxicEvo04pgiEvo07J01EcoliGlc','OxicEvo04pgiEvo07J02EcoliGlc','OxicEvo04pgiEvo07J03EcoliGlc','OxicEvo04pgiEvo08EPEcoliGlc','OxicEvo04pgiEvo08J01EcoliGlc','OxicEvo04pgiEvo08J02EcoliGlc','OxicEvo04pgiEvo08J03EcoliGlc','OxicEvo04ptsHIcrrEcoliGlc','OxicEvo04ptsHIcrrEvo01EPEcoliGlc','OxicEvo04ptsHIcrrEvo01J01EcoliGlc','OxicEvo04ptsHIcrrEvo01J03EcoliGlc','OxicEvo04ptsHIcrrEvo02EPEcoliGlc','OxicEvo04ptsHIcrrEvo02J01EcoliGlc','OxicEvo04ptsHIcrrEvo02J03EcoliGlc','OxicEvo04ptsHIcrrEvo03EPEcoliGlc','OxicEvo04ptsHIcrrEvo03J01EcoliGlc','OxicEvo04ptsHIcrrEvo03J03EcoliGlc','OxicEvo04ptsHIcrrEvo03J04EcoliGlc','OxicEvo04ptsHIcrrEvo04EPEcoliGlc','OxicEvo04ptsHIcrrEvo04J01EcoliGlc','OxicEvo04ptsHIcrrEvo04J03EcoliGlc','OxicEvo04ptsHIcrrEvo04J04EcoliGlc','OxicEvo04sdhCBEcoliGlc','OxicEvo04sdhCBEvo01EPEcoliGlc','OxicEvo04sdhCBEvo02EPEcoliGlc','OxicEvo04sdhCBEvo03EPEcoliGlc','OxicEvo04tpiAEcoliGlc','OxicEvo04tpiAEvo01EPEcoliGlc','OxicEvo04tpiAEvo01J01EcoliGlc','OxicEvo04tpiAEvo01J03EcoliGlc','OxicEvo04tpiAEvo02EPEcoliGlc','OxicEvo04tpiAEvo02J01EcoliGlc','OxicEvo04tpiAEvo02J03EcoliGlc','OxicEvo04tpiAEvo03EPEcoliGlc','OxicEvo04tpiAEvo03J01EcoliGlc','OxicEvo04tpiAEvo03J03EcoliGlc','OxicEvo04tpiAEvo04EPEcoliGlc','OxicEvo04tpiAEvo04J01EcoliGlc','OxicEvo04tpiAEvo04J03EcoliGlc'],
#    calculated_concentration_units_I=['mM']);