from model import Person
from error import Error

huIds = set()

def process(record: Person):

    if record.objectInfo is None:
        return

    if ('缺劳动力' in record.objectInfo.get('致贫/返贫风险1') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险2') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险3') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险4') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险5') ) \
            and record.objectInfo.get('劳动技能') != '无劳动力' \
            and len(record.family.member) >= 4 \
            and len(record.objectInfo.get('监测对象类别')) != 0:

        count = 1
        for member in record.family.member:
            if member.objectInfo.get('劳动技能') != '无劳动力':
                count += 1

        thisHuId = str(record.objectInfo.get('户编号'))
        if count >= len(record.family.member) / 2 and thisHuId not in huIds:
            huIds.add(thisHuId)
            raise Error(no='5_11_029', objectInfo=[record.objectInfo]
                        , msg='未消除风险的监测对象(4人户及以上)一半以上家庭成员有劳动能力（普+技）但风险类型为缺劳动力, 户编号:' + str(thisHuId))