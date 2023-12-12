# 기본 이미지로부터 시작
FROM node:latest

# 작업 디렉토리 설정
WORKDIR /app

# 앱 의존성 설치
COPY package*.json ./
RUN npm install

# 앱 소스 추가
COPY . .

# 포트 열기
EXPOSE 8008

# 앱 실행
CMD [ "node", "app.js" ]
