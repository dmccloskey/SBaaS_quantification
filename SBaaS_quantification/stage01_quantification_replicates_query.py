﻿#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
from .stage01_quantification_replicates_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base

class stage01_quantification_replicates_query(sbaas_base):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_replicates':data_stage01_quantification_replicates,
                        };
        self.set_supportedTables(tables_supported);
        
    # Query samples from data_stage01_quantification_replicates
    def get_sampleNameAbbreviations_experimentID_dataStage01Replicates(self,experiment_id_I,exp_type_I=4):
        '''Querry sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample_description.sample_name_abbreviation).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_description.sample_name_short),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicates.used_.is_(True)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_abbreviation);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_SampleNameShort_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage01Replicates(self,experiment_id_I,sample_name_abbreviation_I,time_point_I,exp_type_I=4):
        '''Querry sample names short that are used from the experiment and sample name abbreviation and time point'''
        try:
            sample_names = self.session.query(sample_description.sample_name_short).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    sample_description.sample_id.like(sample.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    sample_description.sample_desc.like('Broth'),
                    data_stage01_quantification_replicates.used_.is_(True),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_description.sample_name_short)
                    ).group_by(
                    sample_description.sample_name_short).order_by(
                    sample_description.sample_name_short.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_SampleNameShort_experimentID_dataStage01Replicates(self,experiment_id_I):
        '''Querry sample names short that are used from the experiment and sample name abbreviation and time point'''
        try:
            sample_names = self.session.query(data_stage01_quantification_replicates.sample_name_short).filter(
                    experiment.id.like(experiment_id_I),
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.used_.is_(True),
                    ).group_by(
                    data_stage01_quantification_replicates.sample_name_short).order_by(
                    data_stage01_quantification_replicates.sample_name_short.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name_short);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query time points
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01Replicates(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Querry time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    data_stage01_quantification_replicates.used_.is_(True),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_description.sample_name_short)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoint_experimentIDAndSampleNameShort_dataStage01Replicates(self,experiment_id_I,sample_name_short_I):
        '''Querry time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(data_stage01_quantification_replicates.time_point).filter(
                    data_stage01_quantification_replicates.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.used_.is_(True),).group_by(
                    data_stage01_quantification_replicates.time_point).order_by(
                    data_stage01_quantification_replicates.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query concentration units:
    def get_calculatedConcentrationUnits_experimentID_dataStage01Replicates(self,experiment_id_I):
        '''Query calculated_concentration_units that are used from the experiment'''
        try:
            calculated_concentration_units = self.session.query(data_stage01_quantification_replicates.calculated_concentration_units).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.used_.is_(True),).group_by(
                    data_stage01_quantification_replicates.calculated_concentration_units).order_by(
                    data_stage01_quantification_replicates.calculated_concentration_units.asc()).all();
            calculated_concentration_units_O = [];
            for tp in calculated_concentration_units: calculated_concentration_units_O.append(tp.calculated_concentration_units);
            return calculated_concentration_units_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows data_stage01_quantification_replicates
    def get_rows_experimentIDAndSampleNameShortAndTimePointAndCalculatedConcentrationUnits_dataStage01Replicates(self,
            experiment_id_I, sample_name_short_I, time_point_I,calculated_concentration_units_I):
        """query rows"""
        try:
            data = self.session.query(data_stage01_quantification_replicates).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.used_.is_(True),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_replicates.calculated_concentration_units.like(calculated_concentration_units_I),
                    data_stage01_quantification_replicates.used_.is_(True)).all();
            data_O = [];
            for d in data: 
                data_O.append(d.__repr__dict__());
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    # Query data data_stage01_quantification_replicates:
    def get_data_experimentID_dataStage01Replicates(self, experiment_id_I):
        """write query results to csv"""
        try:
            data = self.session.query(data_stage01_quantification_replicates.sample_name_short,
                    data_stage01_quantification_replicates.calculated_concentration,
                    data_stage01_quantification_replicates.component_group_name).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.used_.is_(True)).all();
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
    def get_data_experimentIDAndSampleNameShortAndTimePoint_dataStage01Replicates(self, experiment_id_I, sample_name_short_I, time_point_I):
        """write query results to csv"""
        try:
            data = self.session.query(data_stage01_quantification_replicates.sample_name_short,
                    data_stage01_quantification_replicates.calculated_concentration,
                    data_stage01_quantification_replicates.component_name).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.used_.is_(True),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_replicates.used_.is_(True)).all();
            data_O = [];
            for d in data: 
                data_1 = {};
                data_1['sample_name_short'] = d.sample_name_short;
                data_1['component_name'] = d.component_name;
                data_1['calculated_concentration'] = d.calculated_concentration;
                data_O.append(data_1);
            return data_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentGroupNameAndConcUnits_experimentIDAndComponentName_dataStage01Replicates(self,experiment_id_I, component_name_I):
        '''Querry data (i.e. concentration) from component name
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_quantification_replicates.component_group_name,
                    data_stage01_quantification_replicates.calculated_concentration_units).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.component_name.like(component_name_I)).group_by(
                    data_stage01_quantification_replicates.component_group_name,
                    data_stage01_quantification_replicates.calculated_concentration_units).all();
            if len(data)>1:
                print('more than 1 component_group_name retrieved per component_name')
            if data:
                cgn_O = data[0][0];
                conc_units_O = data[0][1];
            else: 
                conc_O = None;
                conc_units_O = None;
            return cgn_O, conc_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentGroupNameAndConcUnits_experimentIDAndComponentNameAndSampleNameAbbreviationAndTimePoint_dataStage01Replicates(self,experiment_id_I, component_name_I, sample_name_abbreviation_I,time_point_I,exp_type_I=4):
        '''Querry data (i.e. concentration) from component name and sample name abbreviation and time points
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_quantification_replicates.component_group_name,
                    data_stage01_quantification_replicates.calculated_concentration_units).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.time_point.like(time_point_I),
                    sample_description.sample_id.like(sample.sample_id),
                    experiment.exp_type_id == exp_type_I,
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(sample.sample_name),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_description.sample_name_short),
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.component_name.like(component_name_I)).group_by(
                    data_stage01_quantification_replicates.component_group_name,
                    data_stage01_quantification_replicates.calculated_concentration_units).all();
            if len(data)>1:
                print('more than 1 component_group_name retrieved per component_name')
            if data:
                cgn_O = data[0][0];
                conc_units_O = data[0][1];
            else: 
                conc_O = None;
                conc_units_O = None;
            return cgn_O, conc_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_concAndConcUnits_experimentIDAndSampleNameShortAndTimePointAndComponentGroupName_dataStage01Replicates(self, experiment_id_I, sample_name_short_I, time_point_I, component_group_name_I):
        """Query calculated concentrations"""
        try:
            data = self.session.query(data_stage01_quantification_replicates.calculated_concentration,
                    data_stage01_quantification_replicates.calculated_concentration_units).filter(
                    data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                    data_stage01_quantification_replicates.sample_name_short.like(sample_name_short_I),
                    data_stage01_quantification_replicates.time_point.like(time_point_I),
                    data_stage01_quantification_replicates.component_group_name.like(component_group_name_I),
                    data_stage01_quantification_replicates.used_.is_(True)).all();
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
    def reset_dataStage01_quantification_replicates(self,experiment_id_I,sample_name_short_I=[],component_names_I=[]):
        try:
            if experiment_id_I and sample_name_short_I:
                for sample_name_short in sample_name_short_I:
                    for component_name in component_names_I:
                        reset = self.session.query(data_stage01_quantification_replicates).filter(
                                     data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                                     data_stage01_quantification_replicates.sample_name_short.like(sample_name_short),
                                     data_stage01_quantification_replicates.component_name.like(component_name)).delete(synchronize_session=False);
                self.session.commit();
            elif experiment_id_I and sample_name_short_I:
                for sample_name_short in sample_name_short_I:
                    reset = self.session.query(data_stage01_quantification_replicates).filter(
                                     data_stage01_quantification_replicates.experiment_id.like(experiment_id_I),
                                     data_stage01_quantification_replicates.sample_name_short.like(sample_name_short)).delete(synchronize_session=False);
                self.session.commit();
            elif experiment_id_I:
                reset = self.session.query(data_stage01_quantification_replicates).filter(data_stage01_quantification_replicates.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_quantification_replicates(self):
        try:
            data_stage01_quantification_replicates.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_quantification_replicates(self):
        try:
            data_stage01_quantification_replicates.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);