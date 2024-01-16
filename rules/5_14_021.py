from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return
    distance = str(record.objectInfo.get('与村主干路距离'))
    if distance == '':
        raise Error(no='5_14_021', objectInfo=[record.objectInfo])



