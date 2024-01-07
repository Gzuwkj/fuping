from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and record.objectInfo.get('综合保障') == '残疾人补贴' \
            and record.objectInfo.get('健康状况') != '残疾' \
            and len(record.objectInfo.get('文化程度')) == 0\
            and len(record.objectInfo.get('在校生状况')) == 0\
            and len(record.objectInfo.get('失学或辍学原因')) == 0:

        bRaise = True
        for member in record.family.member:
            if member.objectInfo is not None:
                if member.objectInfo.get('健康状况') == '残疾':
                    bRaise = False


        if bRaise:
            raise Error(no='4_11_016', objectInfo=[record.objectInfo]
                        , msg='防止返贫监测对象户享受残疾人补贴帮扶措施但家中无残疾人口(含自然减少人员)')