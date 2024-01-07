# 出列村出列村执业（助理）医师数为空
from model import DictRecord
from error import Error


def process(record: DictRecord):
    if record is None:
        return
    if str(record.get('是否出列')) == '是':
        doctor_num = str(record.get('行政村执业（助理）医师（人）'))
        if doctor_num == '':
            raise Error(no='1_03_011', countryInfo=[record])
