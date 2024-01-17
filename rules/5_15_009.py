from model import Person
from error import Error

def process(record: Person):

    if record.previewInfo is None:
        return
    if record.objectInfo is None:
        return

    previewInfoRecord = []
    if len(record.objectInfo.get('监测对象类别')) != 0:
        for previewInfo in record.previewInfo:
            if previewInfo.get('户类型') == '脱贫户' \
                and previewInfo.get('是否计划务工') == '是' \
                and len(previewInfo.get('就业服务需求')) == 0:
                previewInfoRecord.append(previewInfo)

    if len(previewInfoRecord) != 0:
        raise Error(no='5_15_009', outInfo=[previewInfo], previewInfo= previewInfoRecord
                            , msg='监测对象人口务工监测有计划外出务工未填写务工需求')