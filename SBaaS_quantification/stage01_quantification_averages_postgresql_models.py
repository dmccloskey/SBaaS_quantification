from SBaaS_base.postgresql_orm_base import *

class data_stage01_quantification_averagesMI(Base):
    __tablename__ = 'data_stage01_quantification_averagesmi'
    id = Column(Integer, Sequence('data_stage01_quantification_averagesmi_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    n_replicates = Column(Integer)
    calculated_concentration_average = Column(Float)
    calculated_concentration_cv = Column(Float)
    calculated_concentration_units = Column(String(20))
    used_ = Column(Boolean);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','component_name'),
            )

    def __init__(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, component_group_name_I, component_name_I,
                    n_replicates_I, calculated_concentration_average_I, calculated_concentration_cv_I,
                    calculated_concentration_units_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.n_replicates = n_replicates_I;
        self.calculated_concentration_average = calculated_concentration_average_I;
        self.calculated_concentration_cv = calculated_concentration_cv_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.used_ = used_I;

    def __repr__dict__(self):
        return {'id':self.id,
                "experiment_id":self.experiment_id,
                "sample_name_abbreviation":self.sample_name_abbreviation,
                "time_point":self.time_point,
                "component_group_name":self.component_group_name,
                "component_name":self.component_name,
                "calculated_concentration_average":self.calculated_concentration_average,
                "calculated_concentration_cv":self.calculated_concentration_cv,
                "calculated_concentration_units":self.calculated_concentration_units,
                "used_":self.used_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_quantification_averagesMIgeo(Base):
    __tablename__ = 'data_stage01_quantification_averagesmigeo'
    id = Column(Integer, Sequence('data_stage01_quantification_averagesmigeo_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    n_replicates = Column(Integer)
    calculated_concentration_average = Column(Float)
    calculated_concentration_var = Column(Float)
    calculated_concentration_lb = Column(Float)
    calculated_concentration_ub = Column(Float)
    calculated_concentration_units = Column(String(20))
    used_ = Column(Boolean);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','component_name'),
            )

    def __init__(self, experiment_id_I, sample_name_abbreviation_I, time_point_I, component_group_name_I, component_name_I,
                    n_replicates_I, calculated_concentration_average_I, calculated_concentration_var_I,
                    calculated_concentration_lb_I, calculated_concentration_ub_I,
                    calculated_concentration_units_I, used_I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.n_replicates = n_replicates_I;
        self.calculated_concentration_average = calculated_concentration_average_I;
        self.calculated_concentration_var = calculated_concentration_var_I;
        self.calculated_concentration_lb = calculated_concentration_lb_I;
        self.calculated_concentration_ub = calculated_concentration_ub_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.used_ = used_I;

    def __repr__dict__(self):
        return {'id':self.id,
                "experiment_id":self.experiment_id,
                "sample_name_abbreviation":self.sample_name_abbreviation,
                "time_point":self.time_point,
                "component_group_name":self.component_group_name,
                "component_name":self.component_name,
                "n_replicates":self.n_replicates,
                "calculated_concentration_average":self.calculated_concentration_average,
                "calculated_concentration_var":self.calculated_concentration_cv,
                "calculated_concentration_lb":self.calculated_concentration_lb,
                "calculated_concentration_ub":self.calculated_concentration_ub,
                "calculated_concentration_units":self.calculated_concentration_units,
                "used_":self.used_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())