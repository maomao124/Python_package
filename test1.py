"""
 * Project name(项目名称)：Python封装
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 12:28
 * Version(版本): 1.0
 * Description(描述)： 
 """


class C:
    def setname(self, name):
        if len(name) < 3:
            raise ValueError('名称长度必须大于3！')
        self.__name = name

    def getname(self):
        return self.__name

    # 为 name 配置 setter 和 getter 方法
    name = property(getname, setname)

    def setsex(self, sex):
        if sex == '男' or sex == '女':
            self.__sex = sex
        else:
            raise ValueError('性别只能为男或者女！')

    def getsex(self):
        return self.__sex

    # 为 sex 配置 setter 和 getter 方法
    sex = property(getsex, setsex)

    def setage(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError('年龄必须大于0！')

    def getage(self):
        return self.__age

    # 为 age 配置 setter 和 getter 方法
    age = property(getage, setage)

    # 定义个私有方法
    def __f(self):
        print("私有方法")

    def display(self):
        print(self.__name, self.__sex, self.__age)


if __name__ == '__main__':
    c = C()
    # c.name="1"
    c.name = "-张三-"
    # c.sex="1"
    c.sex = "男"
    # c.age=-2
    c.age = 21
    print(c.name)
    print(c.sex)
    print(c.age)
    c.display()
    c.sex = "女"
    c.age = 19
    print(c.name)
    print(c.sex)
    print(c.age)
    c.display()

    # 使用私有方法和属性
    print(c._C__name)
    print(c._C__sex)
    print(c._C__age)
    c._C__age = 18
    print(c._C__age)
    c._C__f()
