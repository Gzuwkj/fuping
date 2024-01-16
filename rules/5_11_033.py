from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 5_11_033-未消除风险的整户无劳动能力防止返贫监测户未被标记成“整户无劳兜底保障户”  ####不懂
    all_no_work = 1
    for i in range(len(record.family.host.family.member)):
        if record.family.host.family.member[i].objectInfo is not None:
            if record.family.host.family.member[i].objectInfo['劳动技能'] != '无劳动力':
                all_no_work = 0
    if record.objectInfo['风险是否已消除'] == '否' and record.objectInfo['监测对象类别'] != '' and \
                record.objectInfo['整户无劳动能力兜底保障户'] != '是' and all_no_work:
        raise Error(no='1111_07', objectInfo=[record.objectInfo])

