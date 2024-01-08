# 出列村总户数为空或0
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        total_number = record.get('总户数')
        if total_number == '' or total_number == '0' or total_number == 0:
            raise Error(no='3_03_003', countryInfo=[record])
