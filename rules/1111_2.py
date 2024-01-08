from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 1111_2-防贫监测对象家中有中职、高职人员但未享受雨露计划帮扶措施(识别以来8月以前识别)基础信息
    renyuan = 0
    for i in range(len(record.family.host.family.member)):
        if record.family.host.family.member[i].objectInfo is not None:
            if record.family.host.family.member[i].objectInfo['在校生状况'][:2] in ['中职', '高职']:
                renyuan = 1
    if renyuan and record.objectInfo['教育帮扶'] != '雨露计划':
            raise Error(no='1111_2', objectInfo=[record.objectInfo])