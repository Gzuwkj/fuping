from model import Person
from error import Error

def process(record: Person):
    process123(record)
    process201(record)
    

def process123(record: Person):
    if record.objectInfo is None:
        return

    if len(record.objectInfo.get('在校生状况')) != 0\
            and len(record.objectInfo.get('监测对象类别')) != 0:

        outInfoRecord = []
        if record.outInfo is not None:
            for outInfo in record.outInfo:
                if outInfo.get('是否已务工') == '是':
                    outInfoRecord.append(outInfo)

        previewInfoRecord = []
        if record.previewInfo is not None:
            for previewInfo in record.previewInfo:
                if previewInfo.get('是否计划务工') == '是':
                    previewInfoRecord.append(previewInfo)

        if len(outInfoRecord) != 0 or len(previewInfoRecord) != 0:
            raise Error(no='4_01_006_123', objectInfo=[record.objectInfo], outInfo=outInfoRecord, previewInfo=previewInfoRecord
                        , msg='在校生状况选择高中、初中、小学、学前教育或学龄前儿童的脱贫人口填写了已外出务工或计划完成务工(改为在校生不为空)')





'''4_01_006-在校生状况选择高中、初中、小学、学前教育或学龄前儿童的脱贫人口填写了已外出务工(改为在校生不为空，基础信息)'''


def process201(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo.get("在校生状况") != "" and record.objectInfo.get("户类型") == "脱贫户":
        if record.outInfo is not None:
            raise Error(no='4_01_006_201', objectInfo=[record.objectInfo], outInfo=record.outInfo)