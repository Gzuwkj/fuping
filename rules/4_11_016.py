from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and len(record.objectInfo.get('监测对象类别')) != 0 \
            and '残疾人补贴' in record.objectInfo.get('综合保障')  \
            and record.objectInfo.get('证件类型') != '残疾人证' :

        bRaise = True
        for member in record.family.member:
            if member.objectInfo is not None:
                if member.objectInfo.get('证件类型') == '残疾人证':
                    bRaise = False


        if bRaise:
            raise Error(no='4_11_016', objectInfo=[record.objectInfo]
                        , msg='防止返贫监测对象户享受残疾人补贴帮扶措施但家中无残疾人口(含自然减少人员)')