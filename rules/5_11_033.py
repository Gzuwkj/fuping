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
        all_no_work and record.objectInfo['享受低保政策情况']!=''  and record.objectInfo['享受特困供养政策情况']!=''\
        and record.objectInfo['整户无劳动能力兜底保障户'] == '否' :
        raise Error(no='1111_07', objectInfo=[record.objectInfo])
    #and

# 用基础信息表中DE列“风险是否已消除”、AP列“劳动技能”、AV列“享受低保政策情况”BI列“享受特困供养政策情况”
# CH列“整户无劳动能力兜底保障户”以及E列“户编号”判断，以E列“户编号”为基础，该户家庭人口AP列“劳动技能”数据值为
# “无劳动力”丧失劳动力”，、AV列“享受低保政策情况”数据值不为“空”以及BI列“享受特困供养政策情况”数据值不为“空”
# 但CH列“整户无劳动能力兜底保障户”数据值为“否”，则为问题