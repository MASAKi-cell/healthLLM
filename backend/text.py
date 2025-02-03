class MyClass:
    def __init__(self):
        self.name = "tanaka"
        self._name = "yamada"
        self.__name = "suzuki"

    def hello(self):
        print('hello')

    def _hello(self):
        print('hello')

    def __hello(self):
        print('hello')
