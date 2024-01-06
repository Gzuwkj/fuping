'''3_01_007-脱贫人员未参加城乡居民（城镇职工）基本医疗保险，但是否接受大病医疗救助选项为是'''
from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get("户类型") == "脱贫户" and \
            (record.objectInfo.get("是否参加城乡居民基本医疗保险") == "否" or record.objectInfo.get("是否参加城镇职工基本医疗保险") == "否") and\
            record.objectInfo.get("是否接受医疗救助") == "是":
        raise Error(no='3_01_003', objectInfo=[record.objectInfo])