#  出列村卫生室个数为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        health_room = str(record.get('行政村卫生室个数'))
        if health_room == '':
            raise Error(no='1_03_009', countryInfo=[record])
