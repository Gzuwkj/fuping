from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return
    detecting_objects = str(record.objectInfo.get('监测对象类别'))
    risk = str(record.objectInfo.get('风险是否已消除'))
    if detecting_objects != '' and risk == '是':
        if str(record.objectInfo.get('风险消除后是否义务教育阶段适龄儿童少年失学辍学')) == "是":
            raise Error(no='1_11_005', objectInfo=[record.objectInfo])
