from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return
    safe_water = str(record.objectInfo.get('是否解决安全饮用水'))
    if safe_water == "否":
        raise Error(no='1_11_007', objectInfo=[record.objectInfo])

