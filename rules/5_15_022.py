from model import Person
import pandas as pd
from error import Error
'''5_15_022-不同户月务工监测家庭成员登记的联系电话号码一致'''

phone_number_dict = {}
def process(record: Person):
    if record.objectInfo is None:
        return

    household_id = str(record.objectInfo.get("户编号", ""))
    phone_number = str(record.objectInfo.get("家庭成员联系电话", ""))

    if phone_number:
        if phone_number in phone_number_dict:
            existing_household_id = phone_number_dict[phone_number]
            if existing_household_id != household_id:
                raise Error(no='5_15_022', objectInfo=[record.objectInfo])
        else:
            phone_number_dict[phone_number] = household_id
