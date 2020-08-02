#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# Description:
# mrc_ner_data_processor.py


import os
from data_loader.mrc_utils import read_mrc_ner_examples ,read_mrc_event_examples



class QueryNERProcessor(object):
    # processor for the query-based ner dataset 
    def get_train_examples(self, data_dir):
        data = read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.train"))
        return data

    def get_dev_examples(self, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.dev"))

    def get_test_examples(self, data_dir):
        return read_mrc_ner_examples(os.path.join(data_dir, "mrc-ner.test"))


class QueryEevetProcessor(object):
    # processor for the query-based ner dataset
    def get_train_examples(self, data_dir):
        data = read_mrc_event_examples(os.path.join(data_dir, "mrc-ner.train"))
        return data

    def get_dev_examples(self, data_dir):
        return read_mrc_event_examples(os.path.join(data_dir, "mrc-ner.dev"))

    def get_test_examples(self, data_dir):
        return read_mrc_event_examples(os.path.join(data_dir, "mrc-ner.test"))

class EventProcessor(QueryEevetProcessor):
    def get_labels(self):
        return ['财经/交易-降价-降价物', '产品行为-获奖-时间', '财经/交易-出售/收购-时间', '司法行为-约谈-约谈对象', '人生-死亡-时间', '组织行为-罢工-罢工人员', '灾害/意外-坍/垮塌-坍塌主体', '财经/交易-降息-降息幅度', '司法行为-开庭-开庭法院', '灾害/意外-袭击-死亡人数', '财经/交易-跌停-跌停股票', '交往-感谢-时间', '组织关系-解雇-被解雇人员', '产品行为-发布-时间', '司法行为-入狱-入狱者', '组织关系-辞/离职-离职者', '司法行为-举报-举报发起方', '人生-失联-失联者', '人生-失联-时间', '司法行为-罚款-时间', '人生-结婚-时间', '财经/交易-降价-时间', '财经/交易-融资-融资金额', '产品行为-获奖-颁奖机构', '组织关系-加盟-时间', '人生-失联-地点', '组织关系-解散-时间', '司法行为-起诉-被告', '产品行为-召回-召回方', '人生-产子/女-产子者', '灾害/意外-坠机-地点', '灾害/意外-爆炸-死亡人数', '组织关系-解雇-时间', '交往-探班-探班对象', '组织关系-停职-所属组织', '竞赛行为-禁赛-被禁赛人员', '财经/交易-降价-降价幅度', '竞赛行为-禁赛-禁赛机构', '组织关系-解散-解散方', '组织行为-罢工-罢工人数', '财经/交易-出售/收购-出售价格', '人生-求婚-时间', '人生-出轨-出轨对象', '司法行为-罚款-执法机构', '竞赛行为-晋级-晋级方', '财经/交易-融资-跟投方', '财经/交易-融资-融资方', '人生-产子/女-出生者', '财经/交易-涨停-涨停股票', '人生-死亡-死者年龄', '组织行为-开幕-地点', '财经/交易-降息-时间', '财经/交易-涨价-涨价幅度', '人生-死亡-地点', '灾害/意外-地震-死亡人数', '交往-会见-地点', '组织关系-加盟-加盟者', '灾害/意外-袭击-受伤人数', '灾害/意外-地震-时间', '交往-道歉-道歉对象', '人生-离婚-离婚双方', '组织关系-解约-时间', '灾害/意外-地震-受伤人数', '人生-出轨-时间', '灾害/意外-车祸-受伤人数', '组织关系-退出-时间', '司法行为-起诉-原告', '司法行为-拘捕-拘捕者', '竞赛行为-晋级-晋级赛事', '组织行为-闭幕-地点', '人生-庆生-生日方年龄', '灾害/意外-袭击-袭击者', '交往-道歉-道歉者', '组织行为-游行-游行组织', '灾害/意外-车祸-时间', '产品行为-下架-被下架方', '人生-婚礼-时间', '产品行为-下架-下架方', '灾害/意外-爆炸-地点', '灾害/意外-洪灾-受伤人数', '司法行为-开庭-时间', '组织行为-闭幕-活动名称', '财经/交易-出售/收购-收购方', '人生-庆生-时间', '竞赛行为-退役-退役者', '组织关系-解约-解约方', '财经/交易-出售/收购-交易物', '司法行为-约谈-时间', '财经/交易-涨停-时间', '竞赛行为-夺冠-时间', '人生-分手-时间', '组织关系-解雇-解雇方', '产品行为-上映-上映影视', '财经/交易-加息-加息机构', '交往-感谢-被感谢人', '灾害/意外-地震-震源深度', '竞赛行为-退赛-时间', '组织行为-游行-时间', '竞赛行为-夺冠-冠军', '财经/交易-上市-上市企业', '组织关系-解约-被解约方', '组织行为-闭幕-时间', '交往-会见-会见主体', '灾害/意外-车祸-死亡人数', '人生-离婚-时间', '产品行为-发布-发布方', '产品行为-上映-上映方', '人生-婚礼-参礼人员', '财经/交易-上市-时间', '财经/交易-加息-时间', '人生-怀孕-时间', '产品行为-召回-时间', '人生-订婚-订婚主体', '竞赛行为-退役-时间', '交往-探班-时间', '人生-婚礼-结婚双方', '人生-结婚-结婚双方', '灾害/意外-坍/垮塌-死亡人数', '组织关系-退出-退出方', '组织行为-游行-地点', '组织行为-罢工-时间', '财经/交易-涨价-涨价方', '人生-庆生-庆祝方', '灾害/意外-洪灾-死亡人数', '灾害/意外-袭击-袭击对象', '交往-点赞-时间', '组织关系-辞/离职-原所属组织', '产品行为-下架-下架产品', '财经/交易-融资-时间', '产品行为-上映-时间', '竞赛行为-胜负-败者', '司法行为-立案-立案对象', '组织行为-游行-游行人数', '财经/交易-出售/收购-出售方', '灾害/意外-起火-受伤人数', '人生-产子/女-时间', '灾害/意外-爆炸-受伤人数', '组织关系-停职-时间', '司法行为-约谈-约谈发起方', '交往-探班-探班主体', '产品行为-下架-时间', '竞赛行为-胜负-胜者', '人生-订婚-时间', '司法行为-举报-时间', '灾害/意外-袭击-地点', '财经/交易-融资-融资轮次', '司法行为-入狱-刑期', '竞赛行为-胜负-时间', '司法行为-拘捕-时间', '灾害/意外-洪灾-地点', '财经/交易-跌停-时间', '竞赛行为-夺冠-夺冠赛事', '财经/交易-涨价-涨价物', '组织关系-退出-原所属组织', '交往-会见-会见对象', '财经/交易-降息-降息机构', '人生-婚礼-地点', '司法行为-拘捕-被拘捕者', '灾害/意外-袭击-时间', '产品行为-获奖-奖项', '灾害/意外-起火-时间', '灾害/意外-坠机-死亡人数', '交往-道歉-时间', '产品行为-召回-召回内容', '灾害/意外-地震-震中', '司法行为-举报-举报对象', '竞赛行为-退赛-退赛赛事', '司法行为-入狱-时间', '司法行为-起诉-时间', '人生-分手-分手双方', '组织行为-开幕-时间', '交往-会见-时间', '交往-点赞-点赞方', '财经/交易-加息-加息幅度', '竞赛行为-禁赛-禁赛时长', '组织行为-罢工-所属组织', '组织行为-开幕-活动名称', '人生-出轨-出轨方', '灾害/意外-坠机-时间', '人生-怀孕-怀孕者', '人生-死亡-死者', '灾害/意外-起火-死亡人数', '司法行为-立案-时间', '灾害/意外-坍/垮塌-受伤人数', '组织关系-停职-停职人员', '灾害/意外-爆炸-时间', '组织关系-加盟-所加盟组织', '司法行为-立案-立案机构', '组织关系-裁员-裁员人数', '人生-庆生-生日方', '人生-求婚-求婚对象', '人生-求婚-求婚者', '产品行为-获奖-获奖人', '司法行为-罚款-罚款金额', '司法行为-罚款-罚款对象', '灾害/意外-洪灾-时间', '灾害/意外-坠机-受伤人数', '组织关系-裁员-裁员方', '财经/交易-涨价-时间', '竞赛行为-晋级-时间', '组织关系-裁员-时间', '交往-感谢-致谢人', '交往-点赞-点赞对象', '财经/交易-融资-领投方', '财经/交易-降价-降价方', '灾害/意外-车祸-地点', '财经/交易-上市-地点', '财经/交易-上市-融资金额', '司法行为-开庭-开庭案件', '组织关系-辞/离职-时间', '产品行为-发布-发布产品', '竞赛行为-禁赛-时间', '灾害/意外-起火-地点', '灾害/意外-坍/垮塌-时间', '竞赛行为-胜负-赛事名称', '灾害/意外-地震-震级', '竞赛行为-退赛-退赛方',"O"]


class Conll03Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "PER", "LOC", "MISC", "O"]


class MSRAProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["NS", "NR", "NT", "O"]


class Onto4ZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["LOC", "PER", "GPE", "ORG", "O"]


class Onto5EngProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['ORDINAL', 'CARDINAL', 'LOC', 'WORK_OF_ART', 'LANGUAGE', 'ORG', 'FAC', 'PERSON', 'EVENT', 'TIME', 'LAW', 'NORP', 'PERCENT', 'DATE', 'GPE', 'QUANTITY', 'PRODUCT', 'MONEY', 'O']


class ResumeZhProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ["ORG", "LOC", "NAME", "RACE", "TITLE", "EDU", "PRO", "CONT", "O"]


class GeniaProcessor(QueryNERProcessor):
    def get_labels(self, ):
        return ['cell_line', 'cell_type', 'DNA', 'RNA', 'protein', "O"]


class ACE2005Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]


class ACE2004Processor(QueryNERProcessor):
    def get_labels(self, ):
        return ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA", "O"]








