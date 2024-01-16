from model import Person
from error import Error
from typing import Dict, List
import os


# 1111_10-未消除风险监测对象帮扶措施登记了外出务工补贴措施但务工监测交通补贴为0
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '否' and \
            record.objectInfo['就业帮扶'] == '外出务工补贴':
        if record.outInfo is not None:
            for info in record.outInfo:
                if info['年度交通费补助'] == '' or info['年度交通费补助'] == '0':
                    raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                outInfo=[record.outInfo[-1]],
                                msg='1111_10-未消除风险监测对象帮扶措施登记了外出务工补贴措施但务工监测交通补贴为0')
