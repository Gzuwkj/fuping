from model import Person
import pandas as pd
from error import Error

'''
5_16_005-未消除风险防止返贫监测对象家中无人享受低保但帮扶措施登记低保名单（含自然减少人员）
'''


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("监测对象类别") != "" and record.objectInfo.get("风险是否已消除0") == "否" \
            and record.objectInfo.get("享受低保政策情况") in ["", "未享受"] and "低保" in record.objectInfo.get("综合保障"):
        raise Error(no='5_16_005', objectInfo=[record.objectInfo])
