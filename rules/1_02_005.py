from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime


def process(record: Person):
    if record.objectInfo is None:
        return
    birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
    currentDate = datetime.now()
    if (int(birthDate.year), int(birthDate.year), int(birthDate.day)) >= (2007, 9, 30):
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age >= 6 and age <= 16:
            if len(str(record.objectInfo.get('在校生状况')).strip()) == 0 and len(str(record.objectInfo.get('义务教育阶段未上学原因')).strip()) == 0:
                raise Error(no='1_02_005', objectInfo=[record.objectInfo])

