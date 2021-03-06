﻿from .lims_quantitationMethod_postgresql_models import *
from .stage01_quantification_MQResultsTable_postgresql_models import *
#from .lims_msMethod_query import lims_msMethod_query
from SBaaS_LIMS.lims_calibratorsAndMixes_query import lims_calibratorsAndMixes_query
from SBaaS_LIMS.lims_experiment_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class lims_quantitationMethod_query(
            lims_calibratorsAndMixes_query,
            #lims_msMethod_query,
            sbaas_template_query,
                                    ):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'quantitation_method':quantitation_method,
                            'quantitation_method_list':quantitation_method_list
                        };
        self.set_supportedTables(tables_supported);
        
    def reset_lims_quantitationMethod(self,
            tables_I = [],
            quantitation_method_id_I = None,
            warn_I=True):
        try:
            if not tables_I:
                tables_I = list(self.get_supportedTables().keys());
            querydelete = sbaas_base_query_delete(session_I=self.session,engine_I=self.engine,settings_I=self.settings,data_I=self.data);
            for table in tables_I:
                if table == 'quantitation_method':
                    query = {};
                    query['delete_from'] = [{'table_name':table}];
                    query['where'] = [{
                            'table_name':table,
                            'column_name':'id',
                            'value':quantitation_method_id_I,
		                    'operator':'LIKE',
                            'connector':'AND'
                            }
	                    ];
                elif table == 'quantitation_method_list':
                    query = {};
                    query['delete_from'] = [{'table_name':table}];
                    query['where'] = [{
                            'table_name':table,
                            'column_name':'quantitation_method_id',
                            'value':quantitation_method_id_I,
		                    'operator':'LIKE',
                            'connector':'AND'
                            }
	                    ];
                table_model = self.convert_tableStringList2SqlalchemyModelDict([table]);
                query = querydelete.make_queryFromString(table_model,query);
                querydelete.reset_table_sqlalchemyModel(query_I=query,warn_I=warn_I);
        except Exception as e:
            print(e);
    #def reset_lims_quantitationMethod(self,quantitation_method_id_I=None):
    #    try:
    #        if quantitation_method_id_I:
    #            reset = self.session.query(quantitation_method).filter(quantitation_method.id.like(quantitation_method_id_I)).delete(synchronize_session=False);
    #            reset = self.session.query(quantitation_method_list).filter(
    #                quantitation_method_list.quantitation_method_id.like(quantitation_method_id_I)).delete(synchronize_session=False);
    #        else:
    #            reset = self.session.query(quantitation_method).delete(synchronize_session=False);
    #            reset = self.session.query(quantitation_method_list).delete(synchronize_session=False);
    #        self.session.commit();
    #    except SQLAlchemyError as e:
    #        print(e);;

    def add_quantitationMethod(self, QMethod_id_I, data_I):
        '''add rows of quantitation_method'''
        if data_I:
            for d in data_I:
                if not d['IS'] or d['IS'] == 'False': # ignore internal standards
                    try:
                        d['id']=QMethod_id_I;
                        d['q1_mass']=d['Q1 Mass - 1']
                        d['q3_mass']=d['Q3 Mass - 1']
                        d['met_id']=d['Group Name']
                        d['component_name']=d['Name']
                        d['is_name']=d['IS Name']
                        d['fit']=d['Regression Type']
                        d['weighting']=d['Regression Weighting']
                        d['intercept']=None
                        d['slope']=None
                        d['correlation']=None
                        d['use_area']=d['Use Area']
                        d['lloq']=None
                        d['uloq']=None
                        d['points']=None

                        data_add = quantitation_method(d
                            #QMethod_id_I,
                            #d['Q1 Mass - 1'],
                            #d['Q3 Mass - 1'],
                            #d['Group Name'],
                            #d['Name'],
                            #d['IS Name'],
                            #d['Regression Type'],
                            #d['Regression Weighting'],
                            #None,
                            #None,
                            #None,
                            #d['Use Area'],
                            #None,
                            #None,
                            #None
                                                    );
                        self.session.add(data_add);
                    except SQLAlchemyError as e:
                        print(e);
            self.session.commit();

    def get_quantMethodIds(self):
        '''Query quantitation method IDs that do not have regression parameters
        Note: correlation==Null is used to identify which quantitation method
              IDs do not have regression parameters'''
        quant_method_ids = self.session.query(quantitation_method.id).filter(
                    quantitation_method.correlation.is_(None)).group_by(
                    quantitation_method.id).all();
        quant_method_ids_O = [];
        for id in quant_method_ids: quant_method_ids_O.append(id.id);
        return quant_method_ids_O;

    def get_quantSamplesAndComponents(self, quant_method_id_I):
        '''Query calibrator samples and components that were used
        for calibration
        NOTE: can be used within a loop if multiple
        there are multiple quantitation ids
        input:
        quantitation_method_id
        ouput:
        calibrators_samples
        calibrators_components
        '''
        # query experiment and samples that were used to create the given calibration method
        calibrators_samples = self.session.query(data_stage01_quantification_MQResultsTable.sample_name).filter(
                             quantitation_method.id==experiment.quantitation_method_id,
                             experiment.sample_name==data_stage01_quantification_MQResultsTable.sample_name,
                             data_stage01_quantification_MQResultsTable.sample_type.like('Standard'),
                             data_stage01_quantification_MQResultsTable.used_,
                             quantitation_method.id.like(quant_method_id_I)).group_by(
                             data_stage01_quantification_MQResultsTable.sample_name).subquery('calibrators_samples');
        # query components from quantitation method that were used to create the given calibration method
        calibrators_components = self.session.query(data_stage01_quantification_MQResultsTable.component_name).filter(
                            data_stage01_quantification_MQResultsTable.used_.is_(True),
                            data_stage01_quantification_MQResultsTable.is_.isnot(True), 
                            data_stage01_quantification_MQResultsTable.sample_name.like(calibrators_samples.c.sample_name)).group_by(
                            data_stage01_quantification_MQResultsTable.component_name).all(); #subquery('calibrators_components');
        #calibrators_components = self.session.query(quantitation_method.component_name).filter(
        #                    quantitation_method.id.like(quant_method_id_I)).group_by(
        #                    quantitation_method.component_name).all(); #subquery('calibrators_components');
        component_names_O = [];
        for cn in calibrators_components: 
            component_names_O.append(cn.component_name);
        return calibrators_samples, component_names_O;
    def get_quantMethodParameters(self, quant_method_id_I, component_name_I):
        '''Query calibration parameters for a given component
        from a specified quantitation method id

         input:
               component_name
               quantitation_method_id
         ouput:
               fit
               weighting
               use_area
        '''
        calibrators_parameters = self.session.query(quantitation_method.component_name,
                            quantitation_method.fit,quantitation_method.weighting,
                            quantitation_method.use_area).filter(
                            quantitation_method.id.like(quant_method_id_I),
                            quantitation_method.component_name.like(component_name_I)).first();
        fit_O = calibrators_parameters.fit;
        weighting_O = calibrators_parameters.weighting;
        use_area_O = calibrators_parameters.use_area;

        return fit_O, weighting_O, use_area_O;
    def update_quantitationMethod(self, quant_method_id_I, component_name_I, 
                                  slope_I, intercept_I, correlation_I, lloq_I, uloq_I, points_I):
        try:
            quant_method_update = self.session.query(quantitation_method).filter(
                 quantitation_method.id.like(quant_method_id_I),
                 quantitation_method.component_name.like(component_name_I)).update(
                 {'slope': slope_I,'intercept':intercept_I,'correlation':correlation_I,
                  'lloq':lloq_I,'uloq':uloq_I,'points':points_I},synchronize_session=False);
            self.session.commit(); # could possible move if efficiency is poor
        except SQLAlchemyError as e:
            print(e);
    
    def get_components(self,quant_method_id_I):
        '''Query calibrator components that are in the calibration method
        NOTE: can be used within a loop if multiple
        there are multiple quantitation ids
         input:
               quantitation_method_id
         ouput:
               calibrators_components
        '''
        # query experiment and samples that were used to create the given calibration method
        try:
            calibrators_components = self.session.query(quantitation_method.component_name).filter(
                                quantitation_method.id.like(quant_method_id_I)).group_by(
                                quantitation_method.component_name).all();
            component_names_O = [];
            for cn in calibrators_components: component_names_O.append(cn.component_name);
            return component_names_O;

        except SQLAlchemyError as e:
            print(e);
    def get_allComponents(self):
        '''Query calibrator components that are in all of the calibration methods
        NOTE: can be used within a loop if multiple
        there are multiple quantitation ids
         input:
               quantitation_method_id
         ouput:
               calibrators_components
        '''
        # query experiment and samples that were used to create the given calibration method
        try:
            calibrators_components = self.session.query(quantitation_method.component_name).group_by(
                                quantitation_method.component_name).all();
            component_names_O = [];
            for cn in calibrators_components: component_names_O.append(cn.component_name);
            return component_names_O;

        except SQLAlchemyError as e:
            print(e);
    def get_allQuantMethodIds(self):
        '''Query quantitation method IDs that do not have regression parameters
        Note: correlation==Null is used to identify which quantitation method
              IDs do not have regression parameters'''
        try:
            quant_method_ids = self.session.query(quantitation_method.id).group_by(
                        quantitation_method.id).all();
            quant_method_ids_O = [];
            for id in quant_method_ids: quant_method_ids_O.append(id.id);
            return quant_method_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_quantMethodRegression(self, quant_method_id_I, component_name_I):
        '''Query calibration parameters for a given component
        from a specified quantitation method id

         input:
               component_name
               quantitation_method_id
         ouput:
               intercept
               slope
               correlation
               lloq
               uloq
               points
        '''

        try:
            calibrators_parameters = self.session.query(quantitation_method.intercept,
                                quantitation_method.slope,
                                quantitation_method.correlation,
                                quantitation_method.lloq,
                                quantitation_method.uloq,
                                quantitation_method.points,
                                quantitation_method.slope).filter(
                                quantitation_method.id.like(quant_method_id_I),
                                quantitation_method.component_name.like(component_name_I)).first();
                                #first(): primary key(quant_method_id,component_name)
            if calibrators_parameters:
                intercept_O = calibrators_parameters.intercept;
                slope_O = calibrators_parameters.slope;
                correlation_O = calibrators_parameters.correlation;
                lloq_O = calibrators_parameters.lloq;
                uloq_O = calibrators_parameters.uloq;
                points_O = calibrators_parameters.points;
                if (slope_O and intercept_O and correlation_O and lloq_O and uloq_O and points_O):
                    return slope_O, intercept_O, correlation_O, lloq_O, uloq_O, points_O;
                else:
                    return 0,0,0,0,0,0;
            else:
                return 0,0,0,0,0,0;

        except SQLAlchemyError as e:
            print(e);
    def get_quantMethodInfo(self,calibrator_samples,use_area_I,component_name_I):
        '''Query calibrators by calibrator_samples
        INPUT:
        calibrator_samples = calibrator_table object'''
        try:
            # query calibrators for specific component_name from specific experiment_id
            if use_area_I:
                calibrators = self.session.query(data_stage01_quantification_MQResultsTable.actual_concentration,
                                            data_stage01_quantification_MQResultsTable.area_ratio,
                                            data_stage01_quantification_MQResultsTable.dilution_factor).filter(
                                         data_stage01_quantification_MQResultsTable.sample_name.like(calibrator_samples.c.sample_name),
                                         data_stage01_quantification_MQResultsTable.used_.is_(True),
                                         data_stage01_quantification_MQResultsTable.is_.isnot(True),
                                         data_stage01_quantification_MQResultsTable.component_name.like(component_name_I)).all();
            else:
                calibrators = self.session.query(data_stage01_quantification_MQResultsTable.actual_concentration,
                                            data_stage01_quantification_MQResultsTable.height_ratio,
                                            data_stage01_quantification_MQResultsTable.dilution_factor).filter(
                                         data_stage01_quantification_MQResultsTable.sample_name.like(calibrator_samples.c.sample_name),
                                         data_stage01_quantification_MQResultsTable.used_.is_(True),
                                         data_stage01_quantification_MQResultsTable.is_.isnot(True),
                                         data_stage01_quantification_MQResultsTable.component_name.like(component_name_I)).all();
            actual_concentration_O = [];
            ratio_O = [];
            dilution_factor_O = [];
            if calibrators:
                for c in calibrators:
                    actual_concentration_O.append(c.actual_concentration);
                    if use_area_I: ratio_O.append(c.area_ratio);
                    else: ratio_O.append(c.height_ratio);
                    dilution_factor_O.append(c.dilution_factor);
            return actual_concentration_O,ratio_O,dilution_factor_O;
        except SQLAlchemyError as e:
            print(e);
    def get_quantMethodInfo_dict(self,calibrator_samples,use_area_I,component_name_I):
        '''Query rows
        INPUT:
        calibrator_samples = calibrator_table object'''
        try:
            # query calibrators for specific component_name from specific experiment_id
            if use_area_I:
                calibrators = self.session.query(data_stage01_quantification_MQResultsTable.actual_concentration,
                                            data_stage01_quantification_MQResultsTable.area_ratio,
                                            data_stage01_quantification_MQResultsTable.dilution_factor).filter(
                                         data_stage01_quantification_MQResultsTable.sample_name.like(calibrator_samples.c.sample_name),
                                         data_stage01_quantification_MQResultsTable.used_.is_(True),
                                         data_stage01_quantification_MQResultsTable.is_.isnot(True),
                                         data_stage01_quantification_MQResultsTable.component_name.like(component_name_I)).all();
            else:
                calibrators = self.session.query(data_stage01_quantification_MQResultsTable.actual_concentration,
                                            data_stage01_quantification_MQResultsTable.height_ratio,
                                            data_stage01_quantification_MQResultsTable.dilution_factor).filter(
                                         data_stage01_quantification_MQResultsTable.sample_name.like(calibrator_samples.c.sample_name),
                                         data_stage01_quantification_MQResultsTable.used_.is_(True),
                                         data_stage01_quantification_MQResultsTable.is_.isnot(True),
                                         data_stage01_quantification_MQResultsTable.component_name.like(component_name_I)).all();
            rows_O = [];
            if calibrators:
                for c in calibrators:
                    tmp = {};
                    tmp['actual_concentration']=c.actual_concentration;
                    if use_area_I: tmp['ratio']=c.area_ratio;
                    else: tmp['ratio']=c.height_ratio;
                    tmp['dilution_factor']=c.dilution_factor;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def get_row_QMethodIDAndComponentNamequantitationMethod(self, quant_method_id_I, component_name_I):
        '''Query calibration parameters for a given component
        from a specified quantitation method id

         input:
               component_name
               quantitation_method_id
         ouput:
               intercept
               slope
               correlation
               lloq
               uloq
               points
        '''
        try:
            row = self.session.query(quantitation_method).filter(
                                quantitation_method.id.like(quant_method_id_I),
                                quantitation_method.component_name.like(component_name_I)).first();
                                #first(): primary key(quant_method_id,component_name)
            row_O = {};
            if row:
                row_O = row.__repr__dict__();
            return row_O;

        except SQLAlchemyError as e:
            print(e);
    # QC queries from quantitation_method
    def get_LLOQAndULOQ(self,
        experiment_id_I,
        sample_names_I=[],
        component_names_I=[],
        component_group_names_I=[],
        calculated_concentration_units_I=[],
        sample_types_I = ['Unknown','Quality Control']
        ):
        '''query to populate the "checkLLOQAndULOQ" view
        TODO: appears to be broken'''
        try:
            #data = self.session.query(data_stage01_quantification_MQResultsTable.sample_name, 
            #            data_stage01_quantification_MQResultsTable.component_group_name, 
            #            data_stage01_quantification_MQResultsTable.component_name, 
            #            data_stage01_quantification_MQResultsTable.calculated_concentration, 
            #            data_stage01_quantification_MQResultsTable.conc_units, 
            #            quantitation_method.correlation, 
            #            quantitation_method.lloq, 
            #            quantitation_method.uloq, 
            #            quantitation_method.points,
            #            data_stage01_quantification_MQResultsTable.used_).filter(
            #            experiment.id.like(experiment_id_I),
            #            experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
            #            experiment.quantitation_method_id.like(quantitation_method.id),
            #            data_stage01_quantification_MQResultsTable.component_name.like(quantitation_method.component_name),
            #            data_stage01_quantification_MQResultsTable.used_,
            #            data_stage01_quantification_MQResultsTable.is_.is_(False),
            #            quantitation_method.points > 0,
            #            or_(data_stage01_quantification_MQResultsTable.sample_type.like('Unknown'),
            #                data_stage01_quantification_MQResultsTable.sample_type.like('Quality Control'))).order_by(
            #            data_stage01_quantification_MQResultsTable.component_name.asc(),
            #            data_stage01_quantification_MQResultsTable.sample_name.asc()).all();
            #check_O = [];
            #for c in data: 
            #    check_1 = {};
            #    check_1['sample_name'] = c.sample_name;
            #    check_1['component_group_name'] = c.component_group_name;
            #    check_1['component_name'] = c.component_name;
            #    check_1['calculated_concentration'] = c.calculated_concentration;
            #    check_1['calculated_concentration_units'] = c.conc_units;
            #    check_1['correlation'] = c.correlation;
            #    check_1['lloq'] = c.lloq;
            #    check_1['uloq'] = c.uloq;
            #    check_1['points'] = c.points;
            #    check_1['used_'] = c.used_;
            #    check_O.append(check_1);
            #return  check_O;

            subquery1 = '''SELECT experiment.id as experiment_id, 
                experiment.sample_name, 
                experiment.quantitation_method_id '''
            subquery1 += '''FROM experiment '''
            subquery1 += '''WHERE ''' 
            if experiment_id_I:
                cmd_q = '''experiment.id =ANY ('{%s}'::text[]) ''' %(
                    self.convert_list2string(experiment_id_I));
                subquery1+=cmd_q;
            if sample_names_I:
                cmd_q = '''AND experiment.sample_name =ANY ('{%s}'::text[]) ''' %(
                    self.convert_list2string(sample_names_I));
                subquery1+=cmd_q;
            subquery1 += '''ORDER BY experiment.id ASC, 
                        experiment.sample_name, 
                        experiment.quantitation_method_id '''

            subquery2 = '''SELECT subquery1.experiment_id,
                subquery1.sample_name,
                subquery1.quantitation_method_id,
                "data_stage01_quantification_mqresultstable".component_name, 
                "data_stage01_quantification_mqresultstable".component_group_name, 
                "data_stage01_quantification_mqresultstable".calculated_concentration,
                "data_stage01_quantification_mqresultstable".conc_units AS calculated_concentration_units,  
                "data_stage01_quantification_mqresultstable".used_  
                '''
            subquery2 += '''FROM "data_stage01_quantification_mqresultstable", 
                         (%s) AS subquery1 ''' %subquery1
            subquery2 += '''WHERE "data_stage01_quantification_mqresultstable".used_ 
                    AND NOT "data_stage01_quantification_mqresultstable".is_ 
                    AND "data_stage01_quantification_mqresultstable".sample_name = subquery1.sample_name '''
            if sample_types_I:
                cmd_q = '''AND "data_stage01_quantification_mqresultstable".sample_type =ANY ('{%s}'::text[]) ''' %(
                    self.convert_list2string(sample_types_I));
                subquery2+=cmd_q;
            if component_names_I:
                cmd_q = '''AND "data_stage01_quantification_mqresultstable".component_name =ANY ('{%s}'::text[]) ''' %(
                    self.convert_list2string(component_names_I));
                subquery2+=cmd_q;
            if component_group_names_I:
                cmd_q = '''AND "data_stage01_quantification_mqresultstable".component_group_name =ANY ('{%s}'::text[]) ''' %(
                    self.convert_list2string(component_group_names_I));
                subquery2+=cmd_q;
            if calculated_concentration_units_I:
                cmd_q = '''AND "data_stage01_quantification_mqresultstable".conc_units =ANY ('{%s}'::text[]) ''' %(
                    self.convert_list2string(calculated_concentration_units_I));
                subquery2+=cmd_q;
            subquery2 += '''GROUP BY subquery1.experiment_id,
                subquery1.sample_name,
                subquery1.quantitation_method_id,
                "data_stage01_quantification_mqresultstable".component_name, 
                "data_stage01_quantification_mqresultstable".component_group_name, 
                "data_stage01_quantification_mqresultstable".calculated_concentration,
                "data_stage01_quantification_mqresultstable".conc_units,  
                "data_stage01_quantification_mqresultstable".used_  
                '''
            subquery2 += '''ORDER BY subquery1.experiment_id ASC,
                subquery1.sample_name ASC,
                subquery1.quantitation_method_id ASC,
                "data_stage01_quantification_mqresultstable".component_name ASC, 
                "data_stage01_quantification_mqresultstable".component_group_name ASC, 
                "data_stage01_quantification_mqresultstable".calculated_concentration ASC,
                "data_stage01_quantification_mqresultstable".conc_units ASC,  
                "data_stage01_quantification_mqresultstable".used_ ASC
                '''

            query1 = '''SELECT subquery2.experiment_id,
                subquery2.sample_name,
                subquery2.quantitation_method_id,
                "subquery2".component_name, 
                "subquery2".component_group_name, 
                "subquery2".calculated_concentration,
                "subquery2".calculated_concentration_units,  
                "subquery2".used_, 
                quantitation_method.correlation, 
                quantitation_method.lloq, 
                quantitation_method.uloq, 
                quantitation_method.points
                '''
            query1 += '''FROM quantitation_method, 
                (%s) AS subquery2 ''' %subquery2
            query1 += '''WHERE quantitation_method.id = subquery2.quantitation_method_id 
                AND quantitation_method.component_name = subquery2.component_name 
                AND quantitation_method.points > 0 '''
            query1 += '''GROUP BY subquery2.experiment_id,
                subquery2.sample_name,
                subquery2.quantitation_method_id,
                "subquery2".component_name, 
                "subquery2".component_group_name, 
                "subquery2".calculated_concentration,
                "subquery2".calculated_concentration_units,  
                "subquery2".used_, 
                quantitation_method.correlation, 
                quantitation_method.lloq, 
                quantitation_method.uloq, 
                quantitation_method.points
                '''
            query1 += '''ORDER BY subquery2.experiment_id ASC,
                subquery2.sample_name ASC,
                subquery2.quantitation_method_id ASC,
                "subquery2".component_name ASC, 
                "subquery2".component_group_name ASC, 
                "subquery2".calculated_concentration ASC,
                "subquery2".calculated_concentration_units ASC,  
                "subquery2".used_ ASC, 
                quantitation_method.correlation ASC, 
                quantitation_method.lloq ASC, 
                quantitation_method.uloq ASC, 
                quantitation_method.points ASC
                '''
    
            result = self.session.execute(query1);
            data = result.fetchall();
            data_O = [dict(d) for d in data];
            return data_O;
        except SQLAlchemyError as e:
            print(e);
        return
    def get_checkLLOQAndULOQ(self,experiment_id_I):
        '''query to populate the "checkLLOQAndULOQ" view'''
        try:
            check = self.session.query(data_stage01_quantification_MQResultsTable.sample_name, 
                        data_stage01_quantification_MQResultsTable.component_group_name, 
                        data_stage01_quantification_MQResultsTable.component_name, 
                        data_stage01_quantification_MQResultsTable.calculated_concentration, 
                        data_stage01_quantification_MQResultsTable.conc_units, 
                        quantitation_method.correlation, 
                        quantitation_method.lloq, 
                        quantitation_method.uloq, 
                        quantitation_method.points,
                        data_stage01_quantification_MQResultsTable.used_).filter(
                        experiment.id.like(experiment_id_I),
                        experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                        experiment.quantitation_method_id.like(quantitation_method.id),
                        data_stage01_quantification_MQResultsTable.component_name.like(quantitation_method.component_name),
                        data_stage01_quantification_MQResultsTable.used_.is_(True),
                        data_stage01_quantification_MQResultsTable.is_.is_(False),
                        quantitation_method.points > 0,
                        or_(data_stage01_quantification_MQResultsTable.sample_type.like('Unknown'),
                        data_stage01_quantification_MQResultsTable.sample_type.like('Quality Control')),
                        or_(data_stage01_quantification_MQResultsTable.calculated_concentration < quantitation_method.lloq,
                        data_stage01_quantification_MQResultsTable.calculated_concentration > quantitation_method.uloq)).order_by(
                        data_stage01_quantification_MQResultsTable.component_name.asc(),
                        data_stage01_quantification_MQResultsTable.sample_name.asc()).all();
            check_O = [];
            for c in check: 
                check_1 = {};
                check_1['sample_name'] = c.sample_name;
                check_1['component_group_name'] = c.component_group_name;
                check_1['component_name'] = c.component_name;
                check_1['calculated_concentration'] = c.calculated_concentration;
                check_1['calculated_concentration'] = c.conc_units;
                check_1['correlation'] = c.correlation;
                check_1['lloq'] = c.lloq;
                check_1['uloq'] = c.uloq;
                check_1['points'] = c.points;
                check_1['used'] = c.used_;
                check_O.append(check_1);
            return  check_O;
        except SQLAlchemyError as e:
            print(e);
        return
    def get_checkISMatch(self,experiment_id_I):
        '''query to populate the "checkISMatch" view'''
        try:
            check = self.session.query(data_stage01_quantification_MQResultsTable.sample_name, 
                        data_stage01_quantification_MQResultsTable.component_name, 
                        data_stage01_quantification_MQResultsTable.calculated_concentration, 
                        data_stage01_quantification_MQResultsTable.is_name.label('IS_name_samples'), 
                        quantitation_method.is_name.label('IS_name_calibrators')).filter(
                        experiment.id.like(experiment_id_I),
                        experiment.sample_name.like(data_stage01_quantification_MQResultsTable.sample_name),
                        experiment.quantitation_method_id.like(quantitation_method.id),
                        data_stage01_quantification_MQResultsTable.component_name.like(quantitation_method.component_name),
                        data_stage01_quantification_MQResultsTable.used_.is_(True),
                        data_stage01_quantification_MQResultsTable.is_.is_(False),
                        or_(data_stage01_quantification_MQResultsTable.sample_type.like('Unknown'),
                        data_stage01_quantification_MQResultsTable.sample_type.like('Quality Control')),
                        ~(data_stage01_quantification_MQResultsTable.is_name.like(quantitation_method.is_name)),
                        quantitation_method.component_name.like(data_stage01_quantification_MQResultsTable.component_name)).order_by(
                        data_stage01_quantification_MQResultsTable.component_name.asc(),
                        data_stage01_quantification_MQResultsTable.sample_name.asc()).all();
            check_O = [];
            for c in check: 
                check_1 = {};
                check_1['sample_name'] = c.sample_name;
                check_1['component_name'] = c.component_name;
                check_1['IS_name_samples'] = c.IS_name_samples;
                check_1['IS_name_calibrators'] = c.IS_name_calibrators;
                check_O.append(check_1);
            return  check_O;
        except SQLAlchemyError as e:
            print(e);
        return