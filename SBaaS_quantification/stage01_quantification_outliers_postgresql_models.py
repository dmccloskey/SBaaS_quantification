from SBaaS_base.postgresql_orm_base import *
class data_stage01_quantification_outliersDeviation_replicates(Base):
    __tablename__ = 'data_stage01_quantification_outliersDeviation_replicates'
    id = Column(Integer, Sequence('data_stage01_quantification_outliersDeviation_replicates_id_seq'), primary_key=True)
    #analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    sample_name_short = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    calculated_concentration = Column(Float)
    calculated_concentration_units = Column(String(50))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
                      UniqueConstraint(
                          #'analysis_id',
                          'experiment_id','sample_name_short','time_point','component_name','calculated_concentration_units'),
            )

    def __init__(self, 
                 #analysis_id_I,
                 experiment_id_I, sample_name_short_I, sample_name_abbreviation_I, time_point_I,
                 component_group_name_I, component_name_I, calculated_concentration_I,calculated_concentration_units_I,
                 used_I,comment_I):
        #self.analysis_id = analysis_id_I;
        self.experiment_id = experiment_id_I;
        self.sample_name_short = sample_name_short_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.calculated_concentration = calculated_concentration_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
            #"analysis_id":self.analysis_id,
            "experiment_id":self.experiment_id,
                "sample_name_short":self.sample_name_short,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                "time_point":self.time_point,
                "component_group_name":self.component_group_name,
                "component_name":self.component_name,
                "calculated_concentration":self.calculated_concentration,
                "calculated_concentration_units":self.calculated_concentration_units,
                "used_":self.used_,
                #'comments_I':self.comments_
                }
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())