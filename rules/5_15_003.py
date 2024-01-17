from model import Person
from error import Error
from typing import Dict, List


def process(record: Person):
    if record.objectInfo is None:
        return
    public_welfare = str(record.objectInfo.get('公益性岗位'))
    time1 = str(record.objectInfo.get('公益性岗位(月数)'))
    if public_welfare != '' and (time1 == '' or time1 == '0'):
        raise Error(no='5_15_003', objectInfo=[record.objectInfo])


