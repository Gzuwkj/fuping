from model import Person
import pandas as pd
from error import Error
'''5_15_022-不同户月务工监测家庭成员登记的联系电话号码一致'''

phone_number_dict = {}
result = []
def process(record: Person):
    if record.objectInfo is None:
        return

    household_id = str(record.objectInfo.get("户编号", ""))
    phone_number = str(record.objectInfo.get("家庭成员联系电话", ""))

    if phone_number:
        if phone_number in phone_number_dict:
            existing_records = phone_number_dict[phone_number]
            for existing_record in existing_records:
                existing_household_id = existing_record["户编号"]
                if existing_household_id != household_id:
                    existing_records.append({
                        "户编号": household_id,
                        "电话号码": phone_number,
                        "其他信息": record.objectInfo
                    })
                    for i in existing_records:
                        result.append(i["其他信息"])

        else:
            phone_number_dict[phone_number] = [{
                "户编号": household_id,
                "电话号码": phone_number,
                "其他信息": record.objectInfo
            }]
    raise Error(no='5_15_022', objectInfo=result)
