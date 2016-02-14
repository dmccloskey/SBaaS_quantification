'''TODO:
1. add in sample_name_abbreviation, sample_name_short, time_point, etc. to 
    normalized, replicates/MI, physiologicalRatiosReplicates
2. update tables to include new column data
3. optimize to remove LIMS
4. make add and update functions
5. update executions and io methods to use add/update functions'''

import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
#sys.path.append('C:/Users/dmccloskey/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics_151001.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_base/settings_2.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
path2Lims = pg_settings.datadir_settings['github']+'/SBaaS_LIMS';
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_quantification')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_visualization')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/quantification_analysis')
sys.path.append(pg_settings.datadir_settings['github']+'/matplotlib_utilities')

## initialize the biologicalMaterial_geneReferences
#from SBaaS_LIMS.lims_biologicalMaterial_io import lims_biologicalMaterial_io
#limsbiomat = lims_biologicalMaterial_io(session,engine,pg_settings.datadir_settings);
#limsbiomat.drop_lims_biologicalMaterial();
#limsbiomat.initialize_lims_biologicalMaterial();
#limsbiomat.reset_lims_biologicalMaterial();
#limsbiomat.import_biologicalMaterialMassVolumeConversion_add(path2Lims+'/SBaaS_LIMS/'+'data/tests/analysis_quantification/140826_biologicalMaterial_massVolumeConversion_MG1655.csv');

## initialize the sample information
#from SBaaS_LIMS.lims_sample_execute import lims_sample_execute
#limssample = lims_sample_execute(session,engine,pg_settings.datadir_settings);
#limssample.drop_lims_sample();
#limssample.initialize_lims_sample();
#limssample.reset_lims_sample();

## initialize the experiment
#from SBaaS_LIMS.lims_experiment_execute import lims_experiment_execute
#limsexperiment = lims_experiment_execute(session,engine,pg_settings.datadir_settings);
#limsexperiment.drop_lims_experimentTypes();
#limsexperiment.initialize_lims_experimentTypes();
#limsexperiment.reset_lims_experimentTypes();
#limsexperiment.drop_lims_experiment();
#limsexperiment.initialize_lims_experiment();
#limsexperiment.reset_lims_experiment('chemoCLim01');
#limsexperiment.execute_deleteExperiments(['chemoCLim01']);
#limsexperiment.execute_makeExperimentFromSampleFile('data/tests/analysis_quantification/150727_Quantification_chemoCLim01_sampleFile01.csv',1,[10.0]);
#limsexperiment.execute_makeExperimentFromCalibrationFile('data/tests/analysis_quantification/150805_Quantification_chemoCLim01_calibrationFile01.csv');
##TODO: link exp_type_id = 4 with metabolomics
##sample_name and sample_id are unique
##sample_name_short and sample_name_abbreviation are not and can come from multiple experiment types from within the same experiment
## export the analyst acquisition batch files
#limsexperiment.execute_makeBatchFile('chemoCLim01', '150805','data/tests/analysis_quantification/150727_Quantification_chemoCLim01.txt',experiment_type_I=4);

#make the results table
from SBaaS_quantification.stage01_quantification_MQResultsTable_execute import stage01_quantification_MQResultsTable_execute
exmqrt01 = stage01_quantification_MQResultsTable_execute(session,engine,pg_settings.datadir_settings);
#exmqrt01.drop_dataStage01_quantification_MQResultsTable();
#exmqrt01.initialize_dataStage01_quantification_MQResultsTable();
#exmqrt01.execute_deleteExperimentFromMQResultsTable('chemoCLim01',sample_types_I = ['Quality Control','Unknown','Standard','Blank'])
#exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_140521_Quantification_chemoCLim01_calibrators01.csv');
#exmqrt01.import_dataStage01MQResultsTable_add('data/tests/analysis_quantification/150805_Quantification_chemoCLim01_samples02.csv');
#exmqrt01.export_dataStage01MQResultsTable_metricPlot_js('chemoCLim01',component_names_I = ['fdp.fdp_1.Light'],measurement_I='calculated_concentration');

