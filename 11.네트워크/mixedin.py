class carMixin:
    def ready(self):
        print('믹스인 레디')

    def start(self):
        print('{}가 {} 속도로 달리고 있습니다.'.format(self.name, self.speed)




class Performance():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed



