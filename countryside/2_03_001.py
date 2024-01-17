# 出列村到乡镇未通硬化路
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        road = str(record.get('到乡镇是否通沥青（水泥）路'))
        if road == '' or road == '0':
            raise Error(no='2_03_001', countryInfo=[record])
