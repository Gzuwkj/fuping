from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime


grade_status = ['高中一年级', '高中二年级', '高中三年级', '中职一年级', '中职二年级', '中职三年级']
def process(record: Person):
    if record.objectInfo is None:
        return
    grade = str(record.objectInfo.get('在校生状况')).strip()
    if grade in grade_status and len(str(record.objectInfo.get('监测对象类别')).strip()) != 0:
        birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
        currentDate = datetime.now()
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age < 15 or age > 20:
            raise Error(no='5_12_016', objectInfo=[record.objectInfo])