from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and len(record.objectInfo.get('监测对象类别')) != 0 \
            and (len(record.objectInfo.get('公益岗位帮扶')) != 0\
                  or len(record.objectInfo.get('就业帮扶')) != 0) \
            and record.objectInfo.get('工资性收入') == 0 \
            and record.objectInfo.get('风险是否已消除0') == '是' :

        raise Error(no='4_11_012', objectInfo=[record.objectInfo]
                        , msg='已消除风险户享受就业或者公益性岗位帮扶但消除后无工资性收入')