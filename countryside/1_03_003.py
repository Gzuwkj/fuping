from model import Person, DictRecord
from error import Error
from typing import Dict, List


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        people_income = str(record.get('村级集体经济收入（万元）'))
        if people_income == '' or people_income == '0':
            raise Error(no='1_03_003', countryInfo=[record])



