from model import Person
from error import Error


# 已消除致贫返贫风险的监测对象未填写风险消除后收入、三保障和饮水状况指标信息
# 用M列“监测对象类别”来判定是否是监测对象，不为“空”的则为监测对象；
# 用DE列“风险是否已消除”来判定，为“是”则为消除返（致）贫风险的监测对象；
# 但FI列“风险消除后是否义务教育阶段适龄儿童少年失学辍学”至FU列“风险消除后合规自付支出”为空，则为问题
def process(record: Person):
    if record.objectInfo is None:
        return
    detecting_objects = str(record.objectInfo.get('监测对象类别'))
    risk = str(record.objectInfo.get('风险是否已消除'))

    if detecting_objects != '' and risk == '是':
        question = ["风险消除后是否义务教育阶段适龄儿童少年失学辍学", "风险消除后是否住房损毁", "风险消除后是否有家庭成员未参加城乡居民（职工）基本医疗保险",
                    "风险消除后是否饮水设施损毁", "风险消除后工资性收入", "风险消除后财产性收入", "风险消除后转移性收入", "风险消除后生产经营性收入", "风险消除后生产经营性支出",
                    "风险消除后家庭纯收入", "风险消除后家庭人均纯收入", "风险消除后理赔收入", "风险消除后合规自付支出"]
        for q in question:
            if record.objectInfo.get(q) == '':
                raise Error(no='1_11_004', objectInfo=[record.objectInfo])

