"""
 作用：主要用于所有接口的公共功能，使用一个基类（父类）
 功能1：处理url
 功能2：重新封装get方法和post方法
 功能3：处理头信息
 功能4:登录

"""

from setting import BASE_URL


class Base:
    # 处理url，实现url拼接
    def get_url(self, path, params=None):
        """

        :return:返回的一个完整的url
        """
        if params:
            full_url = BASE_URL + path + params
            return full_url
        return BASE_URL + path

    # 重写get方法：
    def get(self):
        pass

    # 重写post方法
    def post(self):
        pass

    # 实现所有头部信息的处理
    def get_headers(self):
        pass

    # 实现登录功能
    def login(self):
        pass


if __name__ == '__main__':
    base = Base()
    print(base.get_url('/admin/auth/login'))
    print(base.get_url('/admin/admin/list','?page=1&limit=20&sort=add_time&order=desc'))
