from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and record.objectInfo.get('证件类型') != '残疾人证' \
            and record.objectInfo.get('健康状况') == '残疾' :

        raise Error(no='4_12_003', objectInfo=[record.objectInfo]
                        , msg='监测对象人口健康状况为残疾但无残疾人证')