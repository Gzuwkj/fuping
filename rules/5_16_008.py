from model import Person
import pandas as pd
from error import Error

'''
5_16_008-未消除风险防止返贫监测对象家中有一二级残疾人但帮扶措施未登记残疾人补贴（含自然减少人员）
'''

def check_id(id: str) -> bool:
    if len(id) == 20 and (id[19] == "1" or id[19] == "2"):
        return True
    else:
        return False

def process(record: Person):
    if record.objectInfo is None:
        return

    risk_conditions = [
        record.objectInfo.get(f"致贫/返贫风险{i}") == "因残" for i in range(1, 4)
    ]

    if record.objectInfo.get("监测对象类别") != "" and record.objectInfo.get("风险是否已消除0") == "否" and any(risk_conditions) and check_id(record.idCard):
        if "残疾人补贴" not in record.objectInfo.get("综合保障"):
            raise Error(no='5_16_008', objectInfo=[record.objectInfo])




