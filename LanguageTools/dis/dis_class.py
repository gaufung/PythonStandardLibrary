import dis

class MyObject:
    """Example for dis"""
    CLASS_ATTRIBUTE = 'some value'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'MyObject({})'.format(self.name)


dis.dis(MyObject)