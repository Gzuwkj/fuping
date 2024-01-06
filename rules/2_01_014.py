from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    phoneStr = str(record.objectInfo.get('家庭成员联系电话')).split('.')[0]
    strBuf = record.objectInfo.get('就业渠道（易地搬迁后扶使用）')
    if not pd.isna(strBuf):
        if record.objectInfo.get('户类型') == '脱贫户' \
            and '务工' in strBuf \
            and len(phoneStr) != 11:
            raise Error(no='2_01_014', record=record
                        , msg='务工脱贫人口联系电话不符合手机号码校验规则')


