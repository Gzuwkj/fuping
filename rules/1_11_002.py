from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return
    if len(str(record.objectInfo.get('监测对象类别'))) != 0:
        rescognition_rime = str(record.objectInfo.get('识别监测时间0')).strip()
        risk = str(record.objectInfo.get('致贫/返贫风险1')).strip()
        house_ensure = str(record.objectInfo.get('是否危房户')).strip()
        water_ensure = str(record.objectInfo.get('是否解决安全饮用水')).strip()
        health_ensure = str(record.objectInfo.get('是否参加大病保险')).strip()

        if len(rescognition_rime) == 0 or len(risk) == 0 or len(water_ensure) == 0 or len(house_ensure) == 0 or len(health_ensure) == 0:
            raise Error(no='1_11_002', objectInfo=[record.objectInfo])
