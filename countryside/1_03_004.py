from model import Person, DictRecord
from error import Error
from typing import Dict, List


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        school_num = str(record.get('村小学（个数）'))
        if school_num == '':
            raise Error(no='1_03_004', countryInfo=[record])



