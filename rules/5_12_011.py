from model import Person
import pandas as pd
from error import Error

'''
5_12_011-防止返贫监测对象户是否实施开发式帮扶措施为是，产业帮扶仅填写其他、就业帮扶仅填写技能培训或其他、金融帮扶仅填写其他
'''


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("监测对象类别") != "" and record.objectInfo.get("实施开发式帮扶措施情况") == "是" \
            and record.objectInfo.get("产业帮扶") == "其他" and record.objectInfo.get("金融帮扶") == "其他" \
            and record.objectInfo.get("就业帮扶") in ["其他", "技能培训", "其他,技能培训", "技能培训,其他"]:
        raise Error(no='5_12_011', objectInfo=[record.objectInfo])
