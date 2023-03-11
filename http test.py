import socket

HOST, PORT = '', 8080

# 소켓 생성 및 바인딩
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print(f'Serving HTTP on port {PORT} ...')

while True:
    # 클라이언트 요청 대기
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)

    # 요청한 파일 찾기
    filename = request.split()[1]
    if filename == '/':
        filename = '/index.html'
    try:
        with open(f'.{filename}', 'rb') as f:
            content = f.read()
            response = b'HTTP/1.1 200 OK\n\n' + content
    except FileNotFoundError:
        response = b'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

    # 클라이언트에게 응답 전송
    client_connection.sendall(response)
    client_connection.close()
