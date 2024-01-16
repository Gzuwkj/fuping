from model import Person
from error import Error
from typing import Dict, List
##4_01_003-脱贫人口无身份证号（含前6位6个9）
# id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.idCard ==None or record.idCard[:6]=='999999':
        raise Error(no='4_01_003', objectInfo=[record.objectInfo])