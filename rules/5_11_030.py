from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if (len(record.objectInfo.get('产业帮扶')) != 0 or \
            len(record.objectInfo.get('公益岗位帮扶')) != 0 or \
            len(record.objectInfo.get('就业帮扶')) != 0 or \
            len(record.objectInfo.get('金融帮扶')) != 0) \
                and record.objectInfo.get('劳动技能') != '无劳动力' \
                and len(record.objectInfo.get('监测对象类别')) != 0 \
                and record.objectInfo.get('风险是否已消除0') == '否' \
                and (record.objectInfo.get('实施开发式帮扶措施情况') == '尚未实施' or
                        len(record.objectInfo.get('实施开发式帮扶措施情况')) == 0):

        raise Error(no='5_11_030', objectInfo=[record.objectInfo]
                        , msg='未消除风险且有劳动力的监测对象已登记开发式帮扶措施但选择已实施开发式帮扶措施为尚未实施或空')