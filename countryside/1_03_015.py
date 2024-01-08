from model import DictRecord
from error import Error
# 出列村特困供养人口数为空


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        special_hardship_support = str(record.get('特困供养人口数'))
        if special_hardship_support == '':
            raise Error(no='1_03_015', countryInfo=[record])
