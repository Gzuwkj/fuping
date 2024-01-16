# -*- coding: utf-8 -*-
import re
from datetime import datetime

from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}
def is_valid_phone_number(phone_number):
    """
    判断是否为有效的手机号码
    """
    pattern = re.compile(r'^1[3456789]\d{9}$')
    return bool(re.match(pattern, phone_number))

def process(record: Person):
    if record.objectInfo is None:
        return

    phone_number_field = '家庭成员联系电话'  # 请将这个字段替换为实际的字段名称
    work_location_field = '务工所在地'  # 请将这个字段替换为实际的字段名称

    phone_number = record.objectInfo.get(phone_number_field, None)
    work_location = record.objectInfo.get(work_location_field, None)

    if (
        work_location is not None and isinstance(work_location, str) and work_location.strip() != ''
        and phone_number is not None and isinstance(phone_number, str) and not is_valid_phone_number(phone_number)
    ):
        raise Error(no='2_12_007', objectInfo=[record.objectInfo])