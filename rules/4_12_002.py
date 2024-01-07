from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
        and '务工' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）') \
        and ( '高中' in record.objectInfo.get('在校生状况') or \
              '初中' in record.objectInfo.get('在校生状况') or \
              '小学' in record.objectInfo.get('在校生状况') or\
              '学前教育' in record.objectInfo.get('在校生状况') or\
              '学龄前儿童' in record.objectInfo.get('在校生状况'))\
        and len(record.objectInfo.get('文化程度')) == 0\
        and len(record.objectInfo.get('在校生状况')) == 0\
        and len(record.objectInfo.get('失学或辍学原因')) == 0:
        raise Error(no='4_12_002', objectInfo=record.objectInfo
                    , msg='在校生状况选择高中、初中、小学、学前教育或学龄前儿童的防止返贫监测对象人口填写了已外出务工或计划外出务工(改为在校生不为空)')


