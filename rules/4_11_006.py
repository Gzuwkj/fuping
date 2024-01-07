from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('是否解决安全饮用水') != '是':
        raise Error(no='4_11_006', objectInfo=[record.objectInfo],
                    msg='监测对象户三保障和饮水状况为饮水出现安全问题但致（返）贫风险没有因安全饮水')