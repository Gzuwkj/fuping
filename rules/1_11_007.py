from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return
    detecting_objects = str(record.objectInfo.get('监测对象类别'))
    risk = str(record.objectInfo.get('风险是否已消除'))
    if detecting_objects != '' and risk == '是':
        safe_water = str(record.objectInfo.get('是否解决安全饮用水'))
        if safe_water == "否":
            raise Error(no='1_11_007', objectInfo=[record.objectInfo])

