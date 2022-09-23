# 1) Base class: 일반적인 클래스처럼 쓸 수 있어 범용적
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"): # 클래스 객체에 _instance 속성이 있는지 확인
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)

        if not hasattr(cls, "_init"):
            cls._init = True


s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # True

# 2) metaclass 사용하는 방식
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


a = MyClass()
b = MyClass()

print(a is b) # True

