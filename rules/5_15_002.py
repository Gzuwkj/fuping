from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return
    electricity = str(record.objectInfo.get('是否通生活用电'))
    detecting_objects = str(record.objectInfo.get('监测对象类别'))
    if detecting_objects != '' and electricity == '':
        raise Error(no='5_15_002', objectInfo=[record.objectInfo])



