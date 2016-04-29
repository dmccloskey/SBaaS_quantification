from SBaaS_base.postgresql_orm_base import *

class data_stage01_quantification_physiologicalRatios_replicates(Base):
    __tablename__ = 'data_stage01_quantification_physiologicalRatios_replicates'
    id = Column(Integer, Sequence('data_stage01_quantification_physiologicalRatios_replicates_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_short = Column(String(100))
    #sample_name_abbreviation = Column(String(100)) #add in at some-point
    time_point = Column(String(10))
    physiologicalratio_id = Column(String(50))
    physiologicalratio_name = Column(String(100))
    physiologicalratio_value = Column(Float)
    physiologicalratio_description = Column(String(500))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_short','time_point','physiologicalratio_id'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.time_point=row_dict_I['time_point'];
        self.physiologicalratio_name=row_dict_I['physiologicalratio_name'];
        self.physiologicalratio_value=row_dict_I['physiologicalratio_value'];
        self.physiologicalratio_description=row_dict_I['physiologicalratio_description'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.id=row_dict_I['id'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_short=row_dict_I['sample_name_short'];
        self.physiologicalratio_id=row_dict_I['physiologicalratio_id'];

    def __set__row__(self, experiment_id_I,
                sample_name_short_I,
                #sample_name_abbreviation_I,
                time_point_I,
                #time_point_units_I,
                physiologicalratio_id_I,
                physiologicalratio_name_I,
                physiologicalratio_value_I,
                physiologicalratio_description_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name_short=sample_name_short_I
        #self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point=time_point_I
        self.physiologicalratio_id=physiologicalratio_id_I
        self.physiologicalratio_name=physiologicalratio_name_I
        self.physiologicalratio_value=physiologicalratio_value_I
        self.physiologicalratio_description=physiologicalratio_description_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__(self):
        return "data_stage01_quantification_physiologicalRatios_replicates: %s, %s, %s" % (self.experiment_id,
                                                                            self.sample_name_short,
                                                                            self.physiologicalratio_id)

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
            'sample_name_short':self.sample_name_short,
            #'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
            'physiologicalratio_id':self.physiologicalratio_id,
            'physiologicalratio_name':self.physiologicalratio_name,
            'physiologicalratio_value':self.physiologicalratio_value,
            'physiologicalratio_description':self.physiologicalratio_description,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage01_quantification_physiologicalRatios_averages(Base):
    __tablename__ = 'data_stage01_quantification_physiologicalRatios_averages'
    id = Column(Integer, Sequence('data_stage01_quantification_physiologicalRatios_averages_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    physiologicalratio_id = Column(String(50))
    physiologicalratio_name = Column(String(100))
    physiologicalratio_value_ave = Column(Float)
    physiologicalratio_value_cv = Column(Float)
    physiologicalratio_value_lb = Column(Float)
    physiologicalratio_value_ub = Column(Float)
    physiologicalratio_description = Column(String(500))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','physiologicalratio_id'),
            )
    def __init__(self,
                row_dict_I,
                ):
        self.physiologicalratio_name=row_dict_I['physiologicalratio_name'];
        self.physiologicalratio_value_ave=row_dict_I['physiologicalratio_value_ave'];
        self.physiologicalratio_value_cv=row_dict_I['physiologicalratio_value_cv'];
        self.comment_=row_dict_I['comment_'];
        self.physiologicalratio_description=row_dict_I['physiologicalratio_description'];
        self.used_=row_dict_I['used_'];
        self.physiologicalratio_value_ub=row_dict_I['physiologicalratio_value_ub'];
        self.id=row_dict_I['id'];
        self.physiologicalratio_value_lb=row_dict_I['physiologicalratio_value_lb'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.time_point=row_dict_I['time_point'];
        self.physiologicalratio_id=row_dict_I['physiologicalratio_id'];

    def __set__row__(self,experiment_id_I,
                sample_name_abbreviation_I,
                time_point_I,
                physiologicalratio_id_I,
                physiologicalratio_name_I,
                physiologicalratio_value_ave_I,
                physiologicalratio_value_cv_I,
                physiologicalratio_value_lb_I,
                physiologicalratio_value_ub_I,
                physiologicalratio_description_I,
                used__I,
                comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.physiologicalratio_id=physiologicalratio_id_I
        self.physiologicalratio_name=physiologicalratio_name_I
        self.physiologicalratio_value_ave=physiologicalratio_value_ave_I
        self.physiologicalratio_value_cv=physiologicalratio_value_cv_I
        self.physiologicalratio_value_lb=physiologicalratio_value_lb_I
        self.physiologicalratio_value_ub=physiologicalratio_value_ub_I
        self.physiologicalratio_description=physiologicalratio_description_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__(self):
        return "data_stage01_quantification_physiologicalRatios_averages: %s, %s, %s" % (self.experiment_id,
                                                                            self.sample_name_abbreviation,
                                                                            self.physiologicalratio_id)

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
                'physiologicalratio_id':self.physiologicalratio_id,
                'physiologicalratio_name':self.physiologicalratio_name,
                'physiologicalratio_value_ave':self.physiologicalratio_value_ave,
                'physiologicalratio_value_cv':self.physiologicalratio_value_cv,
                'physiologicalratio_value_lb':self.physiologicalratio_value_lb,
                'physiologicalratio_value_ub':self.physiologicalratio_value_ub,
                'physiologicalratio_description':self.physiologicalratio_description,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())