# 出列村残疾人口数为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        disabled_num = str(record.get('残疾人口数'))
        if disabled_num == '':
            raise Error(no='1_03_016', countryInfo=[record])
