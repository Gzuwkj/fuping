from model import Person
from error import Error
from typing import Dict, List
import os
import datetime

id2record: Dict[str, List[Person]] = {}
def process(record: Person):
    if record.objectInfo is None:
        return
    # 5_15_023-未消除风险识别时收入填写不合理（识别时工资性收入大于0小于100）
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '是' and (record.objectInfo['信息采集人'] == '' and record.objectInfo['信息采集人联系电话']):
        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                    msg='1_11_011-已消除返（致）贫风险的监测对象未填写监测联系人和监测联系人电话')





