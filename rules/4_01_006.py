from model import Person
from error import Error

'''4_01_006-在校生状况选择高中、初中、小学、学前教育或学龄前儿童的脱贫人口填写了已外出务工(改为在校生不为空，基础信息)'''


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get("在校生状况") != "" and record.objectInfo.get("户类型") == "脱贫户":
        if record.outInfo is not None:
            raise Error(no='4_01_006', objectInfo=[record.objectInfo], outInfo=record.outInfo)
