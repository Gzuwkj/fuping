from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return


    strBuf = record.objectInfo.get('义务教育保障')
    if not pd.isna(strBuf) and type(record.objectInfo.get('在校生状况')) == str:
        if record.objectInfo.get('户类型') == '脱贫户' \
            and ('本科' in record.objectInfo.get('在校生状况') \
            or '研究生' in record.objectInfo.get('在校生状况')):
            raise Error(no='5_15_011', record=record
                        , msg='脱贫人口2023年享受雨露计划职业教育补助人员但该人员不是中高职学生')