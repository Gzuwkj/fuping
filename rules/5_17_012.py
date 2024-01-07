from model import Person
from error import Error

def process(record: Person):
    # 5_17_012-未消除风险防止防贫监测对象识别以来家中无县外务工人员但措施登记了外出务工补贴
    if record.outInfo and record.objectInfo is None:
        return
    famliy_num = len(record.family.member)
    my_city = record.objectInfo['县']
    T = 1
    for i in range(famliy_num):
        if record.family.member[i].outInfo is None:
            last = len(record.family.member[i].outInfo) - 1
            if record.family.member[i].outInfo[last]['务工所在县'] == my_city:
                T = 0
    if record.objectInfo['监测对象类别'] != '' and "外出务工补贴" in record.objectInfo['就业帮扶'] and T:
        raise Error(no='5_17_012', outInfo=record.outInfo, objectInfo=[record.objectInfo])
