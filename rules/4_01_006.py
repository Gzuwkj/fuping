from model import Person
from error import Error
import pandas as pd

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
        and ( '高中' in record.objectInfo.get('在校生状况') or \
              '初中' in record.objectInfo.get('在校生状况') or \
              '小学' in record.objectInfo.get('在校生状况') or\
              '学前教育' in record.objectInfo.get('在校生状况') or\
              '学龄前儿童' in record.objectInfo.get('在校生状况')):

        if record.outInfo is None:
            return
        for outInfo in record.outInfo:
            if outInfo.get('是否已务工') == '是':
                raise Error(no='4_01_006', objectInfo=[record.objectInfo]
                            , msg='在校生状况选择高中、初中、小学、学前教育或学龄前儿童的脱贫人口填写了已外出务工或计划完成务工(改为在校生不为空)')

        if record.previewInfo is None:
            return
        for previewInfo in record.previewInfo:
            if previewInfo.get('是否计划务工') == '是':
                raise Error(no='4_01_006', objectInfo=[record.objectInfo]
                            , msg='在校生状况选择高中、初中、小学、学前教育或学龄前儿童的脱贫人口填写了已外出务工或计划完成务工(改为在校生不为空)')


