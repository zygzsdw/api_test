import unittest
from HTMLTestRunner import HTMLTestRunner
from api.base import Base

test_report = 'test_report.html'

if __name__ == '__main__':
    base = Base()
    base.login()
    # 创建组件
    suite = unittest.TestLoader().discover('cases', pattern='test*.py')
    with open(test_report, 'wb') as f:
        runner = HTMLTestRunner(f, title='wshop测试报告', description=" 简化版的测试报告")
        runner.run(suite)
