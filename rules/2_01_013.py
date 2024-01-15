from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    phoneStr = str(record.objectInfo.get('家庭成员联系电话')).split('.')[0]
    if record.objectInfo.get('户类型') == '脱贫户' \
        and '务工' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）') \
        and len(phoneStr) != 11:
        raise Error(no='2_01_013', objectInfo=[record.objectInfo]
                    , msg='务工脱贫人口联系电话不是11位手机号码')


