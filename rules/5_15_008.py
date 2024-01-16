from model import Person
from error import Error

def process(record: Person):
    if record.previewInfo is None:
        return

    previewInfoRecord = []
    for previewInfo in record.previewInfo:
        if previewInfo.get('是否计划务工') == '是' \
            and len(previewInfo.get('就业服务需求')) == 0:
            previewInfoRecord.append(previewInfo)

    if len(previewInfoRecord) != 0:
        raise Error(no='5_15_008', previewInfo=previewInfoRecord
                        , msg='脱贫人口务工监测有计划外出务工未填写务工需求')

