from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime



def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get('在校生状况') == '小学' and record.objectInfo.get('户类型') == '脱贫户':
        birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
        currentDate = datetime.now()
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age < 6 or age > 14:
            raise Error(no='5_17_002', objectInfo=[record.objectInfo])



