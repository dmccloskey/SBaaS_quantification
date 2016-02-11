from .stage01_quantification_QCs_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_quantification_QCs_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_QCs':data_stage01_quantification_QCs,
                        #    'data_stage01_quantification_checkCV_dilutions':data_stage01_quantification_checkCV_dilutions,
                        #'data_stage01_quantification_checkCV_QCs':data_stage01_quantification_checkCV_QCs,
                        #'data_stage01_quantification_checkCVAndExtracellular_averages':data_stage01_quantification_checkCVAndExtracellular_averages,
                        #'data_stage01_quantification_checkISMatch':data_stage01_quantification_checkISMatch,
                        #'data_stage01_quantification_checkLLOQAndULOQ':data_stage01_quantification_checkLLOQAndULOQ,
                        'data_stage01_quantification_dilutions':data_stage01_quantification_dilutions,
                        'data_stage01_quantification_LLOQAndULOQ':data_stage01_quantification_LLOQAndULOQ,
                        };
        self.set_supportedTables(tables_supported);

    def add_dataStage01_quantification_QCs(self, data_I):
        '''add rows of quantification_QCs'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_quantification_QCs(d['experiment_id'],
                    d['sample_name_abbreviation'],
                    d['sample_dilution'],
                    d['component_group_name'],
                    d['component_name'],
                    d['n_replicates'],
                    d['calculated_concentration_average'],
                    d['calculated_concentration_CV'],
                    d['calculated_concentration_units']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01_quantification_dilutions(self, data_I):
        '''add rows of _quantification_dilutions'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_quantification_dilutions(d['experiment_id'],
                        d['sample_id'],
                        d['component_group_name'],
                        d['component_name'],
                        d['n_replicates'],
                        d['calculated_concentration_average'],
                        d['calculated_concentration_cv'],
                        d['calculated_concentration_units']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01_quantification_LLOQAndULOQ(self, data_I):
        '''add rows of quantification_LLOQAndULOQ'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_quantification_LLOQAndULOQ(d['experiment_id'],
                        d['sample_name'],
                        d['component_group_name'],
                        d['component_name'],
                        d['calculated_concentration'],
                        d['calculated_concentration_units'],
                        d['correlation'],
                        d['lloq'],
                        d['uloq'],
                        d['points'],
                        d['used_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
            

    # data_stage01_quantification_dilutions only
    def get_checkCV_dilutions(self,experiment_id_I,cv_threshold_I=20.0):
        '''query to populate the "checkCV_dilutions" view'''
        try:
            check = self.session.query(data_stage01_quantification_dilutions).filter(
                        data_stage01_quantification_dilutions.experiment_id.like(experiment_id_I),
                        data_stage01_quantification_dilutions.calculated_concentration_cv > cv_threshold_I).all();
            check_O = [];
            for c in check: 
                check_1 = {};
                check_1['experiment_id'] = c.experiment_id;
                check_1['sample_id'] = c.sample_id;
                check_1['component_group_name'] = c.component_group_name;
                check_1['component_name'] = c.component_name;
                check_1['n_replicates'] = c.n_replicates;
                check_1['calculated_concentration_average'] = c.calculated_concentration_average;
                check_1['calculated_concentration_cv'] = c.calculated_concentration_cv;
                check_1['calculated_concentration_units'] = c.calculated_concentration_units;
                check_O.append(check_1);
            return  check_O;
        except SQLAlchemyError as e:
            print(e);

    def reset_datastage01_quantification_LLOQAndULOQ(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_LLOQAndULOQ).filter(data_stage01_quantification_LLOQAndULOQ.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_quantification_LLOQAndULOQ).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage01_quantification_QCs(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_QCs).filter(data_stage01_quantification_QCs.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_quantification_QCs).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage01_quantification_dilutions(self,experiment_id_I):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_dilutions).filter(data_stage01_quantification_dilutions.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_quantification_dilutions).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_quantification_QCs(self):
        try:
            data_stage01_quantification_LLOQAndULOQ.__table__.drop(self.engine,True);
            data_stage01_quantification_QCs.__table__.drop(self.engine,True);
            data_stage01_quantification_dilutions.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_QCs(self):
        try:
            data_stage01_quantification_LLOQAndULOQ.__table__.create(self.engine,True);
            data_stage01_quantification_QCs.__table__.create(self.engine,True);
            data_stage01_quantification_dilutions.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_quantification_allQCs(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_quantification_LLOQAndULOQ).filter(data_stage01_quantification_LLOQAndULOQ.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_dilutions).filter(data_stage01_quantification_dilutions.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_QCs).filter(data_stage01_quantification_QCs.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_quantification_LLOQAndULOQ).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_dilutions).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_quantification_QCs).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    
    def update_data_stage01_quantification_LLOQAndULOQ(self,data_I):
        '''update rows of data_stage01_quantification_LLOQAndULOQ'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_quantification_LLOQAndULOQ).filter(
                            data_stage01_quantification_LLOQAndULOQ.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'component_group_name':d['component_group_name'],
                            'component_name':d['component_name'],
                            'calculated_concentration':d['calculated_concentration'],
                            'calculated_concentration_units':d['calculated_concentration_units'],
                            'correlation':d['correlation'],
                            'lloq':d['lloq'],
                            'uloq':d['uloq'],
                            'points':d['points'],
                            'used_':d['used_']
                                },
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    
    def update_data_stage01_quantification_dilutions(self,data_I):
        '''update rows of data_stage01_quantification_dilutions'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_quantification_dilutions).filter(
                            data_stage01_quantification_dilutions.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_id':d['sample_id'],
                            'component_group_name':d['component_group_name'],
                            'component_name':d['component_name'],
                            'n_replicates':d['n_replicates'],
                            'calculated_concentration_average':d['calculated_concentration_average'],
                            'calculated_concentration_cv':d['calculated_concentration_cv'],
                            'calculated_concentration_units':d['calculated_concentration_units']
                                },
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    
    def update_data_stage01_quantification_QCs(self,data_I):
        '''update rows of data_stage01_quantification_QCs'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_quantification_QCs).filter(
                            data_stage01_quantification_QCs.id==d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'sample_dilution':d['sample_dilution'],
                            'component_group_name':d['component_group_name'],
                            'component_name':d['component_name'],
                            'n_replicates':d['n_replicates'],
                            'calculated_concentration_average':d['calculated_concentration_average'],
                            'calculated_concentration_CV':d['calculated_concentration_CV'],
                            'calculated_concentration_units':d['calculated_concentration_units']
                                },
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
   # Query information from calibrators based on data_stage01_quantification_replicatesMI
    def get_lloq_ExperimentIDAndComponentName_dataStage01LLOQAndULOQ(self, experiment_id_I, component_name_I):
        '''Query lloq for a given component and experiment
        NOTE: intended to be used in a loop'''

        try:
            calibrators_parameters = self.session.query(data_stage01_quantification_LLOQAndULOQ.lloq,
                                                   data_stage01_quantification_LLOQAndULOQ.calculated_concentration_units).filter(
                                data_stage01_quantification_LLOQAndULOQ.experiment_id.like(experiment_id_I),
                                data_stage01_quantification_LLOQAndULOQ.component_name.like(component_name_I)).first();
            if calibrators_parameters:
                lloq_O = calibrators_parameters.lloq;
                calculated_concentration_units_O = calibrators_parameters.calculated_concentration_units;
                return lloq_O, calculated_concentration_units_O;
            else:
                return None,None;

        except SQLAlchemyError as e:
            print(e);