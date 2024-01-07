# -*- coding: utf-8 -*-
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime

id2record: Dict[str, List[Person]] = {}


def calculate_age(birthdate: str):
    birth_date = datetime.strptime(str(int(float(birthdate))), "%Y%m%d")
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def process(record: Person):
    if record.family is not None and record.family.host is not None:
        household_type = record.objectInfo.get("户类型")
        birthdate = record.objectInfo.get("出生日期")
        public_service_position = record.objectInfo.get("公益性岗位")

        if household_type == "脱贫户" and calculate_age(birthdate) < 16 and public_service_position is not None:
            raise Error(no='3_01_008', objectInfo=[record.objectInfo],
                        msg="16岁以下脱贫人口参加公益性岗位")


