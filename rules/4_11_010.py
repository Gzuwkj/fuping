from model import Person
from error import Error


def process(record: Person):
    if record.objectInfo is None:
        return

    # TODO: 暂时拿不到 countryInfo信息
    shi = record.objectInfo.get('市')
    xian = record.objectInfo.get('县')
    xiang = record.objectInfo.get('乡')
    cun = record.objectInfo.get('村')
    if record.objectInfo.get('户类型') == '脱贫户' \
            and type(record.objectInfo.get('农民人均纯收入（元）')) == float \
            and record.objectInfo.get('人均纯收入（元）') < record.objectInfo.get('农民人均纯收入（元）'):
        print(11)
        raise Error(no='4_11_010', record=record
                        , msg='通过帮扶消除返（致）贫风险的监测对象风险消除时人均纯收入低于本省当年监测范围')