#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_quantification_averages_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_quantification_averages_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_averagesmi':data_stage01_quantification_averagesMI,
'data_stage01_quantification_averagesmigeo':data_stage01_quantification_averagesMIgeo,
                        };
        self.set_supportedTables(tables_supported);

    # Query data from data_stage01_quantification_averagesMI:
    def get_concentrations_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01AveragesMI(self, experiment_id_I, sample_name_abbreviation_I, time_point_I):
        """get data from experiment ID, sample name abbreviation, and time point"""
        try:
            data = self.session.query(data_stage01_quantification_averagesMI.calculated_concentration_average,
                    data_stage01_quantification_averagesMI.calculated_concentration_cv,
                    data_stage01_quantification_averagesMI.calculated_concentration_units,
                    data_stage01_quantification_averagesMI.component_group_name).filter(
                    data_stage01_quantification_averagesMI.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMI.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_averagesMI.time_point.like(time_point_I),
                    data_stage01_quantification_averagesMI.used_.is_(True)).all();
            data_O = {};
            for d in data: 
                data_O[d.component_group_name] = {'concentration':d.calculated_concentration_average,
                      'concentration_cv':d.calculated_concentration_cv,
                      'concentration_units':d.calculated_concentration_units};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    
    # Query sample names from data_stage01_quantification_averagesMIgeo:
    def get_sampleNameAbbreviations_experimentIDAndTimePointAndComponentName_dataStage01AveragesMIgeo(self,experiment_id_I,time_point_I,component_name_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_averagesMIgeo.sample_name_abbreviation).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.time_point.like(time_point_I),
                    data_stage01_quantification_averagesMIgeo.component_name.like(component_name_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).group_by(
                    data_stage01_quantification_averagesMIgeo.sample_name_abbreviation).order_by(
                    data_stage01_quantification_averagesMIgeo.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_averagesMIgeo:
    def get_concentrations_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01AveragesMIgeo(self, experiment_id_I, sample_name_abbreviation_I, time_point_I):
        """get data from experiment ID, sample name abbreviation, and time point"""
        try:
            data = self.session.query(data_stage01_quantification_averagesMIgeo.calculated_concentration_average,
                    data_stage01_quantification_averagesMIgeo.calculated_concentration_var,
                    data_stage01_quantification_averagesMIgeo.calculated_concentration_lb,
                    data_stage01_quantification_averagesMIgeo.calculated_concentration_ub,
                    data_stage01_quantification_averagesMIgeo.calculated_concentration_units,
                    data_stage01_quantification_averagesMIgeo.component_group_name).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_averagesMIgeo.time_point.like(time_point_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).all();
            data_O = {};
            for d in data: 
                data_O[d.component_group_name] = {'concentration':d.calculated_concentration_average,
                      'concentration_var':d.calculated_concentration_var,
                      'concentration_lb':d.calculated_concentration_lb,
                      'concentration_ub':d.calculated_concentration_ub,
                      'concentration_units':d.calculated_concentration_units};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndSampleNameAbbreviationAndTimePointAndComponentName_dataStage01AveragesMIgeo(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, component_name_I):
        """get data from experiment ID, sample name abbreviation, and time point"""
        try:
            data = self.session.query(data_stage01_quantification_averagesMIgeo).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_averagesMIgeo.component_name.like(component_name_I),
                    data_stage01_quantification_averagesMIgeo.time_point.like(time_point_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).all();
            data_O = {};
            if data: 
                data_O={"experiment_id":data[0].experiment_id,
                "sample_name_abbreviation":data[0].sample_name_abbreviation,
                "time_point":data[0].time_point,
                "component_group_name":data[0].component_group_name,
                "component_name":data[0].component_name,
                "calculated_concentration_average":data[0].calculated_concentration_average,
                "calculated_concentration_var":data[0].calculated_concentration_var,
                "calculated_concentration_lb":data[0].calculated_concentration_lb,
                "calculated_concentration_ub":data[0].calculated_concentration_ub,
                "calculated_concentration_units":data[0].calculated_concentration_units,
                "used_":data[0].used_};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # Query time points from data_stage01_quantification_averagesMIgeo
    def get_timePoint_experimentID_dataStage01AveragesMIgeo(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_averagesMIgeo.time_point).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).group_by(
                    data_stage01_quantification_averagesMIgeo.time_point).order_by(
                    data_stage01_quantification_averagesMIgeo.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndComponentName_dataStage01AveragesMIgeo(self,experiment_id_I,component_name_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_averagesMIgeo.time_point).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.component_name.like(component_name_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).group_by(
                    data_stage01_quantification_averagesMIgeo.time_point).order_by(
                    data_stage01_quantification_averagesMIgeo.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query component names from data_stage01_quantification_averagesMIgeo:
    def get_componentNames_experimentIDAndTimePoint_dataStage01AveragesMIgeo(self,experiment_id_I,time_point_I):
        '''Querry component Names that are used from the experiment'''
        try:
            component_names = self.session.query(data_stage01_quantification_averagesMIgeo.component_name).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.time_point.like(time_point_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).group_by(
                    data_stage01_quantification_averagesMIgeo.component_name).order_by(
                    data_stage01_quantification_averagesMIgeo.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentNames_experimentID_dataStage01AveragesMIgeo(self,experiment_id_I):
        '''Querry component Names that are used from the experiment'''
        try:
            component_names = self.session.query(data_stage01_quantification_averagesMIgeo.component_name).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).group_by(
                    data_stage01_quantification_averagesMIgeo.component_name).order_by(
                    data_stage01_quantification_averagesMIgeo.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_quantification_averagesMI(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_averagesMI).filter(data_stage01_quantification_averagesMI.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_averagesMIgeo).filter(data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_quantification_averagesMI(self):
        try:
            data_stage01_quantification_averagesMI.__table__.drop(self.engine,True);
            data_stage01_quantification_averagesMIgeo.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_averagesMI(self):
        try:
            data_stage01_quantification_averagesMI.__table__.create(self.engine,True);
            data_stage01_quantification_averagesMIgeo.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_averagesMIgeo:
    def get_rows_experimentID_dataStage01AveragesMIgeo(self, experiment_id_I):
        """get data from experiment ID"""
        try:
            data = self.session.query(data_stage01_quantification_averagesMIgeo).filter(
                    data_stage01_quantification_averagesMIgeo.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averagesMIgeo.used_.is_(True)).all();
            data_O = [];
            for d in data: 
                data_O.append({"experiment_id":d.experiment_id,
                    "sample_name_abbreviation":d.sample_name_abbreviation,
                    "time_point":d.time_point,
                    "component_group_name":d.component_group_name,
                    "component_name":d.component_name,
                    "n_replicates":d.n_replicates,
                    "calculated_concentration_average":d.calculated_concentration_average,
                    "calculated_concentration_var":d.calculated_concentration_var,
                    "calculated_concentration_lb":d.calculated_concentration_lb,
                    "calculated_concentration_ub":d.calculated_concentration_ub,
                    "calculated_concentration_units":d.calculated_concentration_units,
                    "used_":d.used_})
            return data_O;
        except SQLAlchemyError as e:
            print(e);