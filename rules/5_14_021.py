from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return
    detecting_objects = str(record.objectInfo.get('监测对象类别'))
    distance = str(record.objectInfo.get('与村主干路距离'))
    if detecting_objects != '' and distance == '':
        raise Error(no='5_14_021', objectInfo=[record.objectInfo])



