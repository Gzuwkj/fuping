from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 未消除风险防止返贫监测对象户返（致）贫风险为“缺劳动力”但家中人员劳动力占比超过四分之一（技能劳动力和普通劳动力）
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['致贫/返贫风险1'] == '缺劳动力':
        power = 0
        for index, member in enumerate(record.family.member):
            if member.objectInfo is not None:
                if member.objectInfo['劳动技能'] == '普通劳动力' or member.objectInfo['劳动技能'] == '技能劳动力':
                    power += 1
        if power / record.family.member.__len__() > 0.25:
            raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                        msg='未消除风险防止返贫监测对象户返（致）贫风险为“缺劳动力”但家中人员劳动力占比超过四分之一（技能劳动力和普通劳动力）')
