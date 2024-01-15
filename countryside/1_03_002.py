from model import Person, DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        people_num = record.get('总人口数')
        if people_num == 0:
            raise Error(no='1_03_002', countryInfo=[record])



