# 出列村未解决饮水农户数、住危房农户数大于总农户数
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        drinking_water = int(record.get('未实现饮水安全户数'))
        dangerous_house = int(record.get('危房户数'))
        total_number = int(record.get('总户数'))
        if drinking_water + dangerous_house > total_number:
            raise Error(no='3_03_001', countryInfo=[record])
