from model import Person
from error import Error


# 监测对象家庭成员文化程度和在校生状况同时填报
def process(record: Person):
    if record.objectInfo is None:
        return
    member = record.family.member
    for m in member:
        education_level = str(m.objectInfo.get('文化程度'))
        school_situation = str(m.objectInfo.get('在校生状况'))
        if education_level != '' and school_situation != '':
            raise Error(no='3_12_004', objectInfo=[record.objectInfo])

