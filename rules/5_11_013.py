from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return


    if record.objectInfo.get('户类型') == '脱贫户' \
        and len(record.objectInfo.get('监测对象类别')) != 0 \
        and record.objectInfo.get('风险是否已消除') == '是' \
        and len(record.objectInfo.get('产业帮扶')) != 0 \
        and float(record.objectInfo.get('生产经营性收入')) == 0 :
        raise Error(no='5_11_013', objectInfo=[record.objectInfo]
                    , msg='防止返贫监测对象享风险消除时享受产业帮扶但风险消除的收入模块中无生产经营性收入')


