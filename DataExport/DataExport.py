import records
import pandas
from DataExport.Member import Member

print('start')
# 连接数据库
# import member
# host='mysql'
# port=3306
# database='queenoa'
# username='test'
# password='369852lpLP;'
url = 'mysql+pymysql://test:369852lpLP;@148.70.108.183:3306/queenoa'
db = records.Database(url)

# 获取数据总数
countData = db.query('select count(*) as count from member')
count = countData.first().count;

# 循环查询数据，每次1000条
startNum = 1
pageNum = 1000
currentMaxMemberId = 0
while startNum * pageNum < count:
    # 拼接sql
    sql = 'select * from member' + ' where member_id > ' + str(currentMaxMemberId) + \
          ' order by member_id asc' + ' limit 0 , ' + str(pageNum)
    print('sql-' + sql)
    # 执行sql
    rowDate = db.query(sql)
    # 存放对象的集合
    export_list = []
    # 循环查询到的行数据
    for row in rowDate:
        memberData = Member(row.member_id, row.address, row.member_name, row.mobile_no)
        export_list.append({'member_id':memberData.member_id,
                            'member_address':memberData.address,
                            'member_name':memberData.member_name,
                            'mobile_no':memberData.mobile_no})
    # 过滤掉上次查询到的数据，避免过多数据造成的分页查询性能低下
    if len(rowDate) != 0:
        currentMaxMemberId = rowDate[len(rowDate)-1].member_id
    print('startNum-' + str(startNum) + '-' + str(len(rowDate)) + '-' + str(currentMaxMemberId))

    # 将对象集合作为数据输入
    batch = str(startNum)
    dataFrame = pandas.DataFrame(export_list)
    # 导出csv文件
    dataFrame.to_csv('e:/csv/'+batch+'.csv')
    # 页数自增
    startNum += 1

print('end')
