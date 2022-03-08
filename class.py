class MyClass:
    """一個簡單例子"""
    i = 12345

    def f(self):
        return "hello world!"


x = MyClass()
print("MyClass 类的属性 i 为：{0}".format(x.i))
print("MyClass 类的方法 f 输出为：{0}".format(x.f()))


class Complex:
    """Class 定义了 __init__() 方法，Class的实例化操作会自动调用 __init__() 方法。"""
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart

    def prt(self):
        print(self)  #class 地址
        print(self.__class__)  #顯示class名稱


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5
x.prt()


class People:
    #定義基本屬性
    name = ''
    age = 0
    __weight = 0  #定义私有属性,私有属性在类外部无法直接进行访问

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("{0} 说: 我 {1} 岁。".format(self.name, self.age))


p = People('runoob', 10, 30)
p.speak()


#-- 繼承
class Student:
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)  #调用父类的构函
        self.grade = g

    #覆写父类的方法
    def speak(self):
        print("{0} 说: 我 {1} 岁，我在读 {2} 年级".format(self.name, self.age,
                                                 self.grade))


#另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


#多重继承
class Sample(Speaker, Student):
    a = ''
    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, 'Python')
test.speak() ##方法名同，默认调用的是在括号中排前class的方法


#调用父类方法
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')

c = Child()
super(Child, c).myMethod()


#类的私有方法
class Site:
    age = 18
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print('Name:{0}; Url:{1}; Age:{2}'.format(self.name, self.__url, self.age))
    def __foo(self):
        print("这是私有方法")
    def foo(self):
        print('这是公共方法')
        self.__foo()
x = Site("fuck", "you")
x.who() #Name:fuck; Url:you; Age:18
x.foo()

#运算符重载
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)