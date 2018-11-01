import socket
import threading, time

#服务端
#参考廖雪峰python教程-网络编程-TCP编程
#编程练习：了解python-TCP编程建立连接的过程
#2018-7-15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # 绑定监听端口
 # bind
 
s.bind(('127.0.0.1', 9999))

## 监听 listen(max_connect_counts)
s.listen(5)
print('Wating for connection...')

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % (sock, addr))
	sock.send(b'Welcome')
	while(True):
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

while(True):
	sock, addr = s.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()
	