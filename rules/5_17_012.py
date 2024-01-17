from model import Person
from error import Error

def process(record: Person):
    # 5_17_012-未消除风险防止防贫监测对象识别以来家中无县外务工人员但措施登记了外出务工补贴
    if (record.outInfo and record.objectInfo) is None:
        return
    famliy_num = len(record.family.member)
    if record.objectInfo['县']==None:
        print(1111)
    my_city = record.objectInfo['县']
    T = 0
    for i in range(famliy_num):
        if record.family.member[i].outInfo is not None:
            last = len(record.family.member[i].outInfo) - 1
            if record.family.member[i].outInfo[last]['年度交通费补助'] and record.family.member[i].outInfo[last]['务工所在县'] == my_city  \
                    and int(record.family.member[i].outInfo[last]['年度交通费补助'])>0:
                T = 1
    if  T and record.objectInfo['风险是否已消除']=='否':
        raise Error(no='5_17_012', outInfo=[record.outInfo[last]], objectInfo=[record.objectInfo])

 #record.objectInfo['监测对象类别'] != '' and "外出务工补贴" in record.objectInfo['就业帮扶'] and