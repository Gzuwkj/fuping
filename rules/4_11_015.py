from model import Person
import pandas as pd
from error import Error

'''
4_11_015-防止返贫监测对象户享受低保或特困帮扶措施但家中无低保或特困供养人口(含自然减少人员)
'''


def process(record: Person):
    if record.objectInfo is None:
        return

    monitoring_category = record.objectInfo.get("监测对象类别")
    comprehensive_support = record.objectInfo.get("综合保障")
    special_support = record.objectInfo.get("享受特困供养政策情况")
    low_support = record.objectInfo.get("享受低保政策情况")

    if monitoring_category != "" and ("低保" in comprehensive_support or "特困供养" in comprehensive_support):
        if not (special_support in ["城市特困", "农村特困"] or low_support in ["城市低保", "农村低保"]):
            raise Error(no='4_11_015', objectInfo=[record.objectInfo])
