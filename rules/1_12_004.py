from model import Person
from error import Error
from typing import Dict, List

checksum_dict = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2'}
def check_id(id: str) -> bool:
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    factors = [int(id[i]) * weights[i] for i in range(17)]
    checksum = sum(factors) % 11
    return checksum_dict.get(checksum) == id[17]

def process(record: Person):
    if record.objectInfo is None:
        return
    if len(str(record.objectInfo.get('监测对象类别'))) != 0:
        if len(record.idCard) == 20 or len(record.idCard) == 22:
            if not check_id(record.idCard):
                raise Error(no='1_12_004', objectInfo=[record.objectInfo])





