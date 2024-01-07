from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return
        # 1111_13- 4月份及后识别监测对象登记参加城乡居民基本医疗保险个人缴费补贴
    if '城乡居民基本医疗保险个人缴费补贴' in record.objectInfo['健康帮扶']:
        raise Error(no='1111_13', objectInfo=[record.objectInfo])