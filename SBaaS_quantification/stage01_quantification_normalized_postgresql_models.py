from SBaaS_base.postgresql_orm_base import *

class data_stage01_quantification_normalized(Base):
    __tablename__ = 'data_stage01_quantification_normalized'
    id = Column(Integer, Sequence('data_stage01_quantification_normalized_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    sample_id = Column(String(100))
    #sample_name_short = Column(String(100))  #add in at some-point
    #sample_name_abbreviation = Column(String(100)) #add in at some-point
    #time_point = Column(String(10)) #add in at some-point
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    calculated_concentration = Column(Float)
    calculated_concentration_units = Column(String(20))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name','component_name','calculated_concentration_units'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name=row_dict_I['sample_name'];
        self.sample_id=row_dict_I['sample_id'];
        self.component_group_name=row_dict_I['component_group_name'];
        self.component_name=row_dict_I['component_name'];
        self.calculated_concentration=row_dict_I['calculated_concentration'];
        self.calculated_concentration_units=row_dict_I['calculated_concentration_units'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self, experiment_id_I, sample_name_I, sample_id_I, 
                 #sample_name_short_I,sample_name_abbreviation_I, time_point_I,
                 component_group_name_I, component_name_I,
                    calculated_concentration_I, calculated_concentration_units_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name = sample_name_I;
        self.sample_id = sample_id_I;
        #self.sample_name_short = sample_name_short_I;
        #self.sample_name_abbreviation = sample_name_abbreviation_I;
        #self.time_point = time_point_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.calculated_concentration = calculated_concentration_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.used_ = used_I;

    def __repr__dict__(self):
        return {'id':self.id,
            'experiment_id':self.experiment_id,
            'sample_name':self.sample_name,
            'sample_id':self.sample_id,
            #"sample_name_short":self.sample_name_short,
            #'sample_name_abbreviation':self.sample_name_abbreviation,
            #'time_point':self.time_point,
            'component_group_name':self.component_group_name,
            'component_name':self.component_name,
            'calculated_concentration':self.calculated_concentration,
            'calculated_concentration_units':self.calculated_concentration_units,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_quantification_averages(Base):
    __tablename__ = 'data_stage01_quantification_averages'
    id = Column(Integer, Sequence('data_stage01_quantification_averages_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    n_replicates_broth = Column(Integer)
    calculated_concentration_broth_average = Column(Float)
    calculated_concentration_broth_cv = Column(Float)
    n_replicates_filtrate = Column(Integer)
    calculated_concentration_filtrate_average = Column(Float)
    calculated_concentration_filtrate_cv = Column(Float)
    n_replicates = Column(Integer)
    calculated_concentration_average = Column(Float)
    calculated_concentration_cv = Column(Float)
    calculated_concentration_units = Column(String(20))
    extracellular_percent = Column(Float)
    used_ = Column(Boolean);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','component_name'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.n_replicates_broth=row_dict_I['n_replicates_broth'];
        self.calculated_concentration_broth_average=row_dict_I['calculated_concentration_broth_average'];
        self.calculated_concentration_broth_cv=row_dict_I['calculated_concentration_broth_cv'];
        self.n_replicates_filtrate=row_dict_I['n_replicates_filtrate'];
        self.calculated_concentration_filtrate_average=row_dict_I['calculated_concentration_filtrate_average'];
        self.calculated_concentration_filtrate_cv=row_dict_I['calculated_concentration_filtrate_cv'];
        self.n_replicates=row_dict_I['n_replicates'];
        self.calculated_concentration_average=row_dict_I['calculated_concentration_average'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.calculated_concentration_cv=row_dict_I['calculated_concentration_cv'];
        self.calculated_concentration_units=row_dict_I['calculated_concentration_units'];
        self.extracellular_percent=row_dict_I['extracellular_percent'];
        self.used_=row_dict_I['used_'];
        self.time_point=row_dict_I['time_point'];
        self.component_group_name=row_dict_I['component_group_name'];
        self.component_name=row_dict_I['component_name'];

    def __set__row__(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, component_group_name_I, component_name_I,
                    n_replicates_broth_I, calculated_concentration_broth_average_I, calculated_concentration_broth_cv_I,
                    n_replicates_filtrate_I, calculated_concentration_filtrate_average_I, calculated_concentration_filtrate_cv_I,
                    n_replicates_I, calculated_concentration_average_I, calculated_concentration_cv_I,
                    calculated_concentration_units_I, extracellular_percent_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.n_replicates_broth = n_replicates_broth_I;
        self.calculated_concentration_broth_average = calculated_concentration_broth_average_I;
        self.calculated_concentration_broth_cv = calculated_concentration_broth_cv_I;
        self.n_replicates_filtrate = n_replicates_filtrate_I;
        self.calculated_concentration_filtrate_average = calculated_concentration_filtrate_average_I;
        self.calculated_concentration_filtrate_cv = calculated_concentration_filtrate_cv_I;
        self.n_replicates = n_replicates_I;
        self.calculated_concentration_average = calculated_concentration_average_I;
        self.calculated_concentration_cv = calculated_concentration_cv_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.extracellular_percent = extracellular_percent_I;
        self.used_ = used_I;

    def __repr__dict__(self):
        return {'id':self.id,
        'experiment_id':self.experiment_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        'time_point':self.time_point,
        'component_group_name':self.component_group_name,
        'component_name':self.component_name,
        'n_replicates_broth':self.n_replicates_broth,
        'calculated_concentration_broth_average':self.calculated_concentration_broth_average,
        'calculated_concentration_broth_cv':self.calculated_concentration_broth_cv,
        'n_replicates_filtrate':self.n_replicates_filtrate,
        'calculated_concentration_filtrate_average':self.calculated_concentration_filtrate_average,
        'calculated_concentration_filtrate_cv':self.calculated_concentration_filtrate_cv,
        'n_replicates':self.n_replicates,
        'calculated_concentration_average':self.calculated_concentration_average,
        'calculated_concentration_cv':self.calculated_concentration_cv,
        'calculated_concentration_units':self.calculated_concentration_units,
        'extracellular_percent':self.extracellular_percent,
        'used_':self.used_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())