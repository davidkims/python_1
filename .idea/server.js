// 필요한 모듈 불러오기
const http = require('http');
const fs = require('fs');
const path = require('path');

// 서버를 생성합니다.
const server = http.createServer((req, res) => {
    // 요청이 들어왔을 때의 처리 로직

    // URL 경로를 가져옵니다.
    const url = req.url === '/' ? '/index.html' : req.url;

    // 파일의 경로를 만듭니다.
    const filePath = path.join(__dirname, 'public', url);

    // 파일이 있는지 확인합니다.
    fs.access(filePath, fs.constants.F_OK, (err) => {
        if (err) {
            // 파일이 없을 경우 404 에러를 보냅니다.
            res.writeHead(404, { 'Content-Type': 'text/html' });
            res.end('<h1>404 Not Found</h1>');
        } else {
            // 파일이 있을 경우 해당 파일을 읽어서 응답합니다.
            fs.readFile(filePath, 'utf8', (err, data) => {
                if (err) {
                    // 파일 읽기 실패 시 500 에러를 보냅니다.
                    res.writeHead(500, { 'Content-Type': 'text/html' });
                    res.end('<h1>500 Internal Server Error</h1>');
                } else {
                    // 파일 읽기 성공 시 정상적으로 응답합니다.
                    res.writeHead(200, { 'Content-Type': 'text/html' });
                    res.end(data);
                }
            });
        }
    });
});

// 서버를 특정 포트로 listen 시킵니다.
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});