from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return


    if record.objectInfo.get('户类型') == '脱贫户' \
        and record.objectInfo.get('享受特困供养政策情况') != '未享受' \
        and pd.isna(record.objectInfo.get('文化程度'))\
        and pd.isna(record.objectInfo.get('在校生状况'))\
        and pd.isna(record.objectInfo.get('失学或辍学原因')):
        raise Error(no='5_12_003', record=record
                    , msg='享受特困供养的防止返贫监测对象人口外出务工（基础信息）')


