from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    strBuf = record.objectInfo.get('就业渠道（易地搬迁后扶使用）')
    if not pd.isna(strBuf) :
        if record.objectInfo.get('户类型') == '脱贫户' \
            and '外出务工' in strBuf \
            and not pd.isna(record.objectInfo.get('务工所在地')) :

            raise Error(no='5_15_008', record=record
                        , msg='脱贫人口务工监测有计划外出务工未填写务工需求')

