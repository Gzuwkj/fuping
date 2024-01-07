from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    strSecurity = record.objectInfo.get('综合保障')
    if record.objectInfo.get('户类型') == '脱贫户' \
            and (strSecurity == '低保' or strSecurity == '特困供养' or strSecurity == '残疾人补贴' )\
            and record.objectInfo.get('转移性收入') == 0 \
            and record.objectInfo.get('风险是否已消除0') == '是' :

        raise Error(no='4_11_013', objectInfo=record.objectInfo
                        , msg='已消除风险户享受低保、特困供养、残疾人补贴但消除后无转移性收入')