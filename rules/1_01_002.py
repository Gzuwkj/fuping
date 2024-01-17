from model import Person
from error import Error
from typing import Dict, List


id2record:Dict[str, List[Person]] = {}
standard_num = [18, 20, 22]
def process(record: Person):
    if record.objectInfo is None:
        return
    error_lists = []
    if record.objectInfo.get('户类型') == '脱贫户' and record.family.host.idCard not in id2record:
        for member in record.family.member:
            if len(member.idCard) not in standard_num:
                error_lists.append(member.objectInfo)
    id2record[record.family.host.idCard] = [record.family.host]
    if len(error_lists) != 0:
        raise Error(no='1_01_002', objectInfo=error_lists)