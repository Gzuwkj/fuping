from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None or record.objectInfo['识别监测时间']=='':
        return
        # 1111_2-防贫监测对象家中有中职、高职人员但未享受雨露计划帮扶措施(识别以来8月以前识别)基础信息
    time=0

    if 202208 >= int(float(record.objectInfo['识别监测时间'])):
        time = 1
    renyuan = 0
    for i in range(len(record.family.host.family.member)):
        if record.family.host.family.member[i].objectInfo is not None:
            if record.family.host.family.member[i].objectInfo['在校生状况'][:2] in ['中职', '高职']:
                renyuan = 1
    if renyuan and record.objectInfo['教育帮扶'] != '雨露计划'and  record.objectInfo['监测对象类别'] != ''and time:
            raise Error(no='1111_2', objectInfo=[record.objectInfo])

    # M列“监测对象类别”、DF列“识别监测时间”结合AO列“在校生状况”、EZ列“教育帮扶”判断，
    # 如DF列“识别监测时间”数据值在8月以前，而AO列“在校生状况”数据值为“中职一年级”、“中职二年级”、“中职三年级”
    # 和“高职高专一年级”、“高职高专二年级”、“高职高专三年级”但EZ列“教育帮扶”数据值不为“雨露计划”，
    # 则为问题