// 필요한 모듈 가져오기
const express = require('express');
const path = require('path');
const mongoose = require('mongoose');
const session = require('express-session');
const FileStore = require('session-file-store')(session);

// 라우트를 처리하는 라우터 모듈 가져오기
const apiRouter = require('./routes/routing.js');

// Express 애플리케이션 생성
const app = express();

// MongoDB에 연결
mongoose.connect("mongodb+srv://root:1234@atlascluster.uphk0xv.mongodb.net/?retryWrites=true&w=majority", { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB에 성공적으로 연결되었습니다'))
  .catch(e => console.error(e));

// 뷰 디렉터리와 뷰 엔진 설정
app.set('views', path.resolve(__dirname + '/views'));
app.set('view engine', 'ejs');

// public 디렉터리에서 정적 파일 제공
app.use(express.static(path.join(__dirname, 'public')));


// 폼 데이터 처리를 위한 바디 파서 활성화
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// 세션 미들웨어 설정
app.use(session({
  secret: "asdfasffdas",
  resave: false,
  saveUninitialized: true,
  store: new FileStore()
}));

// 라우터를 사용하여 라우트 처리
app.use('/', apiRouter);

// 서버 시작
const port = process.env.PORT || 8008;
app.listen(port, () => {
  console.log(`서버가 http://localhost:${port}에서 실행 중입니다`);
});
