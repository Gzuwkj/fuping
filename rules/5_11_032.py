from model import Person
from error import Error
from typing import Dict, List
import os

id2record: Dict[str, List[Person]] = {}


# 5_11_032-有劳动能力的未消除风险监测对象户仅享受综合保障一项措施
def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo['监测对象类别'] != '' and record.objectInfo['风险是否已消除'] == '否':
        if record.objectInfo['劳动技能'] == '普通劳动力' or record.objectInfo['劳动技能'] == '技能劳动力':
                if record.objectInfo['综合保障'] != '' and \
                        record.objectInfo['义务教育保障'] == '' and \
                        record.objectInfo['健康帮扶'] == '' and \
                        record.objectInfo['产业帮扶'] == '' and \
                        record.objectInfo['住房安全保障'] == '' and \
                        record.objectInfo['公益岗位帮扶'] == '' and \
                        record.objectInfo['公益性岗位帮扶其他备注'] == '' and \
                        record.objectInfo['就业帮扶'] == '' and \
                        record.objectInfo['搬迁'] == '' and \
                        record.objectInfo['生产生活条件改善'] == '' and \
                        record.objectInfo['教育帮扶'] == '' and \
                        record.objectInfo['社会帮扶'] == '' and \
                        record.objectInfo['金融帮扶'] == '' and \
                        record.objectInfo['饮水安全保障'] == '' and \
                        record.objectInfo['基础设施建设'] == '':
                        raise Error(no=os.path.basename(__file__)[:-3], objectInfo=[record.objectInfo],
                                msg='5_11_032-有劳动能力的未消除风险监测对象户仅享受综合保障一项措施')
