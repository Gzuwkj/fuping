from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
        and '补助' in record.objectInfo.get('义务教育保障') \
        and '初中' not in record.objectInfo.get('在校生状况') \
        and '高中' not in record.objectInfo.get('在校生状况'):
        raise Error(no='5_15_011', objectInfo=[record.objectInfo]
                    , msg='脱贫人口2023年享受雨露计划职业教育补助人员但该人员不是中高职学生')