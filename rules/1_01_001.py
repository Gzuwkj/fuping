from model import Person
from error import Error
from typing import Dict, List

'''
规则：省内脱贫人口证件号码重复
完成！！！！
'''
id2record: Dict[str, List[Person]] = {}

def process(record: Person):
    if record.objectInfo is None:
        return
    if record.idCard in id2record:
        id2record[record.idCard].append(record)
        raise Error(no='1_01_001', objectInfo=id2record[record.idCard])
    else:
        id2record[record.idCard] = [record]