from model import Person
from error import Error
import pandas as pd
import datetime

def getAge(idcard):
    birth = idcard[6:10]
    age = datetime.date.today().year - int(birth)
    return age

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
        and '公益岗位' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）') \
        and getAge(record.objectInfo.get('证件号码')) >= 70 \
        and len(record.objectInfo.get('文化程度')) == 0 \
        and len(record.objectInfo.get('在校生状况')) == 0 \
        and len(record.objectInfo.get('失学或辍学原因')) == 0:
        raise Error(no='5_12_005', objectInfo=record.objectInfo, outInfo=record.outInfo
                    , msg='70岁及以上防止返贫监测对象人口参加公益性岗位')




