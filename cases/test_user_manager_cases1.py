# 主要实现用户管理中的测试用例
import unittest
from api.user_manager import UserManager
from loguru import logger
from data.user_manager_data import UserManagerData


class TestUserManager(unittest.TestCase):
    user_id = 0

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        # cls.user.login()
        cls.username = UserManagerData.add_user_data.get('username')
        cls.password = UserManagerData.add_user_data.get('password')
        cls.new_username = UserManagerData.add_user_data.get('new_username')
        cls.errno = UserManagerData.add_user_data.get('errno')

    # case1:添加管理员，只输入用户名和密码的情况
    def test01_add_user(self):
        # 1.初始化添加管理员的测试数据
        # 2.调用添加管理员的接口
        actual_result = self.user.add_user(self.username, self.password)
        data = actual_result.get('data')
        if data:
            TestUserManager.user_id = data.get('id')
            logger.info("获取添加用户id:{}".format(TestUserManager.user_id))
        # 3.断言
        self.assertEqual(self.errno, actual_result['errno'])
        self.assertEqual(self.username, actual_result.get('data').get('username'))

    # case1:编辑管理员：修改用户名称
    def test02_edit_username(self):
        actual_result = self.user.edit_user(TestUserManager.user_id, self.new_username, password='123456')
        self.assertEqual(self.errno, actual_result['errno'])
        self.assertEqual(self.new_username, actual_result.get('data').get('username'))

    # case1:查询用户列表
    def test03_search_user(self):
        actual_result = self.user.search_user()
        self.assertEqual(self.errno, actual_result['errno'])
        self.assertEqual(self.new_username, actual_result['data'].get('list')[0].get('username'))

    # case1:删除用户：删除指定id的用户名
    def test04_delete_user(self):
        actual_result = self.user.delete_user(TestUserManager.user_id, self.new_username)
        self.assertEqual(self.errno, actual_result['errno'])


if __name__ == '__main__':
    unittest.main()
