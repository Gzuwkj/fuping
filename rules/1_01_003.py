from model import Person
from error import Error
from typing import Dict, List


id2record:Dict[str, List[Person]] = {}
checksum_dict = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2'}
def check_id(id: str) -> bool:
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    factors = [int(id[i]) * weights[i] for i in range(17)]
    checksum = sum(factors) % 11
    return checksum_dict.get(checksum) == id[17]

def process(record: Person):
    if record.objectInfo is None:
        return
    error_lists = []
    if record.objectInfo.get('户类型') == '脱贫户' and record.family.host.idCard not in id2record:
        for member in record.family.member:
            if len(member.idCard) == 18:
                if not check_id(member.idCard):
                    error_lists.append(member.objectInfo)
    id2record[record.family.host.idCard] = [record.family.host]
    if len(error_lists) != 0:
        raise Error(no='1_01_003', objectInfo=error_lists)
