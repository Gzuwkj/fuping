from model import Person
import pandas as pd
from error import Error

'''
5_16_003-未消除风险的防止返贫监测对象家庭成员享受农村最低生活保障但帮扶措施未勾选低保
'''


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("监测对象类别") != "" and record.objectInfo.get("风险是否已消除0") == "否" \
            and record.objectInfo.get("享受低保政策情况") in ["城市低保", "农村低保"] and "低保" not in record.objectInfo.get("综合保障"):
        raise Error(no='5_16_003', objectInfo=[record.objectInfo])
