from model import Person
from error import Error
from typing import Dict, List


'''
规则：省内防止返贫监测对象人口证件号码重复
完成！！！！
'''
id2record: Dict[str, List[Person]] = {}
unstable_type = ['脱贫不稳定户', '边缘易致贫户']
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.idCard in id2record and record.objectInfo.get('监测对象类别') in unstable_type:
        raise Error(no='1_01_002', objectInfo=[record.objectInfo])
    elif record.objectInfo.get('监测对象类别') in unstable_type:
        id2record[record.idCard] = [record]