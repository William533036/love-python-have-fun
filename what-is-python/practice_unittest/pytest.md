# 1.pytest单元测试框架

## (1)什么是单元测试

针对程序的最小单位(函数、方法)进行测试。这个 `pytest` 框架使编写小测试变得容易，但是可以扩展到支持应用程序和库的复杂功能测试。

常见单元测试框架：

python: unittest、[pytest](https://www.osgeo.cn/pytest/index.html#)

GO: testify + gomonkey 附加：httptest + sqlmock

java: Junit、testing

## (2)[为什么要做单元测试](https://www.zhihu.com/question/28729261)

- 便于后期重构。单元测试可以为代码的重构提供保障，只要重构代码之后单元测试全部运行通过，那么在很大程度上表示这次重构没有引入新的BUG，当然这是建立在完整、有效的单元测试覆盖率的基础上。
- 优化设计。编写单元测试将使用户从调用者的角度观察、思考，特别是使用TDD驱动开发的开发方式，会让使用者把程序设计成易于调用和可测试，并且解除软件中的耦合。
- 文档记录。单元测试就是一种无价的文档，它是展示函数或类如何使用的最佳文档，这份文档是可编译、可运行的、并且它保持最新，永远与代码同步。
- 具有回归性。自动化的单元测试避免了代码出现回归，编写完成之后，可以随时随地地快速运行测试，而不是将代码部署到设备之后，然后再手动地覆盖各种执行路径，这样的行为效率低下，浪费时间。

## (3)[如何去做单元测试](https://mp.weixin.qq.com/s?__biz=MzA5MTAzNjU1OQ==&mid=2454779818&idx=1&sn=0c91a9b637a7a7ecf1c2d30e94d521b1&chksm=87a6d94ab0d1505c90c8f3f495402aa76f50fe42df3c4660e775670be8833c10c377956cccae&mpshare=1&scene=21&srcid=&rd2werd=1#wechat_redirect)

单元测试的代码结构⼀般一个三步经典结构：准备，调⽤，断⾔。

1. 准备部分的⽬的是准备好调⽤所需要的外部环境，如数据，Stub，Mock，临时变量，调⽤请求，环境背景变量等等。
2. 调⽤部分则是实际调⽤需要测试⽅法，函数或者流程。
3. 断⾔部分判断调⽤部分的返回结果是否符合预期。

每个单元测试都应该能清晰地分出这三部分，当然有时调⽤断⾔两部分合在⼀起也是⽐较常见 的

## (4)单元测试框架主要做什么

1.测试发现：从多个文件里去找到我们的测试用例

2.测试执行：安装一定的顺序和规则去执行，并生成结果

3.测试判断：通过断言判断预期结果和实际结果的差异

4.测试报告：统计测试进度，耗时，通过率，生成测试报告

# 2.单元测试框架和自动化测试框架有什么关系

## （1）什么是自动化测试框架

## （2）作用

1.提高测试效率，降低维护成本

2.减少人工干预，提高测试的准确性，增加代码的重用性

3.核心思想是让不懂代码的人也能通过这个框架去实现自动化测试

## （3）pytest单元测试框架和自动化框架的关系

单元测试框架：只是自动化测试框架中的组成部分之一

pom设计模式：只是自动化测试框架中的组成部分之一

数据驱动

关键字驱动

全局配置文件的封装

日志监控

selenium、requests二次封装

断言

报告邮件.....

# 3.pytest简介

1.pytest是一个非常成熟的python单元测试框架，比unittest更灵活更容易上手

2.pytest可以和selenium，requests，appnium结合实现web自动化、接口自动化、app自动化

3.pytest可以实现测试用例的跳过以及reruns失败用例重试

4.pytest可以和allure生成非常美观的测试报告

5.pytest可以和Jenkins持续集成

6.pytest有很多非常强大的插件，并且这些插件能够实现很多实用的操作

​	pytest

​	pytest-html

​	pytest-xdist  测试用例分布式执行或并发

​	pytest-ordering 用于改变测试用例的执行顺序

​	pytest-rerunfailures 用例失败后重跑

​	allure-pytest 用于生成美观的测试报告

​	pip install -r requirements.txt

# 4.使用pytest，默认的测试用例的规则

1.模块名必须以test_ 开头或者 _test结尾

2.测试类必须以Test开头，并且不能有init方法

3.测试方法必须以test开头

# 5.pytest测试用例的运行方式

1.主函数模式

2.命令行模式

（1）运行所有：pytest

（2）指定模块：pytest -vs test_demo.py

（3）指定目录：pytest -vs ./demo

（4）指定方法：pytest -vs ./demo/test_demo.py::test_fun

常用参数：

-s:输出调试信息，包括print打印的信息

-v：显示更加详细的信息

-vs：两个参数一起用

-m：mark,对应配置文件的markers里的参数

-n：支持多线程或者分布式运行测试用例

--reruns number：识别重跑

-x：表示只要一个用例报错，那么测试停止

-k:根据测试用例名称的部分字符串指定用例

--html 生成html测试报告

pytest -vs -m "test" **--html=./demo.html**

3.通过读取pytest.ini配置文件运行

```ini
[pytest]
addopts = -vs
testpath = ./
python_files = code*.py
python_classes = Test*
python_functions = test
markers =
   test:我的测试
```



# 6.pytest执行测试用例的顺序

unittest:ascii 的大小来绝对的执行的顺序

pytest：默认从上到下

改变默认的执行顺序：使用mark标记

@pytest.mark.run(order=3)

# 7.如何分组执行

pytest -m "test" 

pytest -m "test"  or -m "test1"

# 8.pytest跳过测试用例

（1）无条件跳过

```python
@pytest.mark.skip("无条件跳过")
```

（1）有条件跳过

```python
@pytest.mark.skipif(age>18, reason="已成年，满足条件")
```



# 9.pytest框架实现一些前置、后置(固件、夹具)的处理，常用的三种

## 1、setup/teardown, setup_class/teardown_class

setup/teardown 在每个测试用例前后运行

setup_class/teardown_class 在每个测试类执行前后运行

```python
import pytest

class TestDemo:
    age=18
    def setup(self):
        print("我执行在前面哦")

    def teardown(self):
        print("最后面是我执行哦")

    # @pytest.mark.skip("无条件跳过")
    def test_01_demo(self):
        print("hello world!")

    @pytest.mark.skipif(age>18, reason="已成年，满足条件")
    @pytest.mark.test
    def test_02_demo(self):
        print("hello 222!")

if __name__ == '__main__':
    pytest.main(['-v', '--html=./demo.html'])
```

## 2.使用@pytest.fixture()装饰器来实现部分用例的前后置

```python
import pytest

@pytest.fixture(scope="function",
                params=['成龙', '甄子丹', '菜10'],
                ids=['c1', 'zzd', 'c10'])
def demo_fixture(request):
    print("我执行在前面哦")
    yield request.param
    print("最后面是我执行哦")
class TestDemo:
    age=18

    def test_01_demo(self, demo_fixture):
        print("hello world!")
        print(str(demo_fixture))

    @pytest.mark.skipif(age>18, reason="已成年，满足条件")
    @pytest.mark.test
    def test_02_demo(self):
        print("hello 222!")

if __name__ == '__main__':
    pytest.main(['-v'])
	#最后运行了4次
```

```python
fixture(callable_or_scope=None, *args, scope="function", params=None, autouse=False, ids=None, name=None):
```

（1）scope 表示 @pytest.fixture标记的作用范围

（2）params参数化（支持 列表[]，元组（），字段列表[{{},{}],字典元组（{}，{}））

 request.param为固定写法

（3）ids：使用params时，给每个变量设置对应的别名

（4）name：别名，当取了别名后原来的名字用不了

（5）autouse：自动使用，默认为False

## 3.通过conftest.py和 @pytest.fixture结合使用实现全局的前后置应用

比如:项目的全局登录，模块的全局处理

1.conftest.py文件是单独存放的一个夹具配置文件，全名不能修改

2.用处可以在不同的py文件中使用同一个fixture函数

3.conftest.py需要和运行的用例放到同一层，并且不需要做任何import导入操作

fixture的顺序和使用时参数位置相同



## 小结：

setup/teardown, setup_class/teardown_class 是作用于所有用例或者所有类

 @pytest.fixture既可以是部分也可以是全部前后置

conftest.py和 @pytest.fixture结合使用实现全局的前后置应用

# 10.断言

assert

# 11.pytest结合allure-pytest插件生成allure测试报告

1.下载，解压，配置path

https://github.com/allure-framework/allure2/releases

2.path路径为bin

验证 allure --version

pycharm重启后可以使用

3.生成allure测试报告

```
os.system('allure generate ./temp -o ./report --clean')
```

allure generate 命令格式

 ./temp	临时的json格式报告路径

 -o ./report 		输出生成的allure报告路径

--clean	清空目录下原来的报告(指定当前目录会删除当前的代码)











