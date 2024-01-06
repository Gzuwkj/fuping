from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    strBuf = record.objectInfo.get('产业帮扶')
    if not pd.isna(strBuf) :
        if record.objectInfo.get('户类型') == '脱贫户' \
            and record.objectInfo.get('风险消除后生产经营性收入') == 0 \
            and pd.isna(record.objectInfo.get('文化程度'))\
            and pd.isna(record.objectInfo.get('在校生状况'))\
            and pd.isna(record.objectInfo.get('失学或辍学原因')):
            raise Error(no='5_11_013', record=record
                        , msg='防止返贫监测对象享风险消除时享受产业帮扶但风险消除的收入模块中无生产经营性收入')