#export a metric plot
exmqrt01.export_dataStage01MQResultsTable_metricPlot_js(
    'ALEsKOs01',
    sample_names_I = ['141219_0_QC_Broth-1',
        '141219_0_QC_Broth-2',
        '141219_0_QC_Broth-3',
        '141219_0_QC_Broth-4',
        '141219_0_QC_Broth-5',
        '141219_0_QC_Broth-7',
        '141219_0_QC_Broth-8',
        '141219_0_QC_Broth-9',
        '141219_0_QC_Broth-10',
        '141219_0_QC_Broth-11',
        '141219_0_QC_Broth-12',
        '141219_0_QC_Broth-13',
        '141219_0_QC_Broth-14',
        '141219_0_QC_Broth-15',
        '141219_0_QC_Broth-16',
        '141219_0_QC_Broth-17',
        '141219_0_QC_Broth-18',
        '141219_0_QC_Broth-19',
        '141219_0_QC_Broth-20',
        '141219_0_QC_Broth-21',
        '141219_0_QC_Broth-22',
        '141219_0_QC_Broth-23',
        '141219_0_QC_Broth-24',
        '141219_0_QC_Broth-25',
        '141219_0_QC_Broth-26',
        '141219_0_QC_Broth-27',
        '141219_0_QC_Broth-28',
        '141219_0_QC_Broth-29',
        '141219_0_QC_Broth-30',
        '141219_0_QC_Broth-31',
        '141219_0_QC_Broth-32',
        '141219_0_QC_Broth-33',
        '141219_0_QC_Broth-34',
    ],
    component_names_I = ['fdp.fdp_1.Light',
                         'gthrd.gthrd_1.Light',
                         'nadph.nadph_1.Light',
                         'icit.icit_2.Light',
                         'gln-L.gln-L_1.Light'],
    measurement_I='calculated_concentration')

##initialize the lims calibrators for quantitative experiments
#from SBaaS_LIMS.lims_calibratorsAndMixes_execute import lims_calibratorsAndMixes_execute
#limscalandmix = lims_calibratorsAndMixes_execute(session,engine,pg_settings.datadir_settings);
#limscalandmix.drop_lims_calibratorsAndMixes();
#limscalandmix.initialize_lims_calibratorsAndMixes();
#limscalandmix.reset_lims_calibratorsAndMixes();
#limscalandmix.import_calibratorConcentrations_add(path2Lims+'/SBaaS_LIMS/'+'data/tests/analysis_quantification/140827_calibratorConcentrations.csv');
##limscalandmix.export_calibratorConcentrations_csv(path2Lims+'/SBaaS_LIMS/'+'data/tests/analysis_quantification/140827_calibratorConcentrations_check.csv');

##make the quantitation methods table (move to SBaaS_quantification)
#from SBaaS_quantification.lims_quantitationMethod_execute import lims_quantitationMethod_execute
#exquant01 = lims_quantitationMethod_execute(session,engine,pg_settings.datadir_settings);
#exquant01.drop_lims_quantitationMethod();
#exquant01.initialize_lims_quantitationMethod();
#exquant01.reset_lims_quantitationMethod(quantitation_method_id_I='140521-v02');
#exquant01.import_quantitationMethod_add('140521-v02','data/tests/analysis_quantification/150805_140521_Quantification_chemoCLim01_QMethod01.csv');
#exquant01.execute_quantitationMethodUpdate(quant_method_ids_I = ['140521-v02']);
#exquant01.export_quantitationMethod_js('140521-v02');

