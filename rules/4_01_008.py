from model import Person
from error import Error

def process(record: Person):
    if record.objectInfo is None:
        return

    if record.objectInfo.get('户类型') == '脱贫户' \
            and len(record.objectInfo.get('监测对象类别')) != 0 \
            and record.objectInfo.get('健康状况') == '残疾' \
            and record.objectInfo.get('劳动技能') == '普通劳动':
        raise Error(no='4_01_008', objectInfo=[record.objectInfo]
                         , msg='一、二级（重度）肢体残疾监测对象家庭成员有普通劳动能力')

        # bRaise = False
        # for member in record.family.member:
        #     if member.objectInfo is not None:
        #         if member.objectInfo.get('劳动技能') == '普通劳动':
        #             bRaise = True
        #
        #
        # if bRaise:
        #     raise Error(no='4_01_008', objectInfo=[record.objectInfo]
        #                 , msg='一、二级（重度）肢体残疾监测对象家庭成员有普通劳动能力')

