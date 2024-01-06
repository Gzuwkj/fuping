from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    strBuf = record.objectInfo.get('就业渠道（易地搬迁后扶使用）')
    if not pd.isna(strBuf):
        if record.objectInfo.get('户类型') == '脱贫户' \
            and '公益性岗位' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）') \
            and '帮扶车间' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）') \
            and pd.isna(record.objectInfo.get('文化程度'))\
            and pd.isna(record.objectInfo.get('在校生状况'))\
            and pd.isna(record.objectInfo.get('失学或辍学原因')):
            raise Error(no='5_12_002', record=record
                        , msg='县外务工的防止返贫监测对象人口填写了"就业渠道"中的"公益性岗位"和"帮扶车间"')


