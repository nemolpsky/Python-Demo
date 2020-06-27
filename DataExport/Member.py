# 数据库对象类
class Member(object):
    def __init__(self, member_id, address, member_name, mobile_no):
        self.member_id = member_id
        self.address = address
        self.member_name = member_name
        self.mobile_no = mobile_no

    # 打印对象所有属性
    def to_str(self):
        self.check_address()
        return str(self.member_id) + '|' + self.address + '|' + self.member_name + '|' + str(self.mobile_no)

    # 校验处理空地址
    def check_address(self):
        if self.address is None or self.address == '':
         self.address = 'no address'