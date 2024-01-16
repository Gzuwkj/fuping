from model import Person
from error import Error


def process(record: Person):
    rescognition_rime = str(record.objectInfo.get('识别监测时间')).strip()
    salary = str(record.objectInfo.get('工资性收入')).strip()
    risk = str(record.objectInfo.get('致贫/返贫风险1')).strip()
    water_ensure = str(record.objectInfo.get('饮水安全保障')).strip()
    house_ensure = str(record.objectInfo.get('住房安全保障')).strip()
    education_ensure = str(record.objectInfo.get('义务教育保障')).strip()
    water_status = str(record.objectInfo.get('是否解决安全饮用水')).strip()
    if len(rescognition_rime) == 0 or len(salary) == 0 or len(risk) == 0 or len(water_status) == 0 or len(water_ensure) == 0 or len(house_ensure) == 0 or len(education_ensure) == 0:
        raise Error(no='1_11_002', objectInfo=[record.objectInfo])


