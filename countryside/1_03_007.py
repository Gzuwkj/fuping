# 出列村是否通客运班车为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        bus = str(record.get('是否通客运班车'))
        if bus == '':
            raise Error(no='1_03_007', countryInfo=[record])
