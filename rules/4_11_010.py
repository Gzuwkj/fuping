from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and record.objectInfo.get('风险消除方式') == '帮扶消除' \
            and len(record.objectInfo.get('监测对象类别')) != 0 \
            and record.objectInfo.get('风险是否已消除') == '是' \
            and float(record.objectInfo.get('人均纯收入（元）')) < float(record.countryInfo.get('农民人均纯收入（元）')):
        raise Error(no='4_11_010', objectInfo=[record.objectInfo]
                        , msg='通过帮扶消除返（致）贫风险的监测对象风险消除时人均纯收入低于本省当年监测范围')