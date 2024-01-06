from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    reason = record.objectInfo.get('致贫/返贫风险1')
    if record.objectInfo.get('是否参加城乡居民基本医疗保险') != '是' \
            and type(reason) == str \
            and reason != '因病':
        raise Error(no='4_11_007', record=record, msg='监测对象户三保障和饮水状况为有家庭成员未参加城乡居民（职工）基本医疗保险但致（返）贫风险没有因病')