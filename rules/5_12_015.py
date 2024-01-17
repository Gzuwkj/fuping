from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime


grade = ['七年级', '八年级', '九年级']
def process(record: Person):
    if record.objectInfo is None:
        return
    if str(record.objectInfo.get('在校生状况')).strip() in grade and len(str(record.objectInfo.get('监测对象类别')).strip()) != 0:
        birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
        currentDate = datetime.now()
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age < 12 or age > 17:
            raise Error(no='5_12_015', objectInfo=[record.objectInfo])
