# 11-3 雇员：
# 编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
# 编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
# 为Employee编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和test_give_custom_raise()。
# 使用方法setUp()，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。

import unittest

class Employe():
    def __init__(self,first_name,last_name,raise_money):
        self.first_name=first_name
        self.last_name=last_name
        self.raise_money=raise_money
    def give_raise(self,money=5000):
        self.raise_money+=money

class TestEmploye(unittest.TestCase):
    def setUp(self):
        employe=Employe('Beckham','David',50000)
        self.default_raise=employe.raise_money
        employe.give_raise(10000)
        self.give_custom_raise=employe.raise_money
    def test_give_default_raise(self):
        self.assertEqual(self.default_raise,50000)
    def test_give_custom_raise(self):
        self.assertEqual(self.give_custom_raise,60000)
