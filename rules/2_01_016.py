from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

        # 2_01_016-脱贫人口医疗未保障（是否参加大病保险和否参加城乡居民基本医疗保险其中一项为否）
    if record.objectInfo['户类型'] == '脱贫户' and (record.objectInfo['是否参加大病保险'] == '否' or \
                                                record.objectInfo['是否参加城乡居民基本医疗保险'] == '否'):
        raise Error(no='2_01_016', objectInfo=[record.objectInfo])