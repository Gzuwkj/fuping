from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and not pd.isna(record.objectInfo.get('公益岗位帮扶')) \
            and not pd.isna(record.objectInfo.get('就业帮扶')) \
            and record.objectInfo.get('年收入（元）') == 0 \
            and record.objectInfo.get('风险是否已消除0') == '否' :

        raise Error(no='4_11_014', record=record
                        , msg='2023年识别或未消除风险防止返贫监测对象户享受就业或公益岗位帮扶措施但家中无务工人口')