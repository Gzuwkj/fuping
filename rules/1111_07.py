from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 1111_07-在校生劳动力状况不是无劳动力(含脱贫人口和监测对象)
    if (record.objectInfo['户类型'] == '脱贫户' or record.objectInfo['监测对象类别'] != '') and \
                record.objectInfo['在校生状况'] != '' and record.objectInfo['劳动技能'] != '无劳动力':
        raise Error(no='1111_07', objectInfo=[record.objectInfo])
