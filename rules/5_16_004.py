from model import Person
import pandas as pd
from error import Error

'''
5_16_004-未消除风险的防止返贫监测对象家庭成员享受特困供养但帮扶措施未勾选特困供养
'''


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("监测对象类别") != "" and record.objectInfo.get("风险是否已消除0") == "否" \
            and record.objectInfo.get("享受特困供养政策情况") in ["城市特困", "农村特困"]\
            and "特困供养" not in record.objectInfo.get("综合保障"):
        raise Error(no='5_16_004', objectInfo=[record.objectInfo])
