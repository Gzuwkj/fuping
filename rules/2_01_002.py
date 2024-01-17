from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    if len(str(record.objectInfo.get('健康状况')).strip()) == 0:
        raise Error(no='2_01_002', objectInfo=[record.objectInfo])
