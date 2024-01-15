from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('是否参加城乡居民基本医疗保险') == '否' \
            and record.objectInfo.get('致贫/返贫风险1') != '因病'\
            and record.objectInfo.get('是否解决安全饮用水') != '是'\
            and record.objectInfo.get('是否危房户') != '否'\
            and record.objectInfo.get('是否义务教育阶段适龄儿童少年失学辍学') != '否':

        raise Error(no='4_11_007', objectInfo=[record.objectInfo]
                    , msg='监测对象户三保障和饮水状况为有家庭成员未参加城乡居民（职工）基本医疗保险但致（返）贫风险没有因病')