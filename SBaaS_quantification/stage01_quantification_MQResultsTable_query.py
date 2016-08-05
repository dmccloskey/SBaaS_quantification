#lims
from .lims_quantitationMethod_postgresql_models import *
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_quantification_MQResultsTable_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#resources
from listDict.listDict import listDict

class stage01_quantification_MQResultsTable_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_quantification_mqresultstable':data_stage01_quantification_MQResultsTable,
                        };
        self.set_supportedTables(tables_supported);

    def initialize_dataStage01_quantification_MQResultsTable(self,
            tables_I = [],):
        try:
            if not tables_I:
                tables_I = list(self.get_supportedTables().keys());
            queryinitialize = sbaas_base_query_initialize(session_I=self.session,engine_I=self.engine,settings_I=self.settings,data_I=self.data);
            for table in tables_I:
                model_I = self.convert_tableString2SqlalchemyModel(table);
                queryinitialize.initialize_table_sqlalchemyModel(model_I);
        except Exception as e:
            print(e);
    def drop_dataStage01_quantification_MQResultsTable(self,
            tables_I = [],):
        try:
            if not tables_I:
                tables_I = list(self.get_supportedTables().keys());
            querydrop = sbaas_base_query_drop(session_I=self.session,engine_I=self.engine,settings_I=self.settings,data_I=self.data);
            for table in tables_I:
                model_I = self.convert_tableString2SqlalchemyModel(table);
                querydrop.drop_table_sqlalchemyModel(model_I);
        except Exception as e:
            print(e);
    def reset_dataStage01_quantification_MQResultsTable(self,
            component_name,sample_name,acquisition_date_and_time,
            tables_I = [],
            warn_I=True):
        try:
            if not tables_I:
                tables_I = list(self.get_supportedTables().keys());
            querydelete = sbaas_base_query_delete(session_I=self.session,engine_I=self.engine,settings_I=self.settings,data_I=self.data);
            for table in tables_I:
                query = {};
                query['delete_from'] = [{'table_name':table}];
                query['where'] = [{
                        'table_name':table,
                        'column_name':'component_name',
                        'value':analysis_id_I,
		                'operator':'LIKE',
                        'connector':'AND'
                        },{
                        'table_name':table,
                        'column_name':'sample_name',
                        'value':analysis_id_I,
		                'operator':'LIKE',
                        'connector':'AND'
                        },{
                        'table_name':table,
                        'column_name':'acquisition_date_and_time',
                        'value':analysis_id_I,
		                'operator':'LIKE',
                        'connector':'AND'
                        },
	                ];
                table_model = self.convert_tableStringList2SqlalchemyModelDict([table]);
                query = querydelete.make_queryFromString(table_model,query);
                querydelete.reset_table_sqlalchemyModel(query_I=query,warn_I=warn_I);
        except Exception as e:
            print(e);

    def add_dataStage01MQResultsTable(self,data_I):
        '''add rows of data_stage01_quantification_MQResultsTable'''
        if data_I:
            cnt = 0;
            for d in data_I:
                try:
                    if 'Index' in d:
                        d['index_']=d['Index'];
                        d['sample_index']=d['Sample Index'];
                        d['original_filename']=d['Original Filename'];
                        d['sample_name']=d['Sample Name'];
                        d['sample_id']=d['Sample ID'];
                        d['sample_comment']=d['Sample Comment'];
                        d['sample_type']=d['Sample Type'];
                        d['acquisition_date_and_time']=d['Acquisition Date & Time'];
                        d['rack_number']=d['Rack Number'];
                        d['plate_number']=d['Plate Number'];
                        d['vial_number']=d['Vial Number'];
                        d['dilution_factor']=d['Dilution Factor'];
                        d['injection_volume']=d['Injection Volume'];
                        d['operator_name']=d['Operator Name'];
                        d['acq_method_name']=d['Acq. Method Name'];
                        d['is_']=d['IS'];
                        d['component_name']=d['Component Name'];
                        d['component_index']=d['Component Index'];
                        d['component_comment']=d['Component Comment'];
                        d['is_comment']=d['IS Comment'];
                        d['mass_info']=d['Mass Info'];
                        d['is_mass']=d['IS Mass Info'];
                        d['is_name']=d['IS Name'];
                        d['component_group_name']=d['Component Group Name'];
                        d['conc_units']=d['Conc. Units'];
                        d['failed_query']=d['Failed Query'];
                        d['is_failed_query']=d['IS Failed Query'];
                        d['peak_comment']=d['Peak Comment'];
                        d['is_peak_comment']=d['IS Peak Comment'];
                        d['actual_concentration']=d['Actual Concentration'];
                        d['is_actual_concentration']=d['IS Actual Concentration'];
                        d['concentration_ratio']=d['Concentration Ratio'];
                        d['expected_rt']=d['Expected RT'];
                        d['is_expected_rt']=d['IS Expected RT'];
                        d['integration_type']=d['Integration Type'];
                        d['is_integration_type']=d['IS Integration Type'];
                        d['area']=d['Area'];
                        d['is_area']=d['IS Area'];
                        d['corrected_area']=d['Corrected Area'];
                        d['is_corrected_area']=d['IS Corrected Area'];
                        d['area_ratio']=d['Area Ratio'];
                        d['height']=d['Height'];
                        d['is_height']=d['IS Height'];
                        d['corrected_height']=d['Corrected Height'];
                        d['is_corrected_height']=d['IS Corrected Height'];
                        d['height_ratio']=d['Height Ratio'];
                        d['area_2_height']=d['Area / Height'];
                        d['is_area_2_height']=d['IS Area / Height'];
                        d['corrected_area2height']=d['Corrected Area/Height'];
                        d['is_corrected_area2height']=d['IS Corrected Area/Height'];
                        d['region_height']=d['Region Height'];
                        d['is_region_height']=d['IS Region Height'];
                        d['quality']=d['Quality'];
                        d['is_quality']=d['IS Quality'];
                        d['retention_time']=d['Retention Time'];
                        d['is_retention_time']=d['IS Retention Time'];
                        d['start_time']=d['Start Time'];
                        d['is_start_time']=d['IS Start Time'];
                        d['end_time']=d['End Time'];
                        d['is_end_time']=d['IS End Time'];
                        d['total_width']=d['Total Width'];
                        d['is_total_width']=d['IS Total Width'];
                        d['width_at_50']=d['Width at 50%'];
                        d['is_width_at_50']=d['IS Width at 50%'];
                        d['signal_2_noise']=d['Signal / Noise'];
                        d['is_signal_2_noise']=d['IS Signal / Noise'];
                        d['baseline_delta_2_height']=d['Baseline Delta / Height'];
                        d['is_baseline_delta_2_height']=d['IS Baseline Delta / Height'];
                        d['modified_']=d['Modified'];
                        d['relative_rt']=d['Relative RT'];
                        d['used_']=d['Used'];
                        d['calculated_concentration']=d['Calculated Concentration'];
                        d['accuracy_']=d['Accuracy'];
                        d['comment_']=d['Comment'];
                        d['use_calculated_concentration']=d['Use_Calculated_Concentration'];
                        data_add = data_stage01_quantification_MQResultsTable(d
                            #d['Index'],
                            #d['Sample Index'],
                            #d['Original Filename'],
                            #d['Sample Name'],
                            #d['Sample ID'],
                            #d['Sample Comment'],
                            #d['Sample Type'],
                            #d['Acquisition Date & Time'],
                            #d['Rack Number'],
                            #d['Plate Number'],
                            #d['Vial Number'],
                            #d['Dilution Factor'],
                            #d['Injection Volume'],
                            #d['Operator Name'],
                            #d['Acq. Method Name'],
                            #d['IS'],
                            #d['Component Name'],
                            #d['Component Index'],
                            #d['Component Comment'],
                            #d['IS Comment'],
                            #d['Mass Info'],
                            #d['IS Mass Info'],
                            #d['IS Name'],
                            #d['Component Group Name'],
                            #d['Conc. Units'],
                            #d['Failed Query'],
                            #d['IS Failed Query'],
                            #d['Peak Comment'],
                            #d['IS Peak Comment'],
                            #d['Actual Concentration'],
                            #d['IS Actual Concentration'],
                            #d['Concentration Ratio'],
                            #d['Expected RT'],
                            #d['IS Expected RT'],
                            #d['Integration Type'],
                            #d['IS Integration Type'],
                            #d['Area'],
                            #d['IS Area'],
                            #d['Corrected Area'],
                            #d['IS Corrected Area'],
                            #d['Area Ratio'],
                            #d['Height'],
                            #d['IS Height'],
                            #d['Corrected Height'],
                            #d['IS Corrected Height'],
                            #d['Height Ratio'],
                            #d['Area / Height'],
                            #d['IS Area / Height'],
                            #d['Corrected Area/Height'],
                            #d['IS Corrected Area/Height'],
                            #d['Region Height'],
                            #d['IS Region Height'],
                            #d['Quality'],
                            #d['IS Quality'],
                            #d['Retention Time'],
                            #d['IS Retention Time'],
                            #d['Start Time'],
                            #d['IS Start Time'],
                            #d['End Time'],
                            #d['IS End Time'],
                            #d['Total Width'],
                            #d['IS Total Width'],
                            #d['Width at 50%'],
                            #d['IS Width at 50%'],
                            #d['Signal / Noise'],
                            #d['IS Signal / Noise'],
                            #d['Baseline Delta / Height'],
                            #d['IS Baseline Delta / Height'],
                            #d['Modified'],
                            #d['Relative RT'],
                            #d['Used'],
                            #d['Calculated Concentration'],
                            #d['Accuracy'],
                            #d['Comment'],
                            #d['Use_Calculated_Concentration']
                            );
                    elif 'index_' in d:
                        data_add = data_stage01_quantification_MQResultsTable(d
                            #d['index_'],
                            #d['sample_index'],
                            #d['original_filename'],
                            #d['sample_name'],
                            #d['sample_id'],
                            #d['sample_comment'],
                            #d['sample_type'],
                            #d['acquisition_date_and_time'],
                            #d['rack_number'],
                            #d['plate_number'],
                            #d['vial_number'],
                            #d['dilution_factor'],
                            #d['injection_volume'],
                            #d['operator_name'],
                            #d['acq_method_name'],
                            #d['is_'],
                            #d['component_name'],
                            #d['component_index'],
                            #d['component_comment'],
                            #d['is_comment'],
                            #d['mass_info'],
                            #d['is_mass'],
                            #d['is_name'],
                            #d['component_group_name'],
                            #d['conc_units'],
                            #d['failed_query'],
                            #d['is_failed_query'],
                            #d['peak_comment'],
                            #d['is_peak_comment'],
                            #d['actual_concentration'],
                            #d['is_actual_concentration'],
                            #d['concentration_ratio'],
                            #d['expected_rt'],
                            #d['is_expected_rt'],
                            #d['integration_type'],
                            #d['is_integration_type'],
                            #d['area'],
                            #d['is_area'],
                            #d['corrected_area'],
                            #d['is_corrected_area'],
                            #d['area_ratio'],
                            #d['height'],
                            #d['is_height'],
                            #d['corrected_height'],
                            #d['is_corrected_height'],
                            #d['height_ratio'],
                            #d['area_2_height'],
                            #d['is_area_2_height'],
                            #d['corrected_area2height'],
                            #d['is_corrected_area2height'],
                            #d['region_height'],
                            #d['is_region_height'],
                            #d['quality'],
                            #d['is_quality'],
                            #d['retention_time'],
                            #d['is_retention_time'],
                            #d['start_time'],
                            #d['is_start_time'],
                            #d['end_time'],
                            #d['is_end_time'],
                            #d['total_width'],
                            #d['is_total_width'],
                            #d['width_at_50'],
                            #d['is_width_at_50'],
                            #d['signal_2_noise'],
                            #d['is_signal_2_noise'],
                            #d['baseline_delta_2_height'],
                            #d['is_baseline_delta_2_height'],
                            #d['modified_'],
                            #d['relative_rt'],
                            #d['used_'],
                            #d['calculated_concentration'],
                            #d['accuracy_'],
                            #d['comment_'],
                            #d['use_calculated_concentration'],
                            );
                    self.session.add(data_add);
                    cnt = cnt + 1;
                    if cnt > 1000: 
                        self.session.commit();
                        cnt = 0;
                except IntegrityError as e:
                    print(e);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01MQResultsTable(self,data_I):
        '''update rows of data_stage01_quantification_MQResultsTable'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_quantification_MQResultsTable).filter(
                            data_stage01_quantification_MQResultsTable.component_name.like(d['Component Name']),
                            data_stage01_quantification_MQResultsTable.sample_name.like(d['Sample Name']),
                            data_stage01_quantification_MQResultsTable.acquisition_date_and_time == d['Acquisition Date & Time']).update(
                            {'index_':d['Index'],
                            'sample_index':d['Sample Index'],
                            'original_filename':d['Original Filename'],
                            'sample_name':d['Sample Name'],
                            'sample_id':d['Sample ID'],
                            'sample_comment':d['Sample Comment'],
                            'sample_type':d['Sample Type'],
                            'acquisition_date_and_time':d['Acquisition Date & Time'],
                            'rack_number':d['Rack Number'],
                            'plate_number':d['Plate Number'],
                            'vial_number':d['Vial Number'],
                            'dilution_factor':d['Dilution Factor'],
                            'injection_volume':d['Injection Volume'],
                            'operator_name':d['Operator Name'],
                            'acq_method_name':d['Acq. Method Name'],
                            'is_':d['IS'],
                            'component_name':d['Component Name'],
                            'component_index':d['Component Index'],
                            'component_comment':d['Component Comment'],
                            'is_comment':d['IS Comment'],
                            'mass_info':d['Mass Info'],
                            'is_mass':d['IS Mass Info'],
                            'is_name':d['IS Name'],
                            'component_group_name':d['Component Group Name'],
                            'conc_units':d['Conc. Units'],
                            'failed_query':d['Failed Query'],
                            'is_failed_query':d['IS Failed Query'],
                            'peak_comment':d['Peak Comment'],
                            'is_peak_comment':d['IS Peak Comment'],
                            'actual_concentration':d['Actual Concentration'],
                            'is_actual_concentration':d['IS Actual Concentration'],
                            'concentration_ratio':d['Concentration Ratio'],
                            'expected_rt':d['Expected RT'],
                            'is_expected_rt':d['IS Expected RT'],
                            'integration_type':d['Integration Type'],
                            'is_integration_type':d['IS Integration Type'],
                            'area':d['Area'],
                            'is_area':d['IS Area'],
                            'corrected_area':d['Corrected Area'],
                            'is_corrected_area':d['IS Corrected Area'],
                            'area_ratio':d['Area Ratio'],
                            'height':d['Height'],
                            'is_height':d['IS Height'],
                            'corrected_height':d['Corrected Height'],
                            'is_corrected_height':d['IS Corrected Height'],
                            'height_ratio':d['Height Ratio'],
                            'area_2_height':d['Area / Height'],
                            'is_area_2_height':d['IS Area / Height'],
                            'corrected_area2height':d['Corrected Area/Height'],
                            'is_corrected_area2height':d['IS Corrected Area/Height'],
                            'region_height':d['Region Height'],
                            'is_region_height':d['IS Region Height'],
                            'quality':d['Quality'],
                            'is_quality':d['IS Quality'],
                            'retention_time':d['Retention Time'],
                            'is_retention_time':d['IS Retention Time'],
                            'start_time':d['Start Time'],
                            'is_start_time':d['IS Start Time'],
                            'end_time':d['End Time'],
                            'is_end_time':d['IS End Time'],
                            'total_width':d['Total Width'],
                            'is_total_width':d['IS Total Width'],
                            'width_at_50':d['Width at 50%'],
                            'is_width_at_50':d['IS Width at 50%'],
                            'signal_2_noise':d['Signal / Noise'],
                            'is_signal_2_noise':d['IS Signal / Noise'],
                            'baseline_delta_2_height':d['Baseline Delta / Height'],
                            'is_baseline_delta_2_height':d['IS Baseline Delta / Height'],
                            'modified_':d['Modified'],
                            'relative_rt':d['Relative RT'],
                            'used_':d['Used'],
                            'calculated_concentration':d['Calculated Concentration'],
                            'accuracy_':d['Accuracy'],
                            'comment_':d['Comment'],
                            'use_calculated_concentration':d['Use_Calculated_Concentration']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    # query data from data_stage01_quantification_mqresultstable
    # no other table dependencies
    def get_peakHeight_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Query peak height from sample name and component name
        NOTE: intended to be used within a for loop'''

        try:
            data = self.session.query(data_stage01_quantification_MQResultsTable.height).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
            if data:
                conc_O = data[0][0];
                conc_units_O = 'height';
            else: 
                conc_O = None;
                conc_units_O = None;
            return conc_O, conc_units_O;
        except SQLAlchemyError as e:
            print(e);
    def get_used_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Query used from sample name and component name
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_quantification_MQResultsTable.used_).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.component_name_name.like(component_name_name_I)).all();
            if data:
                used_O = data[0];
            else: used_O = None;
            return used_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Query peak information from sample name and component name
        NOTE: intended to be used within a for loop'''
        try:
            data = self.session.query(data_stage01_quantification_MQResultsTable).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
            data_O = {};
            if data:
                for d in data:
                    used_O=d.__repr__dict__();
            else: used_O = None;
            return used_O;
        except SQLAlchemyError as e:
            print(e);
    def get_peakInfo_sampleNameAndComponentName(self,sample_name_I,component_name_I,acquisition_date_and_time_I):
        '''Query peak information from sample name and component name
        NOTE: intended to be used within a for loop'''
        try:
            if acquisition_date_and_time_I[0] and acquisition_date_and_time_I[1]:
                data = self.session.query(data_stage01_quantification_MQResultsTable).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_quantification_MQResultsTable.acquisition_date_and_time>=acquisition_date_and_time_I[0],
                    data_stage01_quantification_MQResultsTable.acquisition_date_and_time<=acquisition_date_and_time_I[1],
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
            else:
                data = self.session.query(data_stage01_quantification_MQResultsTable).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
            data_O = {};
            if data:
                for d in data:
                    used_O={'acquisition_date_and_time':d.acquisition_date_and_time,
                    'component_name':d.component_name,
                    'component_group_name':d.component_group_name,
                    'area':d.area,
                    'height':d.height,
                    'retention_time':d.retention_time,
                    'start_time':d.start_time,
                    'end_time':d.end_time,
                    'total_width':d.total_width,
                    'width_at_50':d.width_at_50,
                    'signal_2_noise':d.signal_2_noise,
                    'baseline_delta_2_height':d.baseline_delta_2_height,
                    'relative_rt':d.relative_rt};
            else: used_O = None;
            return used_O;
        except SQLAlchemyError as e:
            print(e);
    # delete data from data_stage01_quantification_mqresultstable
    # no other table dependencies
    def delete_row_sampleName(self,sampleNames_I):
        '''Delete specific samples from an experiment by their sample ID from sample_physiologicalparameters'''
        deletes = [];
        for d in sampleNames_I:
            try:
                delete = self.session.query(data_stage01_quantification_MQResultsTable).filter(
                        data_stage01_quantification_MQResultsTable.sample_name.like(d['sample_name'])).delete(
                        synchronize_session=False);
                if delete == 0:
                    print('row not found')
                    print(d);
                deletes.append(delete);
            except SQLAlchemyError as e:
                print(e);
        self.session.commit();
    # query data from data_stage01_quantification_mqresultstable
    # requires quantitation_method
    def get_concAndConcUnits_sampleNameAndComponentName(self,sample_name_I,component_name_I):
        '''Query data (i.e. concentration, area/peak height ratio) from sample name and component name
        NOTE: intended to be used within a for loop'''
        # check for absolute or relative quantitation (i.e. area/peak height ratio)
        try:
            use_conc = self.session.query(data_stage01_quantification_MQResultsTable.use_calculated_concentration).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
            if use_conc:
                use_conc_O = use_conc[0][0];
            else: 
                use_conc_O = None;
        except SQLAlchemyError as e:
            print(e);

        if use_conc_O:
            try:
                data = self.session.query(data_stage01_quantification_MQResultsTable.calculated_concentration,
                        data_stage01_quantification_MQResultsTable.conc_units).filter(
                        data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                        data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                        data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
                if data:
                    conc_O = data[0][0];
                    conc_units_O = data[0][1];
                else: 
                    conc_O = None;
                    conc_units_O = None;
                return conc_O, conc_units_O;
            except SQLAlchemyError as e:
                print(e);

        else:
            # check for area or peak height ratio from quantitation_method
            try:
                data = self.session.query(quantitation_method.use_area).filter(
                        experiment.sample_name.like(sample_name_I),
                        experiment.quantitation_method_id.like(quantitation_method.id),
                        quantitation_method.component_name.like(component_name_I)).all();
                if data:
                    ratio_O = data[0][0];
                else: 
                    ratio_O = None;
            except SQLAlchemyError as e:
                print(e);

            if ratio_O:
                try:
                    data = self.session.query(data_stage01_quantification_MQResultsTable.area_ratio).filter(
                            data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                            data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                            data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
                    if data:
                        conc_O = data[0][0];
                        conc_units_O = 'area_ratio';
                    else: 
                        conc_O = None;
                        conc_units_O = None;
                    return conc_O, conc_units_O;
                except SQLAlchemyError as e:
                    print(e);
            else:
                try:
                    data = self.session.query(data_stage01_quantification_MQResultsTable.height_ratio).filter(
                            data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                            data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                            data_stage01_quantification_MQResultsTable.used_.is_(True)).all();
                    if data:
                        conc_O = data[0][0];
                        conc_units_O = 'height_ratio';
                    else: 
                        conc_O = None;
                        conc_units_O = None;
                    return conc_O, conc_units_O;
                except SQLAlchemyError as e:
                    print(e);

    # query component group names from data_stage01_quantification_mqresultstable
    def get_componentGroupNames_sampleName(self,sample_name_I):
        '''Query component group names that are used from the sample name
        NOTE: intended to be used within a for loop'''
        try:
            component_group_names = self.session.query(data_stage01_quantification_MQResultsTable.component_group_name).filter(
                    data_stage01_quantification_MQResultsTable.sample_name.like(sample_name_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).group_by(
                    data_stage01_quantification_MQResultsTable.component_group_name).order_by(
                    data_stage01_quantification_MQResultsTable.component_group_name.asc()).all();
            component_group_names_O = [];
            for cgn in component_group_names: component_group_names_O.append(cgn.component_group_name);
            return component_group_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentGroupName_experimentIDAndComponentName(self,experiment_id_I,component_name_I,exp_type_I=4):
        '''Query component group names that are used from the component name
        NOTE: intended to be used within a for loop'''
        try:
            component_group_name = self.session.query(data_stage01_quantification_MQResultsTable.component_group_name).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).group_by(
                    data_stage01_quantification_MQResultsTable.component_group_name).all();
            if len(component_group_name)>1:
                print('more than 1 component_group_name retrieved per component_name')
            component_group_name_O = component_group_name[0].component_group_name;
            return component_group_name_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample names from data_stage01_quantification_mqresultstable
    def get_sampleNames_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=4):
        '''Query sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_MQResultsTable.sample_name).filter(
                    data_stage01_quantification_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    #experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    data_stage01_quantification_MQResultsTable.sample_name).order_by(
                    data_stage01_quantification_MQResultsTable.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample names from data_stage01_quantification_mqresultstable
    def get_sampleNamesAndSampleIDs_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=4):
        '''Query sample names and sample ids (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(data_stage01_quantification_MQResultsTable.sample_name,
                    sample.sample_id).filter(
                    data_stage01_quantification_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    #experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                    experiment.sample_name.like(sample.sample_name)).group_by(
                    data_stage01_quantification_MQResultsTable.sample_name,
                    sample.sample_id).order_by(
                    data_stage01_quantification_MQResultsTable.sample_name.asc(),
                    sample.sample_id.asc()).all();
            sample_names_O = [];
            sample_ids_O = [];
            for sn in sample_names:
                sample_names_O.append(sn.sample_name);
                sample_ids_O.append(sn.sample_id);
            return sample_names_O,sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleID(self,experiment_id_I,sample_id_I,exp_type_I=4):
        '''Query sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample.sample_id.like(sample_id_I),
                    experiment.id.like(experiment_id_I),
                    #experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleIDAndSampleDilution(self,experiment_id_I,sample_id_I,sample_dilution_I,exp_type_I=4):
        '''Query sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample.sample_id.like(sample_id_I),
                    sample.sample_dilution == sample_dilution_I,
                    experiment.id.like(experiment_id_I),
                    #experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameShortAndSampleDescription(self,experiment_id_I,sample_name_short_I,sample_decription_I,exp_type_I=4):
        '''Query sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample_description.sample_name_short.like(sample_name_short_I),
                    sample_description.sample_desc.like(sample_decription_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDescription(self,experiment_id_I,sample_name_abbreviation_I,sample_decription_I,exp_type_I=4):
        '''Query sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample_description.sample_desc.like(sample_decription_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDilution(self,experiment_id_I,sample_name_abbreviation_I,sample_dilution_I,exp_type_I=4):
        '''Query sample names that are used from
        the experiment'''
        try:
            sample_names = self.session.query(sample.sample_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    sample.sample_dilution == sample_dilution_I,
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                    data_stage01_quantification_MQResultsTable.used_.is_(True)).group_by(
                    sample.sample_name).order_by(
                    sample.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample ids from data_stage01_quantification_mqresultstable
    def get_sampleIDs_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=4):
        '''Query sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_ids = self.session.query(sample.sample_id).filter(
                    data_stage01_quantification_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_id).order_by(
                    sample.sample_id.asc()).all();
            sample_ids_O = [];
            for si in sample_ids: sample_ids_O.append(si.sample_id);
            return sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleIDs_experimentID(self,experiment_id_I,exp_type_I=4):
        '''Query sample names that are used from the experiment'''
        try:
            sample_ids = self.session.query(sample.sample_id).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_id).order_by(
                    sample.sample_id.asc()).all();
            sample_ids_O = [];
            for si in sample_ids: sample_ids_O.append(si.sample_id);
            return sample_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleID_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=4):
        '''Query sample names (i.e. unknowns) that are used from
        the experiment'''
        try:
            sample_id = self.session.query(sample.sample_id).filter(
                    sample.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_id).all();
            sample_id_O = sample_id[0][0];
            return sample_id_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name short from data_stage01_quantification_mqresultstable
    def get_sampleNameShort_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=4):
        '''Query sample name short that are used from
        the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    sample.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_short).order_by(
                    sample_description.sample_name_short.asc()).all();
            sample_name_short_O = [];
            for sns in sample_name_short: sample_name_short_O.append(sns.sample_name_short);
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameShort_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=4):
        '''Query sample name short that are used from
        the experiment'''
        try:
            sample_name_short = self.session.query(sample_description.sample_name_short).filter(
                    sample.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_short).all();
            sample_name_short_O = sample_name_short[0];
            return sample_name_short_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample name abbreviations from data_stage01_quantification_mqresultstable
    def get_sampleNameAbbreviations_experimentIDAndSampleType(self,experiment_id_I,sample_type_I,exp_type_I=4):
        '''Query sample name abbreviations that are used from
        the experiment'''
        try:
            sample_name_abbreviations = self.session.query(sample_description.sample_name_abbreviation).filter(
                    sample.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample_description.sample_name_abbreviation).order_by(
                    sample_description.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            for sna in sample_name_abbreviations: sample_name_abbreviations_O.append(sna.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query dilutions from data_stage01_quantification_mqresultstable
    def get_sampleDilution_experimentIDAndSampleID(self,experiment_id_I,sample_id_I,exp_type_I=4):
        '''Query dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(sample.sample_dilution).filter(
                    sample.sample_id.like(sample_id_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_dilution).order_by(
                    sample.sample_dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.sample_dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleDilution_experimentIDAndSampleNameAbbreviation(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Query dilutions that are used from the experiment'''
        try:
            sample_dilutions = self.session.query(sample.sample_dilution).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample.sample_dilution).order_by(
                    sample.sample_dilution.asc()).all();
            sample_dilutions_O = [];
            for sd in sample_dilutions: sample_dilutions_O.append(sd.sample_dilution);
            return sample_dilutions_O;
        except SQLAlchemyError as e:
            print(e);
    # query time points from data_stage01_quantification_mqresultstable
    def get_timePoint_experimentIDAndSampleNameAbbreviation(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Query time points that are used from the experiment and sample name abbreviation'''
        try:
            time_points = self.session.query(sample_description.time_point).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    sample_description.time_point).order_by(
                    sample_description.time_point.asc()).all();
            time_points_O = [];
            for tp in time_points: time_points_O.append(tp.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query component names from data_stage01_quantification_mqresultstable
    def get_componentsNames_experimentIDAndSampleID(self,experiment_id_I,sample_id_I,exp_type_I=4):
        '''Query component names that are used and are not IS from
        the experiment and sample_id'''
        try:
            component_names = self.session.query(data_stage01_quantification_MQResultsTable.component_name).filter(
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    data_stage01_quantification_MQResultsTable.used_.is_(True),                   
                    data_stage01_quantification_MQResultsTable.is_.is_(False),
                    experiment.sample_name.like(sample.sample_name),
                    sample.sample_id.like(sample_id_I),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    data_stage01_quantification_MQResultsTable.component_name).order_by(
                    data_stage01_quantification_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleNameAbbreviation(self,experiment_id_I,sample_name_abbreviation_I,exp_type_I=4):
        '''Query component names that are used from
        the experiment and sample_name_abbreviation'''
        try:
            component_names = self.session.query(data_stage01_quantification_MQResultsTable.component_name).filter(
                    sample_description.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    sample.sample_id.like(sample_description.sample_id),
                    experiment.sample_name.like(sample.sample_name),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),                   
                    data_stage01_quantification_MQResultsTable.used_.is_(True),                   
                    data_stage01_quantification_MQResultsTable.is_.is_(False)).group_by(
                    data_stage01_quantification_MQResultsTable.component_name).order_by(
                    data_stage01_quantification_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=4):
        '''Query component names that are used and not internal standards from
        the experiment and sample_name'''
        try:
            component_names = self.session.query(data_stage01_quantification_MQResultsTable.component_name).filter(
                    experiment.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),                   
                    data_stage01_quantification_MQResultsTable.used_.is_(True),                   
                    data_stage01_quantification_MQResultsTable.is_.is_(False)).group_by(
                    data_stage01_quantification_MQResultsTable.component_name).order_by(
                    data_stage01_quantification_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNamesAndComponentGroupNames_experimentIDAndSampleName(self,experiment_id_I,sample_name_I,exp_type_I=4):
        '''Query component names that are used and not internal standards from
        the experiment and sample_name'''
        try:
            component_names = self.session.query(data_stage01_quantification_MQResultsTable.component_name,
                    data_stage01_quantification_MQResultsTable.component_group_name).filter(
                    experiment.sample_name.like(sample_name_I),
                    experiment.id.like(experiment_id_I),
                    experiment.exp_type_id == exp_type_I,
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),                   
                    data_stage01_quantification_MQResultsTable.used_.is_(True),                   
                    data_stage01_quantification_MQResultsTable.is_.is_(False)).group_by(
                    data_stage01_quantification_MQResultsTable.component_name,
                    data_stage01_quantification_MQResultsTable.component_group_name).order_by(
                    data_stage01_quantification_MQResultsTable.component_name.asc(),
                    data_stage01_quantification_MQResultsTable.component_group_name.asc()).all();
            component_names_O = [];
            component_group_names_O = [];
            for cn in component_names:
                component_names_O.append(cn.component_name);
                component_group_names_O.append(cn.component_group_name);
            return component_names_O,component_group_names_O;
        except SQLAlchemyError as e:
            print(e);
    def get_componentsNames_experimentIDAndSampleType(self,experiment_id_I,sample_type_I):
        '''Query component names that are used and not internal standards from
        the experiment and sample_name'''
        try:
            component_names = self.session.query(data_stage01_quantification_MQResultsTable.component_name).filter(
                    data_stage01_quantification_MQResultsTable.sample_type.like(sample_type_I),
                    experiment.id.like(experiment_id_I),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),         
                    data_stage01_quantification_MQResultsTable.used_.is_(True),                   
                    data_stage01_quantification_MQResultsTable.is_.is_(False)).group_by(
                    data_stage01_quantification_MQResultsTable.component_name).order_by(
                    data_stage01_quantification_MQResultsTable.component_name.asc()).all();
            component_names_O = [];
            for cn in component_names: component_names_O.append(cn.component_name);
            return component_names_O;
        except SQLAlchemyError as e:
            print(e);#,quant_method_id_I
    def get_sampleNames_QMethodIDAndComponentNameAndSampleType(self,quantitation_method_id_I,component_name_I,sample_type_I='Standard'):
        '''Query sample names (i.e. unknowns) that are used from
        the experiment by quantitation_method_id, component_name, and sample_type'''
        try:
            sample_names = self.session.query(data_stage01_quantification_MQResultsTable.sample_name).filter(
                    data_stage01_quantification_MQResultsTable.sample_type.like(sample_type_I),
                    data_stage01_quantification_MQResultsTable.component_name.like(component_name_I),
                    experiment.quantitation_method_id.like(quantitation_method_id_I),
                    data_stage01_quantification_MQResultsTable.used_.is_(True),
                    experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name)).group_by(
                    data_stage01_quantification_MQResultsTable.sample_name).order_by(
                    data_stage01_quantification_MQResultsTable.sample_name.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.sample_name);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);

    
    # query sample names from data_stage01_quantification_mqresultstable
    def getGroupJoin_experimentAndQuantitationMethodAndMQResultsTable_experimentID_dataStage01QuantificationMQResultsTable(self,
        experiment_id_I,
        sample_types_I=[],
        sample_names_I=[],
        sample_ids_I=[],
        component_names_I=[],
        ):
        '''Query sample names and sample ids (i.e. unknowns) that are used from
        the experiment'''
        try:
            cmd = '''SELECT quantitation_method.use_area, subquery1.sample_name, subquery1.sample_type, 
                subquery1.use_calculated_concentration, subquery1.sample_id, subquery1.component_name, 
                subquery1.component_group_name, subquery1.quantitation_method_id, subquery1.acquisition_date_and_time,
                subquery1.calculated_concentration, subquery1.height, subquery1.height_ratio, subquery1.area_ratio, subquery1.conc_units  
            FROM quantitation_method, (
                SELECT data_stage01_quantification_mqresultstable.sample_name, data_stage01_quantification_mqresultstable.sample_type,
                    data_stage01_quantification_mqresultstable.use_calculated_concentration, sample.sample_id,
                    data_stage01_quantification_mqresultstable.component_name, data_stage01_quantification_mqresultstable.component_group_name, 
                    experiment.quantitation_method_id, data_stage01_quantification_mqresultstable.acquisition_date_and_time, 
                    data_stage01_quantification_mqresultstable.calculated_concentration, data_stage01_quantification_mqresultstable.height,
                    data_stage01_quantification_mqresultstable.height_ratio, data_stage01_quantification_mqresultstable.area_ratio,
                    data_stage01_quantification_mqresultstable.conc_units
                FROM data_stage01_quantification_mqresultstable, sample, experiment 
                WHERE experiment.id LIKE '%s' AND data_stage01_quantification_mqresultstable.used_ IS true AND data_stage01_quantification_mqresultstable.is_ IS false AND experiment.sample_name LIKE data_stage01_quantification_mqresultstable.sample_name AND experiment.sample_name LIKE sample.sample_name 
                GROUP BY data_stage01_quantification_mqresultstable.sample_name, data_stage01_quantification_mqresultstable.sample_type, 
                    data_stage01_quantification_mqresultstable.use_calculated_concentration, sample.sample_id, 
                    data_stage01_quantification_mqresultstable.component_name, data_stage01_quantification_mqresultstable.component_group_name, 
                    experiment.quantitation_method_id, data_stage01_quantification_mqresultstable.acquisition_date_and_time, 
                    data_stage01_quantification_mqresultstable.calculated_concentration, data_stage01_quantification_mqresultstable.height,
                    data_stage01_quantification_mqresultstable.height_ratio, data_stage01_quantification_mqresultstable.area_ratio,
                    data_stage01_quantification_mqresultstable.conc_units 
                ORDER BY data_stage01_quantification_mqresultstable.sample_name ASC, sample.sample_id ASC, data_stage01_quantification_mqresultstable.component_name ASC, data_stage01_quantification_mqresultstable.component_group_name ASC
                ) subquery1
            WHERE quantitation_method.component_name LIKE subquery1.component_name AND quantitation_method.id LIKE subquery1.quantitation_method_id 
            GROUP BY subquery1.sample_name, subquery1.sample_type, subquery1.use_calculated_concentration, 
                subquery1.sample_id, subquery1.component_name, subquery1.component_group_name, quantitation_method.use_area, subquery1.quantitation_method_id, subquery1.acquisition_date_and_time,
                subquery1.calculated_concentration, subquery1.height, subquery1.height_ratio, subquery1.area_ratio, subquery1.conc_units 
            ORDER BY subquery1.sample_name ASC, subquery1.sample_id ASC, subquery1.component_name ASC, subquery1.component_group_name ASC, subquery1.acquisition_date_and_time ASC 
            ''' % (experiment_id_I);
            result = self.session.execute(cmd);
            data = result.fetchall();
            #data = self.session.query(data_stage01_quantification_MQResultsTable.sample_name,
            #        data_stage01_quantification_MQResultsTable.sample_type,
            #        data_stage01_quantification_MQResultsTable.use_calculated_concentration,
            #        sample.sample_id,
            #        data_stage01_quantification_MQResultsTable.component_name,
            #        data_stage01_quantification_MQResultsTable.component_group_name,
            #        #quantitation_method.use_area,
            #        experiment.quantitation_method_id
            #        ).filter(
            #        experiment.id.like(experiment_id_I),
            #        data_stage01_quantification_MQResultsTable.used_.is_(True),
            #        data_stage01_quantification_MQResultsTable.is_.is_(False),
            #        experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
            #        experiment.sample_name.like(sample.sample_name),
            #        #data_stage01_quantification_MQResultsTable.component_name.like(quantitation_method.component_name),
            #        #experiment.quantitation_method_id.like(quantitation_method.id)
            #        ).group_by(
            #        data_stage01_quantification_MQResultsTable.sample_name,
            #        data_stage01_quantification_MQResultsTable.sample_type,
            #        data_stage01_quantification_MQResultsTable.use_calculated_concentration,
            #        sample.sample_id,
            #        data_stage01_quantification_MQResultsTable.component_name,
            #        data_stage01_quantification_MQResultsTable.component_group_name,
            #        #quantitation_method.use_area,
            #        experiment.quantitation_method_id
            #        ).order_by(
            #        data_stage01_quantification_MQResultsTable.sample_name.asc(),
            #        sample.sample_id.asc(),
            #        data_stage01_quantification_MQResultsTable.component_name.asc(),
            #        data_stage01_quantification_MQResultsTable.component_group_name.asc()
            #        ).all();
            data_O = [];
            if data:
                data_O = listDict(record_I=data);
                data_O.convert_record2DataFrame();
                data_O.filterIn_byDictList({
                                            'sample_id':sample_ids_I,
                                            'sample_name':sample_names_I,
                                            'sample_type':sample_types_I,
                                            'component_name':component_names_I,
                                           });
            return data_O;
        except SQLAlchemyError as e:
            print(e);

