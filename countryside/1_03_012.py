# 出列村垃圾集中堆放点个数为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        rubbish_dump = str(record.get('行政村生产生活垃圾集中堆放点个数（个）'))
        if rubbish_dump == '':
            raise Error(no='1_03_012', countryInfo=[record])
        