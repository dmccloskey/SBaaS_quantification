from SBaaS_base.postgresql_orm_base import *


class data_stage01_quantification_LLOQAndULOQ(Base):
    __tablename__ = 'data_stage01_quantification_LLOQAndULOQ'
    id = Column(Integer, Sequence('data_stage01_quantification_lloqanduloq_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name = Column(String(100))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    calculated_concentration = Column(Float)
    calculated_concentration_units = Column(String(20))
    correlation = Column(Float)
    lloq = Column(Float);
    uloq = Column(Float);
    points = Column(Float);
    used_ = Column(Boolean);
    __table_args__ = (UniqueConstraint('experiment_id','sample_name','component_name','calculated_concentration_units'),
            )
    def __init__(self,
                row_dict_I,
                ):        
        self.experiment_id=row_dict_I['experiment_id'];
        self.used_=row_dict_I['used_'];
        self.points=row_dict_I['points'];
        self.uloq=row_dict_I['uloq'];
        self.lloq=row_dict_I['lloq'];
        self.correlation=row_dict_I['correlation'];
        self.calculated_concentration_units=row_dict_I['calculated_concentration_units'];
        self.calculated_concentration=row_dict_I['calculated_concentration'];
        self.component_name=row_dict_I['component_name'];
        self.component_group_name=row_dict_I['component_group_name'];
        self.sample_name=row_dict_I['sample_name'];


    def __set__row__(self, experiment_id_I, sample_name_I, component_group_name_I, component_name_I,
                    calculated_concentration_I, calculated_concentration_units_I,
                    correlation_I, lloq_I, uloq_I, points_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name = sample_name_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.calculated_concentration = calculated_concentration_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.correlation = correlation_I;
        self.lloq = lloq_I;
        self.uloq = uloq_I;
        self.points = points_I;
        self.used_ = used_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name':self.sample_name,
                'component_group_name':self.component_group_name,
                'component_name':self.component_name,
                'calculated_concentration':self.calculated_concentration,
                'calculated_concentration_units':self.calculated_concentration_units,
                'correlation':self.correlation,
                'lloq':self.lloq,
                'uloq':self.uloq,
                'points':self.points,
                'used_':self.used_,
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_quantification_dilutions(Base):
    __tablename__ = 'data_stage01_quantification_dilutions'
    id = Column(Integer, Sequence('data_stage01_quantification_dilutions_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_id = Column(String(100))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    n_replicates = Column(Integer)
    calculated_concentration_average = Column(Float)
    calculated_concentration_cv = Column(Float)
    calculated_concentration_units = Column(String(20))
    __table_args__ = (UniqueConstraint('experiment_id','sample_id','component_name','calculated_concentration_units'),
            )
    
    def __init__(self,
                row_dict_I,
                ):
        self.calculated_concentration_average=row_dict_I['calculated_concentration_average'];
        self.calculated_concentration_cv=row_dict_I['calculated_concentration_cv'];
        self.calculated_concentration_units=row_dict_I['calculated_concentration_units'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_id=row_dict_I['sample_id'];
        self.component_group_name=row_dict_I['component_group_name'];
        self.component_name=row_dict_I['component_name'];
        self.n_replicates=row_dict_I['n_replicates'];

    def __set__row__(self, experiment_id_I, sample_id_I, component_group_name_I, component_name_I, n_replicates_I,
                    calculated_concentration_average_I, calculated_concentration_cv_I, calculated_concentration_units_I):
        self.experiment_id = experiment_id_I;
        self.sample_id = sample_id_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.n_replicates = n_replicates_I;
        self.calculated_concentration_average = calculated_concentration_average_I;
        self.calculated_concentration_cv = calculated_concentration_cv_I;
        self.calculated_concentration_units = calculated_concentration_units_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_id':self.sample_id,
                'component_group_name':self.component_group_name,
                'component_name':self.component_name,
                'n_replicates':self.n_replicates,
                'calculated_concentration_average':self.calculated_concentration_average,
                'calculated_concentration_cv':self.calculated_concentration_cv,
                'calculated_concentration_units':self.calculated_concentration_units,
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_quantification_QCs(Base):
    __tablename__ = 'data_stage01_quantification_QCs'
    id = Column(Integer, Sequence('data_stage01_quantification_qcs_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    sample_dilution = Column(Float, primary_key=True);
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    n_replicates = Column(Integer)
    calculated_concentration_average = Column(Float)
    calculated_concentration_CV = Column(Float)
    calculated_concentration_units = Column(String(20))

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','component_name','calculated_concentration_units'),
            )
    
    def __init__(self,
                row_dict_I,
                ):
        self.sample_dilution=row_dict_I['sample_dilution'];
        self.calculated_concentration_units=row_dict_I['calculated_concentration_units'];
        self.calculated_concentration_CV=row_dict_I['calculated_concentration_CV'];
        self.calculated_concentration_average=row_dict_I['calculated_concentration_average'];
        self.n_replicates=row_dict_I['n_replicates'];
        self.component_name=row_dict_I['component_name'];
        self.component_group_name=row_dict_I['component_group_name'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.experiment_id=row_dict_I['experiment_id'];

    def __set__row__(self, experiment_id_I, sample_name_abbreviation_I, sample_dilution_I, component_group_name_I, component_name_I, n_replicates_I,
                    calculated_concentration_average_I, calculated_concentration_CV_I, calculated_concentration_units_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.sample_dilution = sample_dilution_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.n_replicates = n_replicates_I;
        self.calculated_concentration_average = calculated_concentration_average_I;
        self.calculated_concentration_CV = calculated_concentration_CV_I;
        self.calculated_concentration_units = calculated_concentration_units_I;

    def __repr__dict__(self):
        return {'id':self.id,
        'experiment_id':self.experiment_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        'sample_dilution':self.sample_dilution,
        'component_group_name':self.component_group_name,
        'component_name':self.component_name,
        'n_replicates':self.n_replicates,
        'calculated_concentration_average':self.calculated_concentration_average,
        'calculated_concentration_CV':self.calculated_concentration_CV,
        'calculated_concentration_units':self.calculated_concentration_units}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())