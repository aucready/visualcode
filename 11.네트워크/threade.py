import time
import threading


def 주문받기():
    for i in range(5):
        print('주문받기:{}'.format(i))
        time.sleep(1)


def 우편발송():
    for i in range(5):
        print('우편발송:{}'.format(i))
        time.sleep(.5)

t1 = threading.Thread(target=주문받기)
t2 = threading.Thread(target=우편발송)


t1.start()
t2.start()

t1.daemon = True
t2.daemon = True

