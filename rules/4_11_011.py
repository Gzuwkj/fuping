from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and record.objectInfo.get('劳动技能') == '无劳动力' \
            and record.objectInfo.get('风险是否已消除0') == '是' :

        bRaise = True
        for member in record.family.member:
            if member.objectInfo is not None:
                if member.objectInfo.get('劳动技能') != '无劳动力':
                    bRaise = False
            else:
                bRaise = False

        if bRaise:
            raise Error(no='4_11_011', objectInfo=record.objectInfo
                        , msg='整户无劳动力监测对象户已消除风险(含自然减少)')