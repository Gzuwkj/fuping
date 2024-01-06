from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    strBuf = record.objectInfo.get('就业渠道（易地搬迁后扶使用）')
    if not pd.isna(strBuf) :
        if record.objectInfo.get('户类型') == '脱贫户' \
                and record.objectInfo.get('享受特困供养政策情况') != '未享受'\
                and '外出务工' in strBuf:
            raise Error(no='5_01_004', record=record
                        , msg='享受特困供养的脱贫人口外出务工（基础信息） ')


