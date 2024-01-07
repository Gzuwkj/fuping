from model import Person
from error import Error
'''4_01_006-在校生状况选择高中、初中、小学、学前教育或学龄前儿童的脱贫人口填写了已外出务工(改为在校生不为空，基础信息)'''
def process(record: Person):
    if record.objectInfo is None:
        return
    if (any(keyword in record.objectInfo.get("在校生状况") for keyword in ["普通高中三年级", "普通高中二年级", "普通高中一年级", "九年级", "八年级", "七年级", "小学", "学前教育", "学龄前儿童"])) and record.objectInfo.get("户类型") == "脱贫户":
        # 字符串中包含高中、初中、小学、学前教育或学龄前儿童
        if record.outInfo is not None:
            raise Error(no='4_01_006', record=[record.objectInfo])


