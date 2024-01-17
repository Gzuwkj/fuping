from model import Person
from error import Error


# 已消除致贫返贫风险的监测对象住危房
def process(record: Person):
    if record.objectInfo is None:
        return
    detecting_objects = str(record.objectInfo.get('监测对象类别'))
    risk = str(record.objectInfo.get('风险是否已消除'))
    if detecting_objects != '' and risk == '是':
        decrepit_house = str(record.objectInfo.get('是否危房户'))
        if decrepit_house == '是':
            raise Error(no='1_11_006', objectInfo=[record.objectInfo])