##make the quantitation methods table
#from SBaaS_quantification.stage01_quantification_peakInformation_execute import stage01_quantification_peakInformation_execute
#expeak01 = stage01_quantification_peakInformation_execute(session,engine,pg_settings.datadir_settings);
#expeak01.drop_dataStage01_quantification_peakInformation();
#expeak01.initialize_dataStage01_quantification_peakInformation();
#expeak01.reset_dataStage01_quantification_peakInformation();
#expeak01.execute_analyzePeakInformation('chemoCLim01',
#                            sample_names_I = [],
#                            sample_types_I = ['Quality Control'],
#                            acquisition_date_and_time_I=[]);
#expeak01.export_boxAndWhiskersPlot_peakInformation_matplot('chemoCLim01',
#                            peakInfo_parameter_I = ['height','retention_time'],
#                            component_names_I=[],
#                            filename_O = 'tmp',
#                            figure_format_O = '.png');
#expeak01.export_boxAndWhiskersPlot_peakInformation_js('chemoCLim01',
#                            peakInfo_parameter_I = ['height','retention_time'],
#                            component_names_I=[],
#                            data_dir_I = 'tmp');
#expeak01.execute_analyzePeakResolution('chemoCLim01',
#                            sample_names_I = [],
#                            sample_types_I = ['Quality Control'],
#                            component_name_pairs_I=[['g1p.g1p_1.Light','g6p.g6p_1.Light'],
#                                                    ['r5p.r5p_1.Light','ru5p-D.ru5p-D_1.Light']],
#                            acquisition_date_and_time_I=[]);
#expeak01.export_boxAndWhiskersPlot_peakResolution_matplot('chemoCLim01',
#                            component_name_pairs_I=[],
#                            peakInfo_parameter_I = ['rt_dif','resolution'],
#                            filename_O = 'tmp',
#                            figure_format_O = '.png');
#expeak01.export_boxAndWhiskersPlot_peakResolution_js('chemoCLim01',
#                            component_name_pairs_I=[],
#                            peakInfo_parameter_I = ['rt_dif','resolution'],
#                            data_dir_I = 'tmp');

#make the QC methods tables
from SBaaS_quantification.stage01_quantification_QCs_execute import stage01_quantification_QCs_execute
exqcs01 = stage01_quantification_QCs_execute(session,engine,pg_settings.datadir_settings);
#exqcs01.drop_dataStage01_quantification_QCs();
#exqcs01.initialize_dataStage01_quantification_QCs();
#exqcs01.reset_dataStage01_quantification_allQCs('CollinsLab_MousePlasma01');
#exqcs01.execute_analyzeQCs('CollinsLab_MousePlasma01');
#exqcs01.export_checkCV_QCs_csv('CollinsLab_MousePlasma01');
#exqcs01.execute_LLOQAndULOQ('CollinsLab_MousePlasma01'); #broken query get_LLOQandULOQ
#exqcs01.export_checkLLOQAndULOQ_csv('CollinsLab_MousePlasma01'); #broken query get_LLOQandULOQ
#exqcs01.export_checkISMatch_csv('CollinsLab_MousePlasma01');
#exqcs01.execute_analyzeDilutions('CollinsLab_MousePlasma01');
#exqcs01.export_checkCV_dilutions_csv('CollinsLab_MousePlasma01');

## normalize samples to biomass
#from SBaaS_quantification.stage01_quantification_normalized_execute import stage01_quantification_normalized_execute
#exnorm01 = stage01_quantification_normalized_execute(session,engine,pg_settings.datadir_settings);
#exnorm01.drop_dataStage01_quantification_normalized();
#exnorm01.initialize_dataStage01_quantification_normalized();
#exnorm01.reset_dataStage01_quantification_normalized('chemoCLim01');
## normalize samples to the measured biomass of the experiment
#exnorm01.execute_normalizeSamples2Biomass(
#        'chemoCLim01','MG1655','ODspecificTotalCellVolume_Volkmer2011',
#        sample_names_I = [],
#        component_names_I = []);
#exnorm01.reset_dataStage01_quantification_averages('chemoCLim01');
## calculate replicates using the formula broth,i - ave(filtrate) for specific samples
#exnorm01.execute_analyzeAverages('chemoCLim01');
#exnorm01.export_checkCVAndExtracelluar_averages_csv('chemoCLim01','checkCVAndExtracellular_averages.csv',cv_threshold_I=40.0,extracellular_threshold_I = 60.0);
#exnorm01.export_dataStage01NormalizedAndAverages_js('chemoCLim01',
#        sample_name_abbreviations_I=[],
#        sample_names_I=[],
#        component_names_I=[],
#        cv_threshold_I=40,extracellular_threshold_I=80,
#        data_dir_I='tmp');
## remove high filtrate compounds by setting used to "false"
#exnorm01.update_setUsed2FalseAllFiltrate_experimentID_dataStage01QuantificationNormalized('chemoCLim01')
## remove selected samples with high variance by setting used to "false"
#exnorm01.update_setUsed2False_experimentIDAndSampleName_dataStage01QuantificationNormalized('chemoCLim01',
#        sample_names_I=[]
#    );

