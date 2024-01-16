from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime
import os

# 5_17_011-未消除风险防止防贫监测对象识别以来家中无县外务工人员但措施登记了劳务输出或外出务工补贴
id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.outInfo is not None:
        if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '否':
            if record.objectInfo['就业帮扶'] == '外出劳务补贴' or record.objectInfo['就业帮扶'] == '劳务输出':
                for info in record.outInfo:
                    if info['务工所在县'] == '' or info['务工所在县'] == '长顺县':
                        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                    outInfo=[record.outInfo[-1]],
                                    msg='5_17_011-未消除风险防止防贫监测对象识别以来家中无县外务工人员但措施登记了劳务输出或外出务工补贴')
