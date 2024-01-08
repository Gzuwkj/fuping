#  出列村公共卫生厕所个数为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        public_toilet = str(record.get('行政村公共卫生厕所个数'))
        if public_toilet == '':
            raise Error(no='1_03_010', countryInfo=[record])
