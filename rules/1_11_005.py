from model import Person
from error import Error


# 已消除致贫返贫风险的监测对象住危房
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["风险是否已消除"] == "是":
        for m in record.family.member:
            chuoxueshixue = str(m.objectInfo.get('风险消除后是否义务教育阶段适龄儿童少年失学辍学'))
            if chuoxueshixue == "是":
                raise Error(no='1_11_005', objectInfo=[record.objectInfo])
            else:
                continue
