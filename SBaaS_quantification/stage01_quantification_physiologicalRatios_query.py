#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_quantification_physiologicalRatios_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_quantification_physiologicalRatios_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_physiologicalRatios_averages':data_stage01_quantification_physiologicalRatios_averages,
'data_stage01_quantification_physiologicalRatios_replicates':data_stage01_quantification_physiologicalRatios_replicates,
                        };
        self.set_supportedTables(tables_supported);

    # Query sample names from data_stage01_quantification_physiologicalRatios_replicates
    def get_sampleNameAbbreviations_experimentID_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I,exp_type_I=4):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.like(sample_description.sample_name_short),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleNameAbbreviationAndRatioIDAndTimePoint_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I,sample_name_abbreviation_I,physiologicalratio_id_I,time_point_I,exp_type_I=4):
        '''Querry sample names that are used from the experiment by sample name abbreviation and sample description'''
        try:
            sample_names = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.sample_name_short).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.like(sample_description.sample_name_short),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short).order_by(
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.asc()).all();
            sample_names_short_O = [];
            for sn in sample_names: sample_names_short_O.append(sn.sample_name_short);
            return sample_names_short_O;
        except SQLAlchemyError as e:
            print(e);
    # Query time points from data_stage01_quantification_physiologicalRatios_replicates
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_short.like(data_stage01_quantification_physiologicalRatios_replicates.sample_name_short),
                    sample_description.time_point.like(data_stage01_quantification_physiologicalRatios_replicates.time_point),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point).order_by(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentID_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.time_point).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point).order_by(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndRatioID_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I,physiologicalratio_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.time_point).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point).order_by(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_physiologicalRatios_replicates
    def get_ratio_experimentIDAndSampleNameShortAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(self, experiment_id_I, sample_name_short_I, time_point_I, physiologicalratio_id_I):
        """Query calculated ratios"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_value).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).all();
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                ratio_O = data[0][0];
            else: 
                ratio_O = None;
            return ratio_O;
        except SQLAlchemyError as e:
            print(e);
    def get_ratios_experimentIDAndSampleNameAbbreviationAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, physiologicalratio_id_I,exp_type_I=4):
        """Query calculated ratios"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_value).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.like(sample_description.sample_name_short),
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_value).all();
            ratios_O = [];
            for d in data:
                ratios_O.append(d[0]);
            return ratios_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleNameAbbreviationAndTimePointAndRatioID_dataStage01PhysiologicalRatiosReplicates(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, physiologicalratio_id_I,exp_type_I=4):
        """Query rows from data_stage01_physiologicalRatios_replicates"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_replicates).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.like(sample_description.sample_name_short),
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).all();
            rows_O = [];
            if data:
                for d in data:
                    rows_O.append({'experiment_id':d.experiment_id,
                        'sample_name_short':d.sample_name_short,
                        'time_point':d.time_point,
                        'physiologicalratio_id':d.physiologicalratio_id,
                        'physiologicalratio_name':d.physiologicalratio_name,
                        'physiologicalratio_value':d.physiologicalratio_value,
                        'physiologicalratio_description':d.physiologicalratio_description,
                        'used_':d.used_,
                        'comment_':d.comment_});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleNameShortAndTimePoint_dataStage01PhysiologicalRatiosReplicates(self, experiment_id_I, sample_name_short_I, time_point_I):
        """Query rows from data_stage01_physiologicalRatios_replicates"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_replicates).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).all();
            rows_O = [];
            if data:
                for d in data:
                    rows_O.append({'experiment_id':d.experiment_id,
                        'sample_name_short':d.sample_name_short,
                        'time_point':d.time_point,
                        'physiologicalratio_id':d.physiologicalratio_id,
                        'physiologicalratio_name':d.physiologicalratio_name,
                        'physiologicalratio_value':d.physiologicalratio_value,
                        'physiologicalratio_description':d.physiologicalratio_description,
                        'used_':d.used_,
                        'comment_':d.comment_});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # Query ratio_id information from data_stage01_quantificaton_physiologicalRatios_replicates
    def get_ratioIDs_experimentIDAndTimePoint_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I,time_point_I):
        '''Query physiologicalRatio_ids that are used from the experiment by time_point'''
        try:
            ratios = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_name,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_description).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_name,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_description).order_by(
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.asc()).all();
            ratios_O = {};
            for r in ratios:
                ratios_O[r.physiologicalratio_id] = {'name':r.physiologicalratio_name,
                                                     'description':r.physiologicalratio_description};
            return ratios_O;
        except SQLAlchemyError as e:
            print(e);
    def get_ratioIDs_experimentID_dataStage01PhysiologicalRatiosReplicates(self,experiment_id_I):
        '''Query physiologicalRatio_ids that are used from the experiment'''
        try:
            ratios = self.session.query(data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_name,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_description).filter(
                    data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_replicates.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_name,
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_description).order_by(
                    data_stage01_quantification_physiologicalRatios_replicates.physiologicalratio_id.asc()).all();
            ratios_O = {};
            for r in ratios:
                ratios_O[r.physiologicalratio_id] = {'name':r.physiologicalratio_name,
                                                     'description':r.physiologicalratio_description};
            return ratios_O;
        except SQLAlchemyError as e:
            print(e);
    
    # Query time points from data_stage01_quantification_physiologicalRatios_averages
    def get_timePoint_experimentID_dataStage01PhysiologicalRatiosAverages(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_physiologicalRatios_averages.time_point).filter(
                    data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_averages.time_point).order_by(
                    data_stage01_quantification_physiologicalRatios_averages.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query sample names from data_stage01_quantification_physiologicalRatios_averages
    def get_sampleNameAbbreviations_experimentIDAndTimePoint_dataStage01PhysiologicalRatiosAverages(self,experiment_id_I,time_point_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation).filter(
                    data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation).order_by(
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndTimePointAndRatioID_dataStage01PhysiologicalRatiosAverages(self,experiment_id_I,time_point_I,physiologicalratio_id_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation).filter(
                    data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_averages.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation).order_by(
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_physiologicalRatios_averages:
    def get_data_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(self, experiment_id_I,time_point_I,sample_name_abbreviation_I):
        """get data from experiment ID"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_averages).filter(
                    data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_physiologicalRatios_averages.used_.is_(True)).all();
            data_O = [];
            for d in data: 
                data_1 = {'experiment_id':d.experiment_id,
                'sample_name_abbreviation':d.sample_name_abbreviation,
                'time_point':d.time_point,
                'physiologicalratio_id':d.physiologicalratio_id,
                'physiologicalratio_name':d.physiologicalratio_name,
                'physiologicalratio_value_ave':d.physiologicalratio_value_ave,
                'physiologicalratio_value_cv':d.physiologicalratio_value_cv,
                'physiologicalratio_value_lb':d.physiologicalratio_value_lb,
                'physiologicalratio_value_ub':d.physiologicalratio_value_ub,
                'physiologicalratio_description':d.physiologicalratio_description,
                'used_':d.used_,
                'comment_':d.comment_};
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_data_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(self, experiment_id_I,time_point_I,physiologicalratio_id_I,sample_name_abbreviation_I):
        """get data from experiment ID"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_averages).filter(
                    data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_averages.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_physiologicalRatios_averages.used_.is_(True)).all();
            data_O = {};
            if data: 
                data_O = {'experiment_id':data[0].experiment_id,
                'sample_name_abbreviation':data[0].sample_name_abbreviation,
                'time_point':data[0].time_point,
                'physiologicalratio_id':data[0].physiologicalratio_id,
                'physiologicalratio_name':data[0].physiologicalratio_name,
                'physiologicalratio_value_ave':data[0].physiologicalratio_value_ave,
                'physiologicalratio_value_cv':data[0].physiologicalratio_value_cv,
                'physiologicalratio_value_lb':data[0].physiologicalratio_value_lb,
                'physiologicalratio_value_ub':data[0].physiologicalratio_value_ub,
                'physiologicalratio_description':data[0].physiologicalratio_description,
                'used_':data[0].used_,
                'comment_':data[0].comment_};
            return data_O;
        except SQLAlchemyError as e:
            print(e);    
    def get_ratio_experimentIDAndTimePointAndRatioIDAndSampleNameAbbreviation_dataStage01PhysiologicalRatiosAverages(self, experiment_id_I,time_point_I,physiologicalratio_id_I,sample_name_abbreviation_I):
        """get data from experiment ID"""
        try:
            data = self.session.query(data_stage01_quantification_physiologicalRatios_averages).filter(
                    data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.time_point.like(time_point_I),
                    data_stage01_quantification_physiologicalRatios_averages.physiologicalratio_id.like(physiologicalratio_id_I),
                    data_stage01_quantification_physiologicalRatios_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_physiologicalRatios_averages.used_.is_(True)).all();
            ratio_O = None;
            if data: 
                ratio_O = data[0].physiologicalratio_value_ave;
            return ratio_O;
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_quantification_physiologicalRatios(self):
        try:
            data_stage01_quantification_physiologicalRatios_replicates.__table__.drop(self.engine,True);
            data_stage01_quantification_physiologicalRatios_averages.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_physiologicalRatios(self):
        try:
            data_stage01_quantification_physiologicalRatios_replicates.__table__.create(self.engine,True);
            data_stage01_quantification_physiologicalRatios_averages.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_quantification_physiologicalRatios(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_physiologicalRatios_replicates).filter(data_stage01_quantification_physiologicalRatios_replicates.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_physiologicalRatios_averages).filter(data_stage01_quantification_physiologicalRatios_averages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
            
    def add_dataStage01QuantificationPhysiologicalRatiosReplicates(self, data_I):
        '''add rows of data_stage01_quantification_physiologicalRatios_replicates'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_quantification_physiologicalRatios_replicates(d
                        #d['experiment_id_I'],
                        #d['sample_name_short_I'],
                        ##d['sample_name_abbreviation_I'],
                        #d['time_point_I'],
                        ##d['time_point_units_I'],
                        #d['physiologicalratio_id_I'],
                        #d['physiologicalratio_name_I'],
                        #d['physiologicalratio_value_I'],
                        #d['physiologicalratio_description_I'],
                        #d['used__I'],
                        #d['comment__I']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01QuantificationPhysiologicalRatiosReplicates(self,data_I):
        '''update rows of data_stage02_quantification_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_quantification_physiologicalRatios_replicates).filter(
                           data_stage01_quantification_physiologicalRatios_replicates.id==d['id']).update(
                            {'experiment_id_I':d['experiment_id_I'],
                            'sample_name_short_I':d['sample_name_short_I'],
                            #'sample_name_abbreviation_I':d['#sample_name_abbreviation_I'],
                            'time_point_I':d['time_point_I'],
                            #'time_point_units_I':d['#time_point_units_I'],
                            'physiologicalratio_id_I':d['physiologicalratio_id_I'],
                            'physiologicalratio_name_I':d['physiologicalratio_name_I'],
                            'physiologicalratio_value_I':d['physiologicalratio_value_I'],
                            'physiologicalratio_description_I':d['physiologicalratio_description_I'],
                            'used__I':d['used__I'],
                            'comment__I':d['comment__I']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();