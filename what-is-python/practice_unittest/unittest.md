# UnitTest

## 单元测试框架

[`unittest`](https://docs.python.org/zh-cn/3/library/unittest.html#module-unittest) 单元测试框架是受到 JUnit 的启发，与其他语言中的主流单元测试框架有着相似的风格。其支持测试自动化，配置共享和关机代码测试。支持将测试样例聚合到测试集中，并将测试与报告框架独立

为了实现这些，[`unittest`](https://docs.python.org/zh-cn/3/library/unittest.html#module-unittest) 通过面向对象的方式支持了一些重要的概念。

- ### 测试脚手架

  *test fixture* 表示为了开展一项或多项测试所需要进行的准备工作，以及所有相关的清理操作。举个例子，这可能包含创建临时或代理的数据库、目录，再或者启动一个服务器进程。

- ### 测试用例

  一个测试用例是一个独立的测试单元。它检查输入特定的数据时的响应。 [`unittest`](https://docs.python.org/zh-cn/3/library/unittest.html#module-unittest) 提供一个基类： [`TestCase`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase) ，用于新建测试用例。

- ### 测试套件

  *test suite* 是一系列的测试用例，或测试套件，或两者皆有。它用于归档需要一起执行的测试。

- ### 测试运行器（test runner）

  *test runner* 是一个用于执行和输出测试结果的组件。这个运行器可能使用图形接口、文本接口，或返回一个特定的值表示运行测试的结果。

## 基本实例

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```



pip install html-testRunner























