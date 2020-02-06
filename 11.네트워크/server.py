'''
1.소켓생성
2.바인딩
3.접속대기
4.접속수락
5.데이터통신
6.접속종료
'''

import socket
print('1.소켓생성')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('2.바인딩')
sock.bind(('', 1200))

print('3.접속대기')
sock.listen()

print('4.접속수락')
c_sock, addr = sock.accept()

print('5.데이터 송신/수신')
recieve_data = c_sock.recv(1024)
print('수신된 데이터:{}'.format(recieve_data))

print('6.접속종료')
c_sock.close()
sock.close()
