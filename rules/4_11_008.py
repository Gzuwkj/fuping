from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('是否义务教育阶段适龄儿童少年失学辍学') == '是' :
        raise Error(no='4_11_008', objectInfo=record.objectInfo
                    , msg='2023年识别监测对象户义务教育阶段适龄儿童少年失学辍学但家中无义务教育阶段不在校儿童（含自然减少）')