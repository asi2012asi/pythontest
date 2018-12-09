# coding=utf8
'第一次使用单元测试 测试python'
# author=luyaoming
import unittest

from zygote import TestName as target


class TestTestName1(unittest.TestCase):

    def test_lib_func(self):
        self.assertEqual(target.lib_func(10), 20)

    def test_lib_func_other(self):
        self.assertEqual(target.lib_func_another(10), 30)

    def test_doc(self):
        print(__doc__, " see doc")

    def setUp(self):
        print('setup...')

    def tearDown(self):
        print('teardown...')

    if __name__ == '__main__':
        unittest.main()
