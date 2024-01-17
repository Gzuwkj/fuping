from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

def process(record: Person):
    if record.objectInfo is None:
        return
    health_problem = False
    house_water_problem = False
    education_problem = False

    health_status =  str(record.objectInfo.get('是否参加大病保险')).strip()
    if health_status == '否' or len(health_status) == 0:
        health_problem = True

    house_status = str(record.objectInfo.get('是否危房户')).strip()
    water_status = str(record.objectInfo.get('是否解决安全饮用水')).strip()
    if house_status == '是' or water_status == '否':
        house_water_problem = True

    birthDate = datetime.strptime(record.idCard.strip()[6:14], "%Y%m%d")
    currentDate = datetime.now()
    if (int(birthDate.year), int(birthDate.year), int(birthDate.day)) >= (2007, 9, 30):
        age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        if age >= 6 and age <= 16:
            if len(str(record.objectInfo.get('在校生状况')).strip()) == 0 and len(str(record.objectInfo.get('义务教育阶段未上学原因')).strip()) == 0:
                education_problem = True

    if health_problem or house_water_problem or education_problem:
        raise Error(no='1_02_007', objectInfo=[record.objectInfo])

