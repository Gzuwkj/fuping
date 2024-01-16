from model import Person
from error import Error
from datetime import  datetime


def process(record: Person):
    if record.objectInfo is None:
        return
    data = record.objectInfo.get('识别监测时间')
    if len(str(record.objectInfo.get('监测对象类别'))) != 0:
        if len(str(data).strip()) == 6:
            recognition_date = datetime.strptime(data,"%Y%m")
            today_date = datetime.now()
            if today_date.year == recognition_date.year:
                date_difference = today_date.month - recognition_date.month
            else:
                if (today_date.year - recognition_date.year) == 1:
                    date_difference = (12-recognition_date.month) + today_date.month
                else:
                    date_difference =(today_date.year - recognition_date.year - 1)*12 + (12 - recognition_date.month) + today_date.month
            if date_difference > 1:
                chanye = len(str(record.objectInfo.get('产业帮扶')).strip())
                zhufang = len(str(record.objectInfo.get('住房安全保障')).strip())
                jiankang = len(str(record.objectInfo.get('健康帮扶')).strip())
                gongyi = len(str(record.objectInfo.get('公益性岗位帮扶')).strip())
                gongyyibeizhu = len(str(record.objectInfo.get('公益性岗位帮扶其他备注')).strip())
                jiuye = len(str(record.objectInfo.get('就业帮扶')))
                banqian = len(str(record.objectInfo.get('搬迁')).strip())
                tiaojian = len(str(record.objectInfo.get('生产生活条件改善')).strip())
                jiaoyu = len(str(record.objectInfo.get('教育帮扶')).strip())
                shehui = len(str(record.objectInfo.get('社会帮扶')).strip())
                jinrong = len(str(record.objectInfo.get('金融帮扶')).strip())
                yinshui = len(str(record.objectInfo.get('饮水安全保障')).strip())
                zonghe = len(str(record.objectInfo.get('综合保障')).strip())
                sheshi = len(str(record.objectInfo.get('基础设施建设')).strip())
                if chanye + zhufang + jiankang + gongyi + gongyyibeizhu + jiuye + banqian + tiaojian + jiaoyu + shehui + jinrong + yinshui + zonghe + sheshi == 0:
                    raise Error(no='1_11_010.py', objectInfo=[record.objectInfo])







