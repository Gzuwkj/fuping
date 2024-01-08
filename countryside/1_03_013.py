# 出列村出列村文化（图书）室个数为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        library_num = str(record.get('行政村文化（图书）室个数 （个）'))
        if library_num == '':
            raise Error(no='1_03_013', countryInfo=[record])
