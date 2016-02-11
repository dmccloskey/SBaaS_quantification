from SBaaS_base.postgresql_orm_base import *

class data_stage01_quantification_replicates(Base):
    __tablename__ = 'data_stage01_quantification_replicates'
    id = Column(Integer, Sequence('data_stage01_quantification_replicates_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_short = Column(String(100))
    #sample_name_abbreviation = Column(String(100)) #add in at some-point
    time_point = Column(String(10))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    calculated_concentration = Column(Float)
    calculated_concentration_units = Column(String(20))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_short','time_point','component_name','calculated_concentration_units'),
            )

    def __init__(self, experiment_id_I, sample_name_short_I,
                 #sample_name_abbreviation_I,
                 time_point_I, component_group_name_I, component_name_I,
                    calculated_concentration_I,calculated_concentration_units_I,
                used__I,
                comment__I):
        self.experiment_id = experiment_id_I;
        self.sample_name_short = sample_name_short_I;
        #self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.component_group_name = component_group_name_I;
        self.component_name = component_name_I;
        self.calculated_concentration = calculated_concentration_I;
        self.calculated_concentration_units = calculated_concentration_units_I;
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                "experiment_id":self.experiment_id,
                "sample_name_short":self.sample_name_short,
                #'sample_name_abbreviation':self.sample_name_abbreviation,
                "time_point":self.time_point,
                "component_group_name":self.component_group_name,
                "component_name":self.component_name,
                "calculated_concentration":self.calculated_concentration,
                "calculated_concentration_units":self.calculated_concentration_units,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())