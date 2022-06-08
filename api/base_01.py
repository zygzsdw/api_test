from loguru import logger
from setting import BASE_URL, LOGIN_INFO
import requests
from cacheout import Cache

cache = Cache()


class Base:
    def get_url(self, path, params=None):
        if params:
            full_url = BASE_URL + path + params
            return full_url
        return BASE_URL + path

    def get(self, url):
        response = requests.get(url, headers=self.headers())
        try:
            result = response.json()
            logger.success('请求URL:{},返回结果:{}'.format(url, result))
            return result
        except Exception as e:
            logger.error('请求get方法异常，返回数据异常:{}'.format(result))

    def post(self, url, data):
        response = requests.post(url, json=data, headers=self.headers())
        try:
            result = response.json()
            logger.success('请求URL:{},返回参数:{},返回结果:{}'.format(url, data, result))
            return result
        except Exception as e:
            logger.error('请求post方法异常，返回数据异常:{}'.format(result))

    def headers(self):
        headers = {'Content-Type':'application/json'}
        token = cache.get('token')
        if token:
            headers.update('X-Litemall-Admin-Token', token)
            return headers
        return headers

    def login(self):
        login_path = '/admin/auth/login'
        login_url = base.get_url(login_path)
        result = self.post(login_url, LOGIN_INFO)
        try:
            if result.get('errno') == 0:
                logger.info('请求登录接口成功')
                token = result.get('data').get('token')
                cache.set('token', token)
            else:
                logger.error('登录失败:{}'.format(result))
                return None
        except Exception as e:
            logger.error('报错信息:{}'.format(e))
            logger.error('请求登录接口失败:{}'.format(result))


if __name__ == '__main__':
    base = Base()
    print(base.get_url('/admin/auth/login'))

    login_url = base.get_url('/admin/auth/login')
    print(base.post(login_url,LOGIN_INFO))

    base.login()