##make the replicates methods table
#from SBaaS_quantification.stage01_quantification_replicates_execute import stage01_quantification_replicates_execute
#exreps01 = stage01_quantification_replicates_execute(session,engine,pg_settings.datadir_settings);
#exreps01.drop_dataStage01_quantification_replicates();
#exreps01.initialize_dataStage01_quantification_replicates();
#exreps01.reset_dataStage01_quantification_replicates('chemoCLim01');
## calculate replicates using the formula broth,i - ave(filtrate) for specific samples
#exreps01.execute_analyzeReplicates('chemoCLim01');
#exreps01.export_dataStage01Replicates_csv('chemoCLim01','replicates.csv');
#exreps01.reset_dataStage01_quantification_replicatesMI('chemoCLim01');
## calculate missing values using a missing value imputation algorithm (AMELIA2)
#exreps01.execute_calculateMissingValues_replicates('chemoCLim01');
## estimate missing components based on the lloq of the calibration curves
## requires QC table lloqAndUloq
#exreps01.execute_calculateMissingComponents_replicates('chemoCLim01',
#        'MG1655','gDW2OD_lab');
#exreps01.export_dataStage01ReplicatesMI_csv('chemoCLim01','replicatesMI.csv');

##make the physiologicalRatios methods table
#from SBaaS_quantification.stage01_quantification_physiologicalRatios_execute import stage01_quantification_physiologicalRatios_execute
#exphysratio01 = stage01_quantification_physiologicalRatios_execute(session,engine,pg_settings.datadir_settings);
#exphysratio01.drop_dataStage01_quantification_physiologicalRatios();
#exphysratio01.initialize_dataStage01_quantification_physiologicalRatios();
#exphysratio01.reset_dataStage01_quantification_physiologicalRatios('chemoCLim01');
#exphysratio01.execute_physiologicalRatios_replicates('chemoCLim01');
#exphysratio01.execute_physiologicalRatios_averages('chemoCLim01');
#exphysratio01.export_boxAndWhiskersPlot_physiologicalRatios_matplot('chemoCLim01');
#exphysratio01.export_scatterLinePlot_physiologicalRatios_matplot('chemoCLim01');
##TODO:
##1. make seperate table to analyze the line of best fit for the numerator vs. denominator
##2. make seperate export method to visualize the numerator vs. denonimator
##notes: template quantificationMethod
#exphysratio01.export_dataStage01QuantificationPhysiologicalRatios_js('chemoCLim01',
#                sample_name_abbreviations_I=[],
#                ratio_ids_I=[],
#                data_dir_I = 'tmp');

##make the averages methods table
#from SBaaS_quantification.stage01_quantification_averages_execute import stage01_quantification_averages_execute
#exave01 = stage01_quantification_averages_execute(session,engine,pg_settings.datadir_settings);
#exave01.drop_dataStage01_quantification_averagesMI();
#exave01.initialize_dataStage01_quantification_averagesMI();
#exave01.reset_dataStage01_quantification_averagesMI('chemoCLim01');
#exave01.execute_calculateAverages_replicates('chemoCLim01');
#exave01.export_dataStage01AveragesMI_json('chemoCLim01', 'OxicWtGlcDil0p25', '0', 'dataStage01AveragesMI.json');
#exave01.execute_calculateGeoAverages_replicates('chemoCLim01');
#exave01.export_dataStage01AveragesMIgeo_json('chemoCLim01', 'OxicWtGlcDil0p25', '0', 'dataStage01AveragesMIgeo.json');

##make the quantitation methods table
#from SBaaS_quantification.stage01_quantification_QMethod_execute import stage01_quantification_QMethod_execute
#exquant01 = stage01_quantification_QMethod_execute(session,engine,pg_settings.datadir_settings);
#exquant01.drop_dataStage01_quantification_QMethod();
#exquant01.initialize_dataStage01_quantification_QMethod();
#exquant01.reset_dataStage01_quantification_QMethod();