from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if ('缺劳动力' in record.objectInfo.get('致贫/返贫风险1') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险2') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险3') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险4') or \
        '缺劳动力' in record.objectInfo.get('致贫/返贫风险5') ) \
            and record.objectInfo.get('风险是否已消除') == '否'\
            and len(record.objectInfo.get('监测对象类别')) != 0:

        bRaise = True
        for member in record.family.member:
            if member.objectInfo.get('劳动技能') == '无劳动力':
                bRaise = False
        if bRaise:
            raise Error(no='4_11_009', objectInfo=[record.objectInfo]
                        , msg='未消除风险的防止返贫监测对象户家庭成员均有劳动能力但风险类型为缺劳动力, 户编号:' + str(record.objectInfo.get('户编号')))