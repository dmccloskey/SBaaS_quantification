from .stage01_quantification_peakInformation_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_quantification_peakInformation_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_peakInformation':data_stage01_quantification_peakInformation,
'data_stage01_quantification_peakResolution':data_stage01_quantification_peakResolution,
                        };
        self.set_supportedTables(tables_supported);
    # Query peakInfo_parameter from data_stage01_quantificaton_peakInformation
    def get_peakInfoParameter_experimentID_dataStage01PeakInformation(self,experiment_id_I):
        '''Query component_names that are used for the experiment'''
        try:
            names = self.session.query(data_stage01_quantification_peakInformation.peakInfo_parameter).filter(
                    data_stage01_quantification_peakInformation.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakInformation.used_.is_(True)).group_by(
                    data_stage01_quantification_peakInformation.component_name).order_by(
                    data_stage01_quantification_peakInformation.component_name.asc()).all();
            names_O = [];
            for n in names:
                names_O.append(n.peakInfo_parameter);
            return names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_peakInformation
    def get_row_experimentIDAndComponentName_dataStage01PeakInformation(self, experiment_id_I, component_name_I):
        """Query rows"""
        try:
            data = self.session.query(data_stage01_quantification_peakInformation).filter(
                    data_stage01_quantification_peakInformation.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakInformation.component_name.like(component_name_I),
                    data_stage01_quantification_peakInformation.used_.is_(True)).all();
            data_O = {};
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                for d in data:
                    data_O = {'experiment_id':d.experiment_id,
            'component_group_name':d.component_group_name,
            'component_name':d.component_name,
            'peakInfo_parameter':d.peakInfo_parameter,
            'peakInfo_ave':d.peakInfo_ave,
            'peakInfo_cv':d.peakInfo_cv,
            'peakInfo_lb':d.peakInfo_lb,
            'peakInfo_ub':d.peakInfo_ub,
            'peakInfo_units':d.peakInfo_units,
            'sample_names':d.sample_names,
            'sample_types':d.sample_types,
            'acqusition_date_and_times':d.acqusition_date_and_times,
            'peakInfo_data':d.peakInfo_data};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_experimentIDAndPeakInfoParameterComponentName_dataStage01PeakInformation(self, experiment_id_I, peakInfo_parameter_I, component_name_I):
        """Query rows"""
        try:
            data = self.session.query(data_stage01_quantification_peakInformation).filter(
                    data_stage01_quantification_peakInformation.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakInformation.component_name.like(component_name_I),
                    data_stage01_quantification_peakInformation.peakInfo_parameter.like(peakInfo_parameter_I),
                    data_stage01_quantification_peakInformation.used_.is_(True)).all();
            data_O = {};
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                for d in data:
                    data_O = {'experiment_id':d.experiment_id,
            'component_group_name':d.component_group_name,
            'component_name':d.component_name,
            'peakInfo_parameter':d.peakInfo_parameter,
            'peakInfo_ave':d.peakInfo_ave,
            'peakInfo_cv':d.peakInfo_cv,
            'peakInfo_lb':d.peakInfo_lb,
            'peakInfo_ub':d.peakInfo_ub,
            'peakInfo_units':d.peakInfo_units,
            'sample_names':d.sample_names,
            'sample_types':d.sample_types,
            'acqusition_date_and_times':d.acqusition_date_and_times,
            'peakInfo_data':d.peakInfo_data};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_analysisID_dataStage01PeakInformation(
        self,
        analysis_id_I=[],
        experiment_id_I=[],
        peakInfo_parameter_I=[],
        component_name_I=[],
        component_group_name_I=[],
        sample_name_abbreviation_I=[]
        ):
        """Query rows"""
        try:
            cmd = '''SELECT "data_stage01_quantification_peakInformation"."id",
                "data_stage01_quantification_peakInformation"."analysis_id",
                "data_stage01_quantification_peakInformation"."experiment_id",
                "data_stage01_quantification_peakInformation"."component_group_name",
                "data_stage01_quantification_peakInformation"."component_name",
                "data_stage01_quantification_peakInformation"."peakInfo_parameter",
                "data_stage01_quantification_peakInformation"."peakInfo_n",
                "data_stage01_quantification_peakInformation"."peakInfo_ave",
                "data_stage01_quantification_peakInformation"."peakInfo_cv",
                "data_stage01_quantification_peakInformation"."peakInfo_lb",
                "data_stage01_quantification_peakInformation"."peakInfo_ub",
                "data_stage01_quantification_peakInformation"."peakInfo_units",
                "data_stage01_quantification_peakInformation"."sample_names",
                "data_stage01_quantification_peakInformation"."sample_name_abbreviation",
                "data_stage01_quantification_peakInformation"."sample_types",
                "data_stage01_quantification_peakInformation"."acqusition_date_and_times",
                "data_stage01_quantification_peakInformation"."peakInfo_data",
                "data_stage01_quantification_peakInformation"."used_",
                "data_stage01_quantification_peakInformation"."comment_"
            '''
            cmd += '''
                FROM "data_stage01_quantification_peakInformation"
            '''
            cmd += '''WHERE "data_stage01_quantification_peakInformation"."used_" 
            '''
            if analysis_id_I:
                cmd_q = '''AND "data_stage01_quantification_peakInformation".analysis_id =ANY ('{%s}'::text[]) '''%(
                    self.convert_list2string(analysis_id_I));
                cmd+=cmd_q;
            if experiment_id_I:
                cmd_q = '''AND "data_stage01_quantification_peakInformation".experiment_id =ANY ('{%s}'::text[]) '''%(
                    self.convert_list2string(experiment_id_I));
                cmd+=cmd_q;
            if peakInfo_parameter_I:
                cmd_q = '''AND "data_stage01_quantification_peakInformation"."peakInfo_parameter" =ANY ('{%s}'::text[]) '''%(
                    self.convert_list2string(peakInfo_parameter_I));
                cmd+=cmd_q;
            #if sample_name_I:
            #    cmd_q = '''AND "data_stage01_quantification_peakInformation".sample_name =ANY ('{%s}'::text[]) '''%(
            #        self.convert_list2string(sample_name_I));
            #    cmd+=cmd_q;
            #if sample_id_I:
            #    cmd_q = '''AND "data_stage01_quantification_peakInformation".sample_id =ANY ('{%s}'::text[]) '''%(
            #        self.convert_list2string(sample_id_I));
            #    cmd+=cmd_q;
            if sample_name_abbreviation_I:
                cmd_q = '''AND "data_stage01_quantification_peakInformation".sample_name_abbreviation =ANY ('{%s}'::text[]) '''%(
                    self.convert_list2string(sample_name_abbreviation_I));
                cmd+=cmd_q;
            if component_name_I:
                cmd_q = '''AND "data_stage01_quantification_peakInformation".component_name_I =ANY ('{%s}'::text[]) '''%(
                    self.convert_list2string(component_name_I));
                cmd+=cmd_q;
            if component_group_name_I:
                cmd_q = '''AND "data_stage01_quantification_peakInformation".component_group_name_I =ANY ('{%s}'::text[]) '''%(
                    self.convert_list2string(component_group_name_I));
                cmd+=cmd_q;
            #if sample_type_I:
            #    cmd_q = '''AND "data_stage01_quantification_peakInformation".sample_type =ANY ('{%s}'::text[]) '''%(
            #        self.convert_list2string(sample_type_I));
            #    cmd+=cmd_q;
            #if acquisition_date_and_time_I and not acquisition_date_and_time_I[0] is None:
            #    cmd_q = '''AND "data_stage01_quantification_peakInformation".acquisition_date_and_time >= %s'''%(
            #        acquisition_date_and_time_I[0]);
            #    cmd+=cmd_q;
            #    cmd_q = '''AND "data_stage01_quantification_peakInformation".acquisition_date_and_time <= %s'''%(
            #        acquisition_date_and_time_I[1]);
            #    cmd+=cmd_q;
            cmd += '''
                ORDER BY 
                "data_stage01_quantification_peakInformation"."analysis_id" ASC,
                "data_stage01_quantification_peakInformation"."experiment_id" ASC,
                "data_stage01_quantification_peakInformation"."sample_name_abbreviation" ASC,
                "data_stage01_quantification_peakInformation"."component_group_name" ASC,
                "data_stage01_quantification_peakInformation"."component_name" ASC,
                "data_stage01_quantification_peakInformation"."peakInfo_parameter" ASC;
            '''
            result = self.session.execute(cmd);
            data = result.fetchall();
            data_O = [dict(d) for d in data];
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    # Query component_names from data_stage01_quantificaton_peakInformation
    def get_componentNames_experimentID_dataStage01PeakInformation(self,experiment_id_I):
        '''Query component_names that are used for the experiment'''
        try:
            names = self.session.query(data_stage01_quantification_peakInformation.component_name).filter(
                    data_stage01_quantification_peakInformation.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakInformation.used_.is_(True)).group_by(
                    data_stage01_quantification_peakInformation.component_name).order_by(
                    data_stage01_quantification_peakInformation.component_name.asc()).all();
            names_O = [];
            for n in names:
                names_O.append(n.component_name);
            return names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentNames_experimentIDAndPeakInfoParameter_dataStage01PeakInformation(self,experiment_id_I,peakInfo_parameter_I):
        '''Query component_names that are used for the experiment'''
        try:
            names = self.session.query(data_stage01_quantification_peakInformation.component_name).filter(
                    data_stage01_quantification_peakInformation.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakInformation.peakInfo_parameter.like(peakInfo_parameter_I),
                    data_stage01_quantification_peakInformation.used_.is_(True)).group_by(
                    data_stage01_quantification_peakInformation.component_name).order_by(
                    data_stage01_quantification_peakInformation.component_name.asc()).all();
            names_O = [];
            for n in names:
                names_O.append(n.component_name);
            return names_O;
        except SQLAlchemyError as e:
            print(e);
            
    # Query peakInfo_parameter from data_stage01_quantification_peakResolution
    def get_peakInfoParameter_experimentID_dataStage01PeakResolution(self,experiment_id_I):
        '''Query component_names that are used for the experiment'''
        try:
            names = self.session.query(data_stage01_quantification_peakResolution.peakInfo_parameter).filter(
                    data_stage01_quantification_peakResolution.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakResolution.used_.is_(True)).group_by(
                    data_stage01_quantification_peakResolution.component_name).order_by(
                    data_stage01_quantification_peakResolution.component_name.asc()).all();
            names_O = [];
            for n in names:
                names_O.append(n.peakInfo_parameter);
            return names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_peakResolution
    def get_row_experimentIDAndComponentName_dataStage01PeakResolution(self, experiment_id_I, component_name_I):
        """Query rows"""
        try:
            data = self.session.query(data_stage01_quantification_peakResolution).filter(
                    data_stage01_quantification_peakResolution.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakResolution.component_name.like(component_name_I),
                    data_stage01_quantification_peakResolution.used_.is_(True)).all();
            data_O = {};
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                for d in data:
                    data_O = {'experiment_id':d.experiment_id,
            'component_group_name_pair':d.component_group_name_pair,
            'component_name_pair':d.component_name_pair,
            'peakInfo_parameter':d.peakInfo_parameter,
            'peakInfo_ave':d.peakInfo_ave,
            'peakInfo_cv':d.peakInfo_cv,
            'peakInfo_lb':d.peakInfo_lb,
            'peakInfo_ub':d.peakInfo_ub,
            'peakInfo_units':d.peakInfo_units,
            'sample_names':d.sample_names,
            'sample_types':d.sample_types,
            'acqusition_date_and_times':d.acqusition_date_and_times,
            'peakInfo_data':d.peakInfo_data};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_experimentIDAndPeakInfoParameterComponentName_dataStage01PeakResolution(self, experiment_id_I, peakInfo_parameter_I, component_name_pair_I):
        """Query rows"""
        try:
            data = self.session.query(data_stage01_quantification_peakResolution).filter(
                    data_stage01_quantification_peakResolution.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakResolution.component_name_pair.any(component_name_pair_I[0]),
                    data_stage01_quantification_peakResolution.component_name_pair.any(component_name_pair_I[1]),
                    data_stage01_quantification_peakResolution.peakInfo_parameter.like(peakInfo_parameter_I),
                    data_stage01_quantification_peakResolution.used_.is_(True)).all();
            data_O = {};
            if len(data)>1:
                print('more than 1 calculated_concentration retrieved per component_name')
            if data:
                for d in data:
                    data_O = {'experiment_id':d.experiment_id,
            'component_group_name_pair':d.component_group_name_pair,
            'component_name_pair':d.component_name_pair,
            'peakInfo_parameter':d.peakInfo_parameter,
            'peakInfo_ave':d.peakInfo_ave,
            'peakInfo_cv':d.peakInfo_cv,
            'peakInfo_lb':d.peakInfo_lb,
            'peakInfo_ub':d.peakInfo_ub,
            'peakInfo_units':d.peakInfo_units,
            'sample_names':d.sample_names,
            'sample_types':d.sample_types,
            'acqusition_date_and_times':d.acqusition_date_and_times,
            'peakInfo_data':d.peakInfo_data};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # Query component_names from data_stage01_quantification_peakResolution
    def get_componentNamePairs_experimentID_dataStage01PeakResolution(self,experiment_id_I):
        '''Query component_names that are used for the experiment'''
        try:
            names = self.session.query(data_stage01_quantification_peakResolution.component_name_pair).filter(
                    data_stage01_quantification_peakResolution.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakResolution.used_.is_(True)).group_by(
                    data_stage01_quantification_peakResolution.component_name_pair).order_by(
                    data_stage01_quantification_peakResolution.component_name_pair.asc()).all();
            names_O = [];
            for n in names:
                names_O.append(n.component_name_pair);
            return names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentNamePairs_experimentIDAndPeakInfoParameter_dataStage01PeakResolution(self,experiment_id_I,peakInfo_parameter_I):
        '''Query component_names that are used for the experiment'''
        try:
            names = self.session.query(data_stage01_quantification_peakResolution.component_name_pair).filter(
                    data_stage01_quantification_peakResolution.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_peakResolution.peakInfo_parameter.like(peakInfo_parameter_I),
                    data_stage01_quantification_peakResolution.used_.is_(True)).group_by(
                    data_stage01_quantification_peakResolution.component_name_pair).order_by(
                    data_stage01_quantification_peakResolution.component_name_pair.asc()).all();
            names_O = [];
            for n in names:
                names_O.append(n.component_name_pair);
            return names_O;
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_quantification_peakInformation(self):
        try:
            data_stage01_quantification_peakInformation.__table__.drop(self.engine,True);
            data_stage01_quantification_peakResolution.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_peakInformation(self):
        try:
            data_stage01_quantification_peakInformation.__table__.create(self.engine,True);
            data_stage01_quantification_peakResolution.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_quantification_peakInformation(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_peakInformation).filter(data_stage01_quantification_peakInformation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_peakResolution).filter(data_stage01_quantification_peakResolution.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);