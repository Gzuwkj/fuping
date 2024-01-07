from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.outInfo is None:
        return

    for outInfo in record.outInfo:
        if outInfo.get('户类型') == '脱贫户' \
            and ('公益性岗位' in outInfo.get('就业渠道')
            or '帮扶车间' in outInfo.get('就业渠道')) \
            and len(record.objectInfo.get('文化程度')) == 0\
            and len(record.objectInfo.get('在校生状况')) == 0\
            and len(record.objectInfo.get('失学或辍学原因')) == 0:
            raise Error(no='5_12_002', record=record
                        , msg='县外务工的防止返贫监测对象人口填写了"就业渠道"中的"公益性岗位"和"帮扶车间"')


