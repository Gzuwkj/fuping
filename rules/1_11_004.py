from model import Person
from error import Error


# 已消除致贫返贫风险的监测对象未填写风险消除后收入、三保障和饮水状况指标信息
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        income = ['风险消除后工资性收入', '风险消除后财产性收入', '风险消除后转移性收入', '风险消除后生产经营性收入']
        safeguard = ['义务教育保障', '住房安全保障', '饮水安全保障']
        # 无饮水状况指标信息字段
        for i in income:
            if record.objectInfo.get(i) == '':
                raise Error(no='1_11_004', objectInfo=[record.objectInfo])

        for s in safeguard:
            if record.objectInfo.get(s) == '':
                raise Error(no='1_11_004', objectInfo=[record.objectInfo])
