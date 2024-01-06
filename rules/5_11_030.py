from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and record.objectInfo.get('劳动技能') != '无劳动力' \
            and record.objectInfo.get('风险是否已消除0') == '否' \
            and record.objectInfo.get('实施开发式帮扶措施情况') != '已实施':

        raise Error(no='5_11_030', record=record
                        , msg='未消除风险且有劳动力的监测对象已登记开发式帮扶措施但选择已实施开发式帮扶措施为尚未实施或空')