from .stage01_quantification_normalized_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
from SBaaS_LIMS.lims_experiment_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_quantification_normalized_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_normalized':data_stage01_quantification_normalized,
                            'data_stage01_quantification_averages':data_stage01_quantification_averages,
                        };
        self.set_supportedTables(tables_supported);
        # query samples from data_stage01_quantification_normalized
    def get_sampleIDs_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample ids that are used from
        the experiment'''
        try:
            sample_ids = self.session.query(data_stage01_quantification_normalized.sample_id).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.sample_id).order_by(
                    data_stage01_quantification_normalized.sample_id.asc()).all();
            sample_ids_O = [];
            for si in sample_ids: sample_ids_O.append(si.sample_id);
            return sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_normalized.sample_name).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.sample_name).order_by(
                    data_stage01_quantification_normalized.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentName_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,sample_decription_I,component_name_I,exp_type_I=4):
        '''Querry sample names that are used from the experiment by sample name abbreviation and sample description'''
        try:
            sample_names = self.session.query(data_stage01_quantification_normalized.sample_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.sample_desc.like(sample_decription_I),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    sample.sample_id.like(sample_description.sample_id),
                    sample.sample_name.like(data_stage01_quantification_normalized.sample_name),
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.sample_name).order_by(
                    data_stage01_quantification_normalized.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescriptionAndComponentNameAndTimePoint_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,sample_decription_I,component_name_I,time_point_I,exp_type_I=4):
        '''Querry sample names that are used from the experiment by sample name abbreviation and sample description'''
        try:
            sample_names = self.session.query(data_stage01_quantification_normalized.sample_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    sample_description.sample_desc.like(sample_decription_I),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    sample.sample_id.like(sample_description.sample_id),
                    sample.sample_name.like(data_stage01_quantification_normalized.sample_name),
                    #experiment.sample_name.like(sample.sample_name),  #not required so long as all sample_names are unique!
                    #experiment.id.like(experiment_id_I),
                    #experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.sample_name).order_by(
                    data_stage01_quantification_normalized.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleName_experimentIDAndSampleIDAndSampleDilution_dataStage01Normalized(self,experiment_id_I,sample_id_I, sample_dilution_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_name = self.session.query(data_stage01_quantification_normalized.sample_name).filter(
                    data_stage01_quantification_normalized.sample_id.like(sample_id_I),
                    sample.sample_dilution == sample_dilution_I,
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.used_.is_(True)).all();
            sample_name_O = sample_name[0];
            return sample_name_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleName_dataStage01Normalized(self,experiment_id_I,sample_name_I):
        '''Querry sample name short that are used from
        the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    sample.sample_name.like(sample_name_I),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.used_.is_(True),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_short).all();
            sample_name_short_O = sample_name_short[0];
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleDescription_dataStage01Normalized(self,experiment_id_I,sample_description_I,exp_type_I=4):
        '''Querry sample name short that are in the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(sample.sample_name),
                    sample_description.sample_desc.like(sample_description_I)).group_by(
                    sample_description.sample_name_short).all();
            sample_name_short_O = [];
            if sample_name_short:
                for sns in sample_name_short:
                    sample_name_short_O.append(sns[0]);
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample name short that are in the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.sample_name_short).all();
            sample_name_short_O = [];
            if sample_name_short:
                for sns in sample_name_short:
                    sample_name_short_O.append(sns[0]);
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query components from data_stage01_quantification_normalized
    def get_componentsNames_experimentID_dataStage01Normalized(self,experiment_id_I):
        '''Querry component names that are used and not internal standards from
        the experiment id'''
        try:
            component_names = self.session.query(data_stage01_quantification_normalized.component_name).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),                  
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.component_name).order_by(
                    data_stage01_quantification_normalized.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleID_dataStage01Normalized(self,experiment_id_I,sample_id_I):
        '''Querry component names that are used and not internal standards from
        the experiment and sample_id'''
        try:
            component_names = self.session.query(data_stage01_quantification_normalized.component_name).filter(
                    data_stage01_quantification_normalized.sample_id.like(sample_id_I),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),                  
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.component_name).order_by(
                    data_stage01_quantification_normalized.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleName_dataStage01Normalized(self,experiment_id_I,sample_name_I):
        '''Querry component names that are used and not internal standards from
        the experiment and sample_name'''
        try:
            component_names = self.session.query(data_stage01_quantification_normalized.component_name).filter(
                    data_stage01_quantification_normalized.sample_name.like(sample_name_I),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),                  
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.component_name).order_by(
                    data_stage01_quantification_normalized.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry component names that are used and not internal standards from
        the experiment and sample abbreviation'''
        try:
            component_names = self.session.query(data_stage01_quantification_normalized.component_name).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    #experiment.exp_type_id == exp_type_I,  #not required so long as all sample_names are unique!
                    #experiment.id.like(experiment_id_I),
                    #experiment.sample_name.like(sample.sample_name),  
                    sample.sample_id.like(sample_description.sample_id),  
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),            
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.component_name).order_by(
                    data_stage01_quantification_normalized.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentGroupName_experimentIDAndComponentName_dataStage01Normalized(self,experiment_id_I,component_name_I):
        '''Querry component group names that are used from the component name
        NOTE: intended to be used within a for loop'''
        try:
            component_group_name = self.session.query(data_stage01_quantification_normalized.component_group_name).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    data_stage01_quantification_normalized.used_.is_(True)).group_by(
                    data_stage01_quantification_normalized.component_group_name).all();
            if len(component_group_name)>1:
                print('more than 1 component_group_name retrieved per component_name')
            component_group_name_O = component_group_name[0];
            return component_group_name_O;
        except SQLAlchemyError as e:
            print(e);
    # query dilutions from data_stage01_quantification_normalized
    def get_sampleDilutions_experimentIDAndSampleIDAndComponentName_dataStage01Normalized(self,experiment_id_I,sample_id_I,component_name_I):
        '''Querry dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(sample.sample_dilution).filter(
                    sample.sample_id.like(sample_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.used_.is_(True),
                    data_stage01_quantification_normalized.component_name.like(component_name_I)).group_by(
                    sample.sample_dilution).order_by(
                    sample.sample_dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.sample_dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    # query time points
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Normalized(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    #experiment.exp_type_id == exp_type_I, #not required so long as all sample_names are unique!
                    #experiment.id.like(experiment_id_I),
                    #experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_normalized.used_.is_(True),
                    data_stage01_quantification_normalized.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query data from data_stage01_quantification_normalized    
    def get_concAndConcUnits_sampleNameAndComponentName_dataStage01Normalized(self,sample_name_I,component_name_I):
        '''Querry data (i.e. concentration) from sample name and component name
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_quantification_normalized.calculated_concentration,
                    data_stage01_quantification_normalized.calculated_concentration_units).filter(
                    data_stage01_quantification_normalized.sample_name.like(sample_name_I),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    data_stage01_quantification_normalized.used_.is_(True)).all();
            if data:
                conc_O = data[0][0];
                conc_units_O = data[0][1];
            else: 
                conc_O = None;
                conc_units_O = None;
            return conc_O, conc_units_O;
        except SQLAlchemyError as e:
            print(e);  
    def get_row_sampleNameAndComponentName_dataStage01Normalized(self,sample_name_I,component_name_I):
        '''Query row by sample name and component name from data_stage01_quantification_normalized
        '''
        try:
            data = self.session.query(data_stage01_quantification_normalized).filter(
                    data_stage01_quantification_normalized.sample_name.like(sample_name_I),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    data_stage01_quantification_normalized.used_.is_(True)).all();
            if data:
                data_O = data[0].__repr__dict__();
            else: 
                data_O = {};
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_uniqueAndUsed_dataStage01QuantificationNormalized(self,experiment_id_I='%',
                        sample_name_I='%',
                        component_name_I='%',
                        calculated_concentration_units_I='%',
                        used__I=True):
        '''Query row by unique columns from data_stage01_quantification_normalized
        '''
        try:
            data = self.session.query(data_stage01_quantification_normalized).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample_name_I),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    data_stage01_quantification_normalized.calculated_concentration_units.like(calculated_concentration_units_I),
                    data_stage01_quantification_normalized.used_.is_(used__I)).all();
            data_O=[];
            if data:
                for d in data:
                    data_O.append(d.__repr__dict__());
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_all_dataStage01QuantificationNormalized(self,experiment_id_I='%',sample_name_I='%',
                        sample_id_I='%',component_group_name_I='%',component_name_I='%',
                        calculated_concentration_units_I='%',used__I=True):
        '''Query rows by all columns from data_stage01_quantification_normalized
        '''
        try:
            data = self.session.query(data_stage01_quantification_normalized).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_id.like(sample_id_I),
                    data_stage01_quantification_normalized.sample_name.like(sample_name_I),
                    data_stage01_quantification_normalized.component_group_name.like(component_group_name_I),
                    data_stage01_quantification_normalized.component_name.like(component_name_I),
                    data_stage01_quantification_normalized.calculated_concentration_units.like(calculated_concentration_units_I),
                    data_stage01_quantification_normalized.used_.is_(used__I)).all();
            data_O=[];
            if data:
                for d in data:
                    data_O.append(d.__repr__dict__());
        except SQLAlchemyError as e:
            print(e);

            
    def drop_dataStage01_quantification_normalized(self):
        try:
            data_stage01_quantification_normalized.__table__.drop(self.engine,True);
            data_stage01_quantification_averages.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_normalized(self):
        try:
            data_stage01_quantification_normalized.__table__.create(self.engine,True);
            data_stage01_quantification_averages.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_quantification_normalized(self,experiment_id_I=None,sample_names_I=None):
        try:
            if experiment_id_I and sample_names_I:
                for sample_name in sample_names_I:
                    reset = self.session.query(data_stage01_quantification_normalized).filter(
                        data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                        data_stage01_quantification_normalized.sample_name.like(sample_name)).delete(synchronize_session=False);

            elif experiment_id_I:
                reset = self.session.query(data_stage01_quantification_normalized).filter(data_stage01_quantification_normalized.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_quantification_normalized).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def update_setUsed2False_experimentIDAndSampleName_dataStage01QuantificationNormalized(self,experiment_id_I=None,sample_names_I=None):
        try:
            if experiment_id_I and sample_names_I:
                for sample_name in sample_names_I:
                    data_update = self.session.query(data_stage01_quantification_normalized).filter(
                        data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                        data_stage01_quantification_normalized.sample_name.like(sample_name)).update(		
                        {
                        'used_':False},
                        synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def update_setUsed2FalseAllFiltrate_experimentID_dataStage01QuantificationNormalized(self,experiment_id_I=None):
        try:
            if experiment_id_I:
                filtrate_sample = '%_Filtrate-%';
                data_update = self.session.query(data_stage01_quantification_normalized).filter(
                    data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_normalized.sample_id.like(filtrate_sample)).update(		
                    {
                    'used_':False},
                    synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def update_setUsed2False_experimentIDAndComponentName_dataStage01QuantificationNormalized(self,experiment_id_I=None,component_names_I=None):
        try:
            if experiment_id_I and component_names_I:
                for component_name in component_names_I:
                    data_update = self.session.query(data_stage01_quantification_normalized).filter(
                        data_stage01_quantification_normalized.experiment_id.like(experiment_id_I),
                        data_stage01_quantification_normalized.component_name.like(component_name)).update(		
                        {
                        'used_':False},
                        synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);

    def update_dataStage01Normalized_unique(self,dataListUpdated_I):
        '''update the data_stage01_quantification_normalized by unique constraint'''
        for d in dataListUpdated_I:
            try:
                data_update = self.session.query(data_stage01_quantification_normalized).filter(
                        #data_stage01_quantification_normalized.id == d['id'],
                        data_stage01_quantification_normalized.experiment_id.like(d['experiment_id']),
                        data_stage01_quantification_normalized.sample_name.like(d['sample_name']),
                        data_stage01_quantification_normalized.component_name.like(d['component_name']),
                        data_stage01_quantification_normalized.calculated_concentration_units.like(d['calculated_concentration_units'])).update(		
                        {
                        #'experiment_id':d['experiment_id'],
                        #'sample_name':d['sample_name'],
                        #'sample_id':d['sample_id'],
                        #'component_group_name':d['component_group_name'],
                        #'component_name':d['component_name'],
                        'calculated_concentration':d['calculated_concentration'],
                        'calculated_concentration_units':d['calculated_concentration_units'],
                        'used_':d['used_'],
                        'comment_':d['comment_']},
                        synchronize_session=False);
                if data_update == 0:
                    print('row not found.')
                    print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
    def update_dataStage01Normalized_id(self,dataListUpdated_I,used_comment_only_I=False):
        '''update the data_stage01_quantification_normalized by id'''
        for d in dataListUpdated_I:
            try:
                if used_comment_only_I:
                    data_update = self.session.query(data_stage01_quantification_normalized).filter(
                            data_stage01_quantification_normalized.id == d['id']).update(		
                            {
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                else:
                    data_update = self.session.query(data_stage01_quantification_normalized).filter(
                            data_stage01_quantification_normalized.id == d['id']).update(		
                            {
                            'experiment_id':d['experiment_id'],
                            'sample_name':d['sample_name'],
                            'sample_id':d['sample_id'],
                            'component_group_name':d['component_group_name'],
                            'component_name':d['component_name'],
                            'calculated_concentration':d['calculated_concentration'],
                            'calculated_concentration_units':d['calculated_concentration_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
    def reset_dataStage01_quantification_averages(self,experiment_id_I=None,sample_name_abbreviations_I=[]):
        try:
            if experiment_id_I and sample_name_abbreviations_I:
                for sample_name_abbreviation in sample_name_abbreviations_I:
                    reset = self.session.query(data_stage01_quantification_averages).filter(data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                                                                                        data_stage01_quantification_averages.sample_name_abbreviation.like(sample_name_abbreviation)).delete(synchronize_session=False);
            elif experiment_id_I:
                reset = self.session.query(data_stage01_quantification_averages).filter(data_stage01_quantification_averages.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_quantification_averages).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def get_checkCVAndExtracellular_averages(self,experiment_id_I,cv_threshold_I=20,extracellular_threshold_I=50):
        '''query to populate the "checkCVAndExtracellular_averages" view'''
        try:
            check = self.session.query(data_stage01_quantification_averages).filter(
                        data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                        or_(data_stage01_quantification_averages.calculated_concentration_cv > cv_threshold_I,
                        data_stage01_quantification_averages.extracellular_percent > extracellular_threshold_I)).all();
            check_O = [];
            for c in check: 
                check_1 = {};
                check_1['experiment_id'] = c.experiment_id;
                check_1['sample_name_abbreviation'] = c.sample_name_abbreviation;
                check_1['time_point'] = c.time_point;
                check_1['component_group_name'] = c.component_group_name;
                check_1['component_name'] = c.component_name;
                check_1['n_replicates_broth'] = c.n_replicates_broth;
                check_1['calculated_concentration_broth_average'] = c.calculated_concentration_broth_average;
                check_1['calculated_concentration_broth_cv'] = c.calculated_concentration_broth_cv;
                check_1['n_replicates_filtrate'] = c.n_replicates_filtrate;
                check_1['calculated_concentration_filtrate_average'] = c.calculated_concentration_filtrate_average;
                check_1['calculated_concentration_filtrate_cv'] = c.calculated_concentration_filtrate_cv;
                check_1['n_replicates'] = c.n_replicates;
                check_1['calculated_concentration_average'] = c.calculated_concentration_average;
                check_1['calculated_concentration_cv'] = c.calculated_concentration_cv;
                check_1['calculated_concentration_units'] = c.calculated_concentration_units;
                check_1['extracellular_percent'] = c.extracellular_percent;
                check_1['used'] = c.used_;
                check_O.append(check_1);
            return  check_O;
        except SQLAlchemyError as e:
            print(e);
    
    # Query sample names from data_stage01_quantification_averages:
    def get_sampleNameAbbreviations_experimentIDAndTimePointAndComponentName_dataStage01Averages(self,experiment_id_I,time_point_I,component_name_I):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_averages.sample_name_abbreviation).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.time_point.like(time_point_I),
                    data_stage01_quantification_averages.component_name.like(component_name_I),
                    data_stage01_quantification_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_averages.sample_name_abbreviation).order_by(
                    data_stage01_quantification_averages.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data from data_stage01_quantification_averages:
    def get_row_experimentIDAndSampleNameAbbreviationAndTimePointAndComponentName_dataStage01Averages(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, component_name_I):
        """get row from experiment ID, sample name abbreviation, and time point"""
        try:
            data = self.session.query(data_stage01_quantification_averages).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_averages.component_name.like(component_name_I),
                    data_stage01_quantification_averages.time_point.like(time_point_I),
                    data_stage01_quantification_averages.used_.is_(True)).all();
            data_O = {};
            if data: 
                data_O=data[0].__repr__dict__();
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_experimentIDAndSampleNameAbbreviationAndTimePointAndComponentNameAndCalculatedConcentrationCVAndExtracellularPercent_dataStage01Averages(self,
            experiment_id_I, sample_name_abbreviation_I, time_point_I, component_name_I,cv_threshold_I=20,extracellular_threshold_I=50):
        """get row from experiment ID, sample name abbreviation, and time point"""
        try:
            data = self.session.query(data_stage01_quantification_averages).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_averages.component_name.like(component_name_I),
                    data_stage01_quantification_averages.time_point.like(time_point_I),
                    data_stage01_quantification_averages.used_.is_(True),
                    or_(data_stage01_quantification_averages.calculated_concentration_cv > cv_threshold_I,
                        data_stage01_quantification_averages.extracellular_percent > extracellular_threshold_I)).all();
            data_O = {};
            if data: 
                data_O=data[0].__repr__dict__();
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # Query time points from data_stage01_quantification_averages
    def get_timePoint_experimentID_dataStage01Averages(self,experiment_id_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_averages.time_point).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_averages.time_point).order_by(
                    data_stage01_quantification_averages.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndComponentName_dataStage01Averages(self,experiment_id_I,component_name_I):
        '''Querry time points that are used from the experiment'''
        try:
            time_points = self.session.query(data_stage01_quantification_averages.time_point).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.component_name.like(component_name_I),
                    data_stage01_quantification_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_averages.time_point).order_by(
                    data_stage01_quantification_averages.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # Query component names from data_stage01_quantification_averages:
    def get_componentNames_experimentIDAndTimePoint_dataStage01Averages(self,experiment_id_I,time_point_I):
        '''Querry component Names that are used from the experiment'''
        try:
            component_names = self.session.query(data_stage01_quantification_averages.component_name).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.time_point.like(time_point_I),
                    data_stage01_quantification_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_averages.component_name).order_by(
                    data_stage01_quantification_averages.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentNames_experimentID_dataStage01Averages(self,experiment_id_I):
        '''Querry component Names that are used from the experiment'''
        try:
            component_names = self.session.query(data_stage01_quantification_averages.component_name).filter(
                    data_stage01_quantification_averages.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_averages.used_.is_(True)).group_by(
                    data_stage01_quantification_averages.component_name).order_by(
                    data_stage01_quantification_averages.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);