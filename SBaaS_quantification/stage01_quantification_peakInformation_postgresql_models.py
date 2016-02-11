from SBaaS_base.postgresql_orm_base import *

class data_stage01_quantification_peakInformation(Base):
    __tablename__ = 'data_stage01_quantification_peakInformation'
    id = Column(Integer, Sequence('data_stage01_quantification_peakInformation_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    peakInfo_parameter = Column(String(50))
    peakInfo_ave = Column(Float)
    peakInfo_cv = Column(Float)
    peakInfo_lb = Column(Float)
    peakInfo_ub = Column(Float)
    peakInfo_units = Column(String(50))
    sample_names = Column(postgresql.ARRAY(String(100)))
    sample_types = Column(postgresql.ARRAY(String(100)))
    acqusition_date_and_times = Column(postgresql.ARRAY(DateTime))
    peakInfo_data = Column(postgresql.ARRAY(Float))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','component_name','peakInfo_parameter'),
            )

    def __init__(self,
                 experiment_id_I,
                component_group_name_I,
                component_name_I,
                peakInfo_parameter_I,
                peakInfo_ave_I,
                peakInfo_cv_I,
                peakInfo_lb_I,
                peakInfo_ub_I,
                peakInfo_units_I,
                sample_names_I,
                sample_types_I,
                acqusition_date_and_times_I,
                peakInfo_data_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.component_group_name=component_group_name_I
        self.component_name=component_name_I
        self.peakInfo_parameter=peakInfo_parameter_I
        self.peakInfo_ave=peakInfo_ave_I
        self.peakInfo_cv=peakInfo_cv_I
        self.peakInfo_lb=peakInfo_lb_I
        self.peakInfo_ub=peakInfo_ub_I
        self.peakInfo_units=peakInfo_units_I
        self.sample_names=sample_names_I
        self.sample_types=sample_types_I
        self.acqusition_date_and_times=acqusition_date_and_times_I
        self.peakInfo_data=peakInfo_data_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
            'component_group_name':self.component_group_name,
            'component_name':self.component_name,
            'peakInfo_parameter':self.peakInfo_parameter,
            'peakInfo_ave':self.peakInfo_ave,
            'peakInfo_cv':self.peakInfo_cv,
            'peakInfo_lb':self.peakInfo_lb,
            'peakInfo_ub':self.peakInfo_ub,
            'peakInfo_units':self.peakInfo_units,
            'sample_names':self.sample_names,
            'sample_types':self.sample_types,
            'acqusition_date_and_times':self.acqusition_date_and_times,
            'peakInfo_data':self.peakInfo_data,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_quantification_peakResolution(Base):
    __tablename__ = 'data_stage01_quantification_peakResolution'
    id = Column(Integer, Sequence('data_stage01_quantification_peakResolution_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    component_group_name_pair = Column(postgresql.ARRAY(String(100)))
    component_name_pair = Column(postgresql.ARRAY(String(500)))
    peakInfo_parameter = Column(String(50))
    peakInfo_ave = Column(Float)
    peakInfo_cv = Column(Float)
    peakInfo_lb = Column(Float)
    peakInfo_ub = Column(Float)
    peakInfo_units = Column(String(50))
    sample_names = Column(postgresql.ARRAY(String(100)))
    sample_types = Column(postgresql.ARRAY(String(100)))
    acqusition_date_and_times = Column(postgresql.ARRAY(DateTime))
    peakInfo_data = Column(postgresql.ARRAY(Float))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','component_name_pair','peakInfo_parameter'),
            )

    def __init__(self,
                 experiment_id_I,
                component_group_name_pair_I,
                component_name_pair_I,
                peakInfo_parameter_I,
                peakInfo_ave_I,
                peakInfo_cv_I,
                peakInfo_lb_I,
                peakInfo_ub_I,
                peakInfo_units_I,
                sample_names_I,
                sample_types_I,
                acqusition_date_and_times_I,
                peakInfo_data_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.component_group_name_pair=component_group_name_pair_I
        self.component_name_pair=component_name_pair_I
        self.peakInfo_parameter=peakInfo_parameter_I
        self.peakInfo_ave=peakInfo_ave_I
        self.peakInfo_cv=peakInfo_cv_I
        self.peakInfo_lb=peakInfo_lb_I
        self.peakInfo_ub=peakInfo_ub_I
        self.peakInfo_units=peakInfo_units_I
        self.sample_names=sample_names_I
        self.sample_types=sample_types_I
        self.acqusition_date_and_times=acqusition_date_and_times_I
        self.peakInfo_data=peakInfo_data_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
            'component_group_name_pair':self.component_group_name_pair,
            'component_name_pair':self.component_name_pair,
            'peakInfo_parameter':self.peakInfo_parameter,
            'peakInfo_ave':self.peakInfo_ave,
            'peakInfo_cv':self.peakInfo_cv,
            'peakInfo_lb':self.peakInfo_lb,
            'peakInfo_ub':self.peakInfo_ub,
            'peakInfo_units':self.peakInfo_units,
            'sample_names':self.sample_names,
            'sample_types':self.sample_types,
            'acqusition_date_and_times':self.acqusition_date_and_times,
            'peakInfo_data':self.peakInfo_data,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())