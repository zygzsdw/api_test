# 用于用户的增加，删除，修改，查询
from loguru import logger
from api.base import Base


class UserManager(Base):
    def __init__(self):
        self.add_user_url = self.get_url('/admin/admin/create')
        self.edit_user_url = self.get_url('/admin/admin/update')
        self.search_user_url = self.get_url('/admin/admin/list?page=1&limit=20&sort=add_time&order=desc')
        self.delete_user_url = self.get_url('/admin/admin/delete')

    # 新增管理员
    def add_user(self, username, password, **kwargs):
        """

        :param username:
        :param password:
        :param kwargs:
        :return: 添加管理员的接口返回的是json数据
        """
        user_data = {"username": username, "password": password}
        if kwargs:
            logger.info("添加管理员的可变参数:{}", **kwargs)
            user_data.update(**kwargs)
        return self.post(self.add_user_url, user_data)

    # 查询管理员
    def search_user(self):
        return self.get(self.search_user_url)

    # 修改管理员
    def edit_user(self, id, username, password, **kwargs):
        user_data = {"id": id, "username": username, "password": password}
        if kwargs:
            logger.info("修改管理员的可变参数:{}", **kwargs)
            user_data.update(**kwargs)
        return self.post(self.edit_user_url, user_data)

    # 删除管理员
    def delete_user(self, id, username, **kwargs):
        user_data = {"id": id, "username": username}
        if kwargs:
            logger.info("删除管理员的可变参数:{}", **kwargs)
            user_data.update(**kwargs)
        return self.post(self.delete_user_url, user_data)


