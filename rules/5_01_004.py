from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and '特困' in record.objectInfo.get('享受特困供养政策情况')  \
            and len(record.objectInfo.get('享受特困供养政策情况')) != 0 \
            and '外出务工' in record.objectInfo.get('就业渠道（易地搬迁后扶使用）'):
        raise Error(no='5_01_004', objectInfo=[record.objectInfo]
                    , msg='享受特困供养的脱贫人口外出务工（基础信息） ')


