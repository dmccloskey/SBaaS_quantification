
from .stage01_quantification_QCs_io import stage01_quantification_QCs_io
from SBaaS_LIMS.lims_experiment_query import lims_experiment_query
# resources
from python_statistics.calculate_interface import calculate_interface

class stage01_quantification_QCs_execute(stage01_quantification_QCs_io,
                                                    lims_experiment_query):
    def execute_analyzeQCs(self,experiment_id_I,sample_types_I=['QC']):
        '''calculate the average and coefficient of variation for QCs
        NOTE: analytical replicates are those samples with the same 
        sample_id (but different sample_name)'''
        # Input:
        #   experiment_id
        # Output:
        #   sample_name
        #   component_group_name
        #   component_name
        #   n_replicates
        #   conc_average
        #   conc_CV
        #   conc_units
        calc = calculate_interface();
        
        print('execute_analyzeQCs...')
        # get sample name abbreviations
        sample_name_abbreviations = [];
        data_O = [];
        for st in sample_types_I:
            sample_name_abbreviations_tmp = [];
            sample_name_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleType(experiment_id_I,st);
            sample_name_abbreviations.extend(sample_name_abbreviations_tmp);
        # create database table
        for sna in sample_name_abbreviations:
            # get dilutions
            sample_dilutions = [];
            sample_dilutions = self.get_sampleDilution_experimentIDAndSampleNameAbbreviation(experiment_id_I,sna);
            # get component names
            component_names = [];
            component_names = self.get_componentsNames_experimentIDAndSampleNameAbbreviation(experiment_id_I,sna);
            for cn in component_names:
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName(experiment_id_I,cn);
                for sd in sample_dilutions:
                    # get sample names
                    sample_names = [];
                    sample_names = self.get_sampleNames_experimentIDAndSampleNameAbbreviationAndSampleDilution(experiment_id_I,sna,sd);
                    if len(sample_names)<2: continue;
                    concs = [];
                    conc_units = None;
                    for sn in sample_names:
                        # concentrations and units
                        conc = None;
                        conc_unit = None;
                        conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName(sn,cn);
                        if not(conc): continue
                        if (conc_unit): conc_units = conc_unit;
                        concs.append(conc);
                    n_replicates = len(concs);
                    # calculate average and CV of concentrations
                    if (not(concs) or n_replicates<2): continue
                    conc_average, data_var_O, conc_CV, data_lb_O, data_ub_O = calc.calculate_ave_var_cv(concs);
                    #conc_average, conc_CV = self.calculate.calculate_ave_CV_R(concs);
                    #conc_average = numpy.mean(numpy.array(concs));
                    #conc_CV = numpy.std(numpy.array(concs))/conc_average*100;
                    data_O.append({'experiment_id':experiment_id_I,
                        'sample_name_abbreviation':sna,
                        'sample_dilution':sd,
                        'component_group_name':component_group_name,
                        'component_name':cn,
                        'n_replicates':n_replicates,
                        'calculated_concentration_average':conc_average,
                        'calculated_concentration_CV':conc_CV,
                        'calculated_concentration_units':conc_units});
                    # add data to the session
                    #row = data_stage01_quantification_QCs(experiment_id_I,sna,sd,component_group_name,cn,n_replicates,
                    #                                            conc_average, conc_CV, conc_units);
                    #self.session.add(row);
        # add data to the database
        #self.session.commit();
        self.add_dataStage01_quantification_QCs(data_O);
        
    def execute_LLOQAndULOQ(self,experiment_id_I):
        '''check the lloq and uloq from the calibrators
        against the calculated concentration
        NOTE: a table is used to store the view'''

        print('execute_LLOQAndULOQ...')
        # query data for the view
        check = [];
        check = self.get_LLOQAndULOQ(experiment_id_I);
        for c in check:
            c['experiment_id'] = experiment_id_I;
        ## create and populate the view
        #for n in range(len(check)):
        #    if check[n]:
        #        try:
        #            row = data_stage01_quantification_LLOQAndULOQ(experiment_id_I,
        #                                                  check[n]['sample_name'],
        #                                                  check[n]['component_group_name'],
        #                                                  check[n]['component_name'],
        #                                                  check[n]['calculated_concentration'],
        #                                                  check[n]['conc_units'],
        #                                                  check[n]['correlation'],
        #                                                  check[n]['lloq'],
        #                                                  check[n]['uloq'],
        #                                                  check[n]['points'],
        #                                                  check[n]['used']);
        #            self.session.add(row);
        #            self.session.commit();
        #        except IntegrityError as e:
        #            self.session.rollback();
        #            print(e);
        # add data to the database
        self.add_dataStage01_quantification_LLOQAndULOQ(check);
    def execute_analyzeDilutions(self,experiment_id_I):
        '''calculate the average and coefficient of variation for analytical
        replicates
        NOTE: analytical replicates are those samples with the same 
        sample_id (but different sample_name)'''
        # Input:
        #   experiment_id
        # Output:
        #   sample_name
        #   component_group_name
        #   component_name
        #   n_replicates
        #   conc_average
        #   conc_CV
        #   conc_units
        
        print('execute_analyzeDilutions...')
        data_O = [];
        # get sample names
        sample_ids = [];
        sample_types = ['Unknown','QC'];
        for st in sample_types:
            sample_ids_tmp = [];
            sample_ids_tmp = self.get_sampleIDs_experimentIDAndSampleType(experiment_id_I,st);
            sample_ids.extend(sample_ids_tmp);
        # create database table
        for si in sample_ids:
            print('analyzing dilutions for sample id ' + si);
            # get sample names
            sample_names = [];
            sample_names = self.get_sampleNames_experimentIDAndSampleID(experiment_id_I,si);
            if len(sample_names)<2: continue;
            # get component names
            component_names = [];
            component_names = self.get_componentsNames_experimentIDAndSampleID(experiment_id_I,si);
            for cn in component_names:
                print('analyzing dilutions for component_name ' + cn);
                concs = [];
                conc_units = None;
                component_group_name = self.get_componentGroupName_experimentIDAndComponentName(experiment_id_I,cn);
                for sn in sample_names:
                    print('analyzing dilutions for sample_name ' + sn);
                    # concentrations and units
                    conc = None;
                    conc_unit = None;
                    conc, conc_unit = self.get_concAndConcUnits_sampleNameAndComponentName(sn,cn);
                    if not(conc): continue
                    if (conc_unit): conc_units = conc_unit;
                    concs.append(conc);
                n_replicates = len(concs);
                # calculate average and CV of concentrations
                if (not(concs) or n_replicates<2): continue
                #conc_average, conc_CV = self.calculate.calculate_ave_CV_R(concs);
                conc_average = numpy.mean(numpy.array(concs));
                conc_CV = numpy.std(numpy.array(concs))/conc_average*100;
                # add data to the session
                data_O.append({'experiment_id':experiment_id_I,
                    'sample_id':si,
                    'component_group_name':component_group_name,
                    'component_name':cn,
                    'n_replicates':n_replicates,
                    'calculated_concentration_average':conc_average,
                    'calculated_concentration_cv':conc_CV,
                    'calculated_concentration_units':conc_units})
                #row = data_stage01_quantification_dilutions(experiment_id_I, si,component_group_name,cn,n_replicates,
                #                                            conc_average, conc_CV, conc_units);
                #self.session.add(row);
        # add data to the database
        #self.session.commit();
        self.add_dataStage01_quantification_dilutions(data_O);

    def execute_analyzeBlanks(self,experiment_id_I):
        '''Compare blanks to unknowns to determine compounds with high background intereference'''
        pass;


    