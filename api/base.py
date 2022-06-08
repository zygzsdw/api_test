"""
 作用：主要用于所有接口的公共功能，使用一个基类（父类）
 功能1：处理url
 功能2：重新封装get方法和post方法
 功能3：处理头信息
 功能4:登录

"""

from setting import BASE_URL, LOGIN_INFO
import requests
from loguru import logger
from cacheout import Cache

cache = Cache()


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
    def get(self, url):
        result = None
        response = requests.get(url, headers=self.get_headers())
        try:
            result = response.json()
            logger.success('请求URL:{},返回结果:{}'.format(url, result))
            return result
        except Exception as e:
            logger.error('请求get方法异常，返回数据为{}'.format(result))

    # 重写post方法
    def post(self, url, data):
        result = None
        response = requests.post(url, json=data, headers=self.get_headers())
        try:
            result = response.json()
            logger.success('请求URL:{},请求参数{},返回结果:{}'.format(url, data, result))
            return result
        except Exception as e:
            logger.error('请求post方法异常，返回数据为{}'.format(result))

    # 实现所有头部信息的处理
    def get_headers(self):
        """
        处理请求头
        :return:返回的是字典格式的请求头，多是包括了Content-Type ,X-Litemall-Admin-Token
        """
        headers = {'Content-Type': 'application/json'}
        token = cache.get('token')  # 从缓存中获取token值
        if token:
            headers.update({'X-Litemall-Admin-Token': token})
            return headers
        return headers

    # 实现登录功能
    def login(self):
        """
        通过调用登录接口获取token值将其缓存，其它接口使用时直接从缓存中取，若没有缓存，再调用登录，
        再将token放在缓存中
        :return:
        """
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        result = self.post(login_url, LOGIN_INFO)
        try:
            if result.get('errno') == 0:
                logger.info('请求登录接口成功')
                token = result.get('data').get('token')
                cache.set('token', token)
                logger.info(cache.get('token'))
            else:
                logger.error('登录失败:{}'.format(result))
                return None
        except Exception as e:
            logger.error('报错信息:{}'.format(e))
            logger.error('请求登录接口异常，异常数据:{}'.format(result))


if __name__ == '__main__':
    pass
    # base = Base()
    # print(base.get_url('/admin/auth/login'))
    # login_url = base.get_url('/admin/auth/login')
    # login_data = {"username": "admin123", "password": "admin123"}
    # print(base.post(login_url, login_data))
