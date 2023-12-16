const express = require('express');
const User = require('../utils/userModel.js');
const List = require('../utils/listModel.js');
const Question = require('../utils/questionMdel.js');
const router = express.Router();
const ObjectId = require('mongoose').Types.ObjectId;

// 미들웨어: 사용자가 로그인했는지 확인
const isLoggedIn = async (req, res, next) => {
  if (req.session['username']) {
    next();
  } else {
    res.status(301).redirect('/login');
  }
};

// 미들웨어: 사용자가 로그인하지 않았는지 확인
const isNotLoggedIn = (req, res, next) => {
  if (req.session['username']) {
    res.status(403).redirect('/');
  } else {
    next();
    
  }
};

// 라우트
router.get('/', (req, res) => res.render('index', { name: req.session['username'] }));
router.get('/index', (req, res) => res.render('index', { name: req.session['username'] }));
router.get('/board', (req, res) => res.render('board', { name: req.session['username'] }));
router.get('/enjoy', (req, res) => res.render('enjoy', { name: req.session['username'] }));

// 공지사항 게시판
router.get('/noticeboard', async (req, res, next) => {
  let articles = await List.find();
  res.render('noticeboard', { articles: articles, name: req.session['username'] });
});

// 게시글 작성 페이지
router.get('/create', isLoggedIn, (req, res, next) => {
  res.render('create', { name: req.session['username'] });
});

// 게시글 작성 처리
router.post('/create', isLoggedIn, async (req, res, next) => {
  const { title, author, desc } = req.body;

  const newList = new List({
    title: title,
    author: author,
    desc: desc
  });

  try {
    await newList.save();
    res.redirect('/noticeboard');
  } catch (error) {
    console.error(error);
    res.redirect('/create');
  }
});

// 게시글 삭제
router.get('/delete/:id', async (req, res) => {
  await List.deleteOne({ _id: new ObjectId(req.params.id) });
  res.redirect('/noticeboard');
});
// 회원가입 페이지
router.get('/register', isNotLoggedIn, (req, res) => res.render('register', { user: 'guest', name: req.session['username'] }));

// 로그인 페이지
router.get('/login', isNotLoggedIn, (req, res) => res.render('login', { user: 'guest', name: req.session['username'] }));

// 회원가입 처리
router.post('/register', async (req, res) => {
  const { name, email, phone, password } = req.body;

  const existingUser = await User.findOne({ email: email });

  if (existingUser) {
    return res.render('login', { user: 'exist', name: req.session["username"] });
  }

  const newUser = new User({
    username: name,
    email: email,
    phone: phone,
    password: password,
  });

  try {
    await newUser.save();
    // 회원가입 성공 시 로그인 페이지로 리다이렉션
    res.redirect('/login');
  } catch (error) {
    console.error(error);
    res.redirect('/');
  }
});
// 로그인 처리
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email: email });

  if (!user || password !== user.password) {
    return res.render('login', { user: 'null', name: req.session["username"] });
  }

  req.session["username"] = user.username;
  res.render('index', { name: req.session["username"] });
});

// 로그아웃 처리
router.get('/logout', isLoggedIn, (req, res) => {
  req.session.destroy(() => {});
  res.redirect('/');
});

// 게시글 목록
router.get('/list', async (req, res) => {
  const articles = await List.find();
  res.render('list', { articles: articles, name: req.session['username'] });
});

// 1:1 문의 페이지
router.get('/question', (req, res) => res.render('question', { name: req.session['username'] }));

// 1:1 문의 처리
router.post('/question', async (req, res) => {
  const { name, email, message } = req.body;

  const newQuestion = new Question({
    name: name,
    email: email,
    message: message,
  });

  try {
    await newQuestion.save();
    console.log(`1:1 문의가 제출되었습니다.`);
    res.render('index', { name: req.session['username'], alertMessage: '1:1 문의가 제출되었습니다.' });
  } catch (error) {
    console.error(error);
    res.render('question', { name: req.session['username'], alertMessage: '문의 제출에 실패하였습니다.' });
  }
});

module.exports = router;
