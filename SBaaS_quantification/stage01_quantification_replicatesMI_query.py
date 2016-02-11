#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
from .stage01_quantification_replicatesMI_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_quantification_replicatesMI_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_replicatesmi':data_stage01_quantification_replicatesMI,
                        };
        self.set_supportedTables(tables_supported);

    # Query sample names from data_stage01_quantification_replicatesMI:
    def get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndComponentNameAndTimePoint_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_abbreviation_I,component_name_I,time_point_I,exp_type_I=4):
        '''Querry sample names that are used from the experiment by sample name abbreviation and sample description'''
        try:
            sample_names = self.session.query(data_stage01_quantification_replicatesMI.sample_name_short).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.sample_name_short).order_by(
                    data_stage01_quantification_replicatesMI.sample_name_short.asc()).all();
            sample_names_short_O = [];
            for sn in sample_names: sample_names_short_O.append(sn.sample_name_short);
            return sample_names_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_SampleNameShort_experimentID_dataStage01ReplicatesMI(self,experiment_id_I):
        '''Querry sample names short that are used from the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_replicatesMI.sample_name_short).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.sample_name_short).order_by(
                    data_stage01_quantification_replicatesMI.sample_name_short.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentID_dataStage01ReplicatesMI(self,experiment_id_I,exp_type_I=4):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndTimePointAndComponentName_dataStage01ReplicatesMI(self,experiment_id_I,time_point_I,component_name_I,exp_type_I=4):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query component names from data_stage01_quantification_replicatesMI:
    def get_componentNames_experimentID_dataStage01ReplicatesMI(self,experiment_id_I):
        '''Querry component Names that are used from the experiment'''
        try:
            component_names = self.session.query(data_stage01_quantification_replicatesMI.component_name).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.component_name).order_by(
                    data_stage01_quantification_replicatesMI.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentNames_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry component names that are used and not internal standards from
        the experiment and sample abbreviation'''
        try:
            component_names = self.session.query(data_stage01_quantification_replicatesMI.component_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),   
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),            
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.component_name).order_by(
                    data_stage01_quantification_replicatesMI.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentNames_experimentIDAndTimePoint_dataStage01ReplicatesMI(self,experiment_id_I,time_point_I):
        '''Querry component names that are used and not internal standards from
        the experiment and time point'''
        try:
            component_names = self.session.query(data_stage01_quantification_replicatesMI.component_name).filter(
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),            
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.component_name).order_by(
                    data_stage01_quantification_replicatesMI.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query time points from data_stage01_quantification_replicatesMI
    def get_timePoint_experimentID_dataStage01ReplicatesMI(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_replicatesMI.time_point).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.time_point).order_by(
                    data_stage01_quantification_replicatesMI.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndSampleNameShort_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_short_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_replicatesMI.time_point).filter(
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.time_point).order_by(
                    data_stage01_quantification_replicatesMI.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_replicatesMI.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(data_stage01_quantification_replicatesMI.sample_name_short),
                    sample_description.time_point.like(data_stage01_quantification_replicatesMI.time_point),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.time_point).order_by(
                    data_stage01_quantification_replicatesMI.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndComponentName_dataStage01ReplicatesMI(self,experiment_id_I,component_name_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_replicatesMI.time_point).filter(
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.time_point).order_by(
                    data_stage01_quantification_replicatesMI.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_replicatesMI:
    def get_data_experimentID_dataStage01ReplicatesMI(self, experiment_id_I):
        """get data from experiment ID"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.component_group_name).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['component_group_name'] = d.component_group_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_calculatedConcentrations_experimentIDAndSampleNameAbbreviationAndTimePointAndComponentName_dataStage01ReplicatesMI(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, component_name_I,exp_type_I=4):
        """Query calculatedConcentrations"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration).all();
            ratios_O = [];
            for d in data:
                ratios_O.append(d[0]);
            return ratios_O;
        except SQLAlchemyError as e:
            print(e);
    def get_calculatedConcentration_experimentIDAndSampleNameShortAndTimePointAndComponentName_dataStage01ReplicatesMI(self, experiment_id_I, sample_name_short_I, time_point_I, component_name_I):
        """Query calculated concentrations"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).all();
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                calc_conc_O = data[0];
            else: 
                calc_conc_O = None;
            return calc_conc_O;
        except SQLAlchemyError as e:
            print(e);
    def get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentName_dataStage01ReplicatesMI(self, experiment_id_I, sample_name_short_I, time_point_I, component_name_I):
        """Query calculated concentrations"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).all();
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                conc_O = data[0][0];
                conc_units_O = data[0][1];
            else: 
                conc_O = None;
                conc_units_O = None;
            return conc_O, conc_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentGroupName_dataStage01ReplicatesMI(self, experiment_id_I, sample_name_short_I, time_point_I, component_group_name_I):
        """Query calculated concentrations"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_group_name.like(component_group_name_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).all();
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                conc_O = data[0][0];
                conc_units_O = data[0][1];
            else: 
                conc_O = None;
                conc_units_O = None;
            return conc_O, conc_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01ReplicatesMI(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,exp_type_I=4):
        '''Querry sample names that are used from the experiment by sample name abbreviation and sample description'''
        #Not tested
        try:
            sample_names = self.session.query(data_stage01_quantification_replicatesMI.sample_name_short).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(sample.sample_id),
                    sample.sample_name.like(experiment.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.sample_name_short).order_by(
                    data_stage01_quantification_replicatesMI.sample_name_short.asc()).all();
            sample_names_short_O = [];
            for sn in sample_names: sample_names_short_O.append(sn.sample_name_short);
            return sample_names_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndTimePointAndSampleNameShortAndUnits_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,sample_name_short_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(sample.sample_id),
                    sample.sample_name.like(experiment.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndTimePointAndUnits_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(sample.sample_id),
                    sample.sample_name.like(experiment.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RExpressionData_experimentIDAndTimePointAndUnits_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(sample.sample_id),
                    sample.sample_name.like(experiment.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RExpressionData_experimentIDAndTimePointAndUnitsAndSampleNameShort_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,sample_name_short_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(sample.sample_id),
                    sample.sample_name.like(experiment.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_RDataList_experimentIDAndTimePointAndUnitsAndComponentNamesAndSampleNameAbbreviation_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,concentration_units_I,component_name_I,sample_name_abbreviation_I,exp_type_I=4):
        """get data from experiment ID"""
        #Tested
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.component_name.like(component_name_I),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.like(concentration_units_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_description.sample_name_short),
                    sample_description.sample_id.like(sample.sample_id),
                    sample.sample_name.like(experiment.sample_name),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.experiment_id,
                    sample_description.sample_name_abbreviation,
                    sample_description.sample_replicate,
                    data_stage01_quantification_replicatesMI.sample_name_short,
                    data_stage01_quantification_replicatesMI.time_point,
                    data_stage01_quantification_replicatesMI.component_group_name,
                    data_stage01_quantification_replicatesMI.component_name,
                    data_stage01_quantification_replicatesMI.calculated_concentration,
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).all();
            data_O = [];
            concentrations_O = [];
            for d in data: 
                concentrations_O.append(d.calculated_concentration);
                data_1 = {};
                data_1['experiment_id'] = d.experiment_id;
                data_1['sample_name_abbreviation'] = d.sample_name_abbreviation;
                data_1['sample_replicate'] = d.sample_replicate;
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['time_point'] = d.time_point;
                data_1['component_group_name'] = d.component_group_name;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_1['calculated_concentration_units'] = d.calculated_concentration_units;
                data_O.append(data_1);
            return data_O,concentrations_O;
        except SQLAlchemyError as e:
            print(e);
    # Query concentration_units from data_stage01_quantification_replicatesMI:    
    def get_concentrationUnits_experimentIDAndTimePoint_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).order_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_concentrationUnits_experimentIDAndTimePointAndSampleNameShort_dataStage01ReplicatesMI(self, experiment_id_I,time_point_I,sample_name_short_I):
        """get concentration_units from experiment ID and time point"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.time_point.like(time_point_I),
                    data_stage01_quantification_replicatesMI.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).order_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_concentrationUnits_experimentID_dataStage01ReplicatesMI(self, experiment_id_I):
        """get concentration_units from experiment ID"""
        try:
            data = self.session.query(data_stage01_quantification_replicatesMI.calculated_concentration_units).filter(
                    data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicatesMI.used_.is_(True)).group_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units).order_by(
                    data_stage01_quantification_replicatesMI.calculated_concentration_units.asc()).all();
            units_O = [];
            for d in data: 
                units_O.append(d[0]);
            return units_O;
        except SQLAlchemyError as e:
            print(e);


    def reset_dataStage01_quantification_replicatesMI(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_replicatesMI).filter(data_stage01_quantification_replicatesMI.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_quantification_replicatesMI(self):
        try:
            data_stage01_quantification_replicatesMI.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_replicatesMI(self):
        try:
            data_stage01_quantification_replicatesMI.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01QuantificationReplicatesMI(self, data_I):
        '''add rows of data_stage01_quantification_replicatesMI'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_quantification_replicatesMI(
                        d['experiment_id_I'],
                        d['sample_name_short_I'],
                        #d['sample_name_abbreviation_I'],
                        d['time_point_I '],
                        #d['time_point_units_I'],
                        d['component_group_name_I'],
                        d['component_name_I'],
                        d['imputation_method_I'],
                        d['imputation_options_I'],
                        d['calculated_concentration_I'],
                        d['calculated_concentration_units_I'],
                        d['used__I'],
                        d['comment__I']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01QuantificationReplicatesMI(self,data_I):
        '''update rows of data_stage02_quantification_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_quantification_replicatesMI).filter(
                           data_stage01_quantification_replicatesMI.id==d['id']).update(
                            {'experiment_id_I':d['experiment_id_I'],
                            'sample_name_short_I':d['sample_name_short_I'],
                            #'sample_name_abbreviation_I':d['#sample_name_abbreviation_I'],
                            'time_point_I ':d['time_point_I '],
                            #'time_point_units_I':d['#time_point_units_I'],
                            'component_group_name_I':d['component_group_name_I'],
                            'component_name_I':d['component_name_I'],
                            'imputation_method_I':d['imputation_method_I'],
                            'imputation_options_I':d['imputation_options_I'],
                            'calculated_concentration_I':d['calculated_concentration_I'],
                            'calculated_concentration_units_I':d['calculated_concentration_units_I'],
                            'used__I':d['used__I'],
                            'comment__I':d['comment__I']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();