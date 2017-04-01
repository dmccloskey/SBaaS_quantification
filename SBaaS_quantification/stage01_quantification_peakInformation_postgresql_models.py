from SBaaS_base.postgresql_orm_base import *

class data_stage01_quantification_peakInformation(Base):
    __tablename__ = 'data_stage01_quantification_peakInformation'
    id = Column(Integer, Sequence('data_stage01_quantification_peakInformation_id_seq'), primary_key=True)
    analysis_id = Column(String(50))
    #experiment_id = Column(postgresql.ARRAY(String(50))) need to remove policies first...
    experiment_id = Column(String(50))
    component_group_name = Column(String(100))
    component_name = Column(String(500))
    peakInfo_parameter = Column(String(50))
    peakInfo_n = Column(Integer)
    peakInfo_ave = Column(Float)
    peakInfo_cv = Column(Float)
    peakInfo_lb = Column(Float)
    peakInfo_ub = Column(Float)
    peakInfo_units = Column(String(50))
    sample_names = Column(postgresql.ARRAY(String(100)))
    sample_name_abbreviation = Column(String(100))
    sample_types = Column(postgresql.ARRAY(String(100)))
    acqusition_date_and_times = Column(postgresql.ARRAY(DateTime))
    peakInfo_data = Column(postgresql.ARRAY(Float))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint(
        'analysis_id','experiment_id','sample_name_abbreviation','component_name','peakInfo_parameter'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.analysis_id=row_dict_I['analysis_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.component_group_name=row_dict_I['component_group_name'];
        self.component_name=row_dict_I['component_name'];
        self.peakInfo_parameter=row_dict_I['peakInfo_parameter'];
        self.peakInfo_n=row_dict_I['peakInfo_n'];
        self.peakInfo_ave=row_dict_I['peakInfo_ave'];
        self.peakInfo_cv=row_dict_I['peakInfo_cv'];
        self.peakInfo_lb=row_dict_I['peakInfo_lb'];
        self.peakInfo_ub=row_dict_I['peakInfo_ub'];
        self.peakInfo_units=row_dict_I['peakInfo_units'];
        self.sample_names=row_dict_I['sample_names'];
        self.sample_types=row_dict_I['sample_types'];
        self.acqusition_date_and_times=row_dict_I['acqusition_date_and_times'];
        self.peakInfo_data=row_dict_I['peakInfo_data'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self,
                 analysis_id_I,
                 experiment_id_I,
                component_group_name_I,
                component_name_I,
                peakInfo_parameter_I,
                peakInfo_n_I,
                peakInfo_ave_I,
                peakInfo_cv_I,
                peakInfo_lb_I,
                peakInfo_ub_I,
                peakInfo_units_I,
                sample_names_I,
                sample_name_abbreviation_I,
                sample_types_I,
                acqusition_date_and_times_I,
                peakInfo_data_I,
                used__I,
                comment__I):
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.component_group_name=component_group_name_I
        self.component_name=component_name_I
        self.peakInfo_parameter=peakInfo_parameter_I
        self.peakInfo_n=peakInfo_n_I
        self.peakInfo_ave=peakInfo_ave_I
        self.peakInfo_cv=peakInfo_cv_I
        self.peakInfo_lb=peakInfo_lb_I
        self.peakInfo_ub=peakInfo_ub_I
        self.peakInfo_units=peakInfo_units_I
        self.sample_names=sample_names_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.sample_types=sample_types_I
        self.acqusition_date_and_times=acqusition_date_and_times_I
        self.peakInfo_data=peakInfo_data_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
            'component_group_name':self.component_group_name,
            'component_name':self.component_name,
            'peakInfo_parameter':self.peakInfo_parameter,
            'peakInfo_n':self.peakInfo_n,
            'peakInfo_ave':self.peakInfo_ave,
            'peakInfo_cv':self.peakInfo_cv,
            'peakInfo_lb':self.peakInfo_lb,
            'peakInfo_ub':self.peakInfo_ub,
            'peakInfo_units':self.peakInfo_units,
            'sample_names':self.sample_names,
            'sample_name_abbreviation':self.sample_name_abbreviation,
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
    analysis_id = Column(String(50))
    #experiment_id = Column(postgresql.ARRAY(String(50))) need to remove policies first...
    experiment_id = Column(String(50))
    component_group_name_pair = Column(postgresql.ARRAY(String(100)))
    component_name_pair = Column(postgresql.ARRAY(String(500)))
    peakInfo_parameter = Column(String(50))
    peakInfo_n = Column(Integer)
    peakInfo_ave = Column(Float)
    peakInfo_cv = Column(Float)
    peakInfo_lb = Column(Float)
    peakInfo_ub = Column(Float)
    peakInfo_units = Column(String(50))
    sample_names = Column(postgresql.ARRAY(String(100)))
    sample_name_abbreviation = Column(String(100))
    sample_types = Column(postgresql.ARRAY(String(100)))
    acqusition_date_and_times = Column(postgresql.ARRAY(DateTime))
    peakInfo_data = Column(postgresql.ARRAY(Float))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint(
        'analysis_id',
        'experiment_id',
        'sample_name_abbreviation',
        'component_name_pair',
        'peakInfo_parameter'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.peakInfo_units=row_dict_I['peakInfo_units'];
        self.peakInfo_ub=row_dict_I['peakInfo_ub'];
        self.peakInfo_lb=row_dict_I['peakInfo_lb'];
        self.peakInfo_cv=row_dict_I['peakInfo_cv'];
        self.peakInfo_ave=row_dict_I['peakInfo_ave'];
        self.peakInfo_parameter=row_dict_I['peakInfo_parameter'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.component_group_name_pair=row_dict_I['component_group_name_pair'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.peakInfo_data=row_dict_I['peakInfo_data'];
        self.acqusition_date_and_times=row_dict_I['acqusition_date_and_times'];
        self.component_name_pair=row_dict_I['component_name_pair'];
        self.sample_types=row_dict_I['sample_types'];
        self.sample_names=row_dict_I['sample_names'];
        self.analysis_id=row_dict_I['analysis_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.peakInfo_n=row_dict_I['peakInfo_n'];

    def __set__row__(self,
                 analysis_id_I,
                 experiment_id_I,
                component_group_name_pair_I,
                component_name_pair_I,
                peakInfo_parameter_I,
                peakInfo_n_I,
                peakInfo_ave_I,
                peakInfo_cv_I,
                peakInfo_lb_I,
                peakInfo_ub_I,
                peakInfo_units_I,
                sample_names_I,
                sample_name_abbreviation_I,
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
        self.analysis_id=analysis_id_I
        self.peakInfo_n=peakInfo_n_I
        self.sample_name_abbreviation=sample_name_abbreviation_I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
                'experiment_id':self.experiment_id,
            'component_group_name_pair':self.component_group_name_pair,
            'component_name_pair':self.component_name_pair,
            'peakInfo_parameter':self.peakInfo_parameter,
            'peakInfo_n':self.peakInfo_n,
            'peakInfo_ave':self.peakInfo_ave,
            'peakInfo_cv':self.peakInfo_cv,
            'peakInfo_lb':self.peakInfo_lb,
            'peakInfo_ub':self.peakInfo_ub,
            'peakInfo_units':self.peakInfo_units,
            'sample_names':self.sample_names,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'sample_types':self.sample_types,
            'acqusition_date_and_times':self.acqusition_date_and_times,
            'peakInfo_data':self.peakInfo_data,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())