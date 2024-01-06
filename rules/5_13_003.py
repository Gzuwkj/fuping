from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    phoneStr = str(record.objectInfo.get('家庭成员联系电话')).split('.')[0]
    if record.objectInfo.get('户类型') == '脱贫户' \
        and (phoneStr == 'nan' or len(phoneStr) != 11):
        raise Error(no='5_13_003', record=record
                    , msg='监测对象户联系电话为空或不符合规则')


