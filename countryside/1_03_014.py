from model import DictRecord
from error import Error
# 出列村低保户数或低保人数为空


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        low_income_family_num = str(record.get('低保人口数'))
        low_income_people_num = str(record.get('低保户数'))
        if low_income_family_num == '' or low_income_people_num == '':
            raise Error(no='1_03_014', countryInfo=[record])
