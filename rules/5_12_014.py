from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime



def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get('在校生状况') == '小学' and len(str(record.objectInfo.get('监测对象类别'))) != 0:
        birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
        currentDate = datetime.now()
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age < 6 or age > 14:
            raise Error(no='5_12_014', objectInfo=[record.objectInfo])



