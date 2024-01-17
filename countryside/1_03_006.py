from model import Person, DictRecord
from error import Error
from typing import Dict, List


# 出列村参加城乡居民基本养老保险人数为空
def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        basic_insurance_num = str(record.get('参加城乡居民基本养老保险人数'))
        if basic_insurance_num == '':
            raise Error(no='1_03_006', countryInfo=[record])



