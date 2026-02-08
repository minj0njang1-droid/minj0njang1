# 매일주식 - AI 추천 종목

![매일주식](https://img.shields.io/badge/%EB%A7%A4%EC%9D%BC%EC%A3%BC%EC%8B%9D-AI%20%EC%B6%94%EC%B2%9C-blue)
![Version](https://img.shields.io/badge/version-4.2-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## 📈 프로젝트 소개

매일 오전 8시, AI가 분석한 추천 종목을 제공하는 웹사이트입니다.

### ✨ 주요 기능

- 🛡️ **안정형 TOP 10** - 배당주, 대형주 중심
- ⚔️ **공격형 TOP 10** - 성장주, 테마주 중심
- 📰 **오늘의 핵심 뉴스** - 증권사 의견 포함
- 📊 **시장 현황** - 코스피/코스닥/환율/금
- ⏰ **매일 오전 8시 자동 업데이트**

### 🎨 디자인 특징

- 친근하고 깔끔한 금융 앱 스타일
- 모바일 최적화 (반응형 디자인)
- 차분한 색상 (신뢰감 UP)
- 클릭 시 상세 이유 펼침

### 💰 수익화

- Google AdSense 광고 3개 배치
- 증권사 제휴 광고 가능

## 🚀 배포 방법

### Vercel 배포

```bash
# 1. Vercel CLI 설치
npm install -g vercel

# 2. 배포
vercel deploy

# 3. 프로덕션 배포
vercel --prod
```

### GitHub Pages 배포

```bash
# index.html을 main 브랜치에 푸시
git add .
git commit -m "Initial commit"
git push origin main
```

## 📁 프로젝트 구조

```
daily-stock/
├── index.html          # 메인 웹페이지
├── vercel.json         # Vercel 설정
└── README.md           # 프로젝트 문서
```

## 🔧 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Hosting**: Vercel / Netlify
- **Analytics**: Google Analytics (선택)

## 📝 향후 계획

- [ ] 백엔드 자동화 (Node.js + Python)
- [ ] 실시간 주가 API 연동
- [ ] 뉴스 크롤링 자동화
- [ ] 이메일 발송 시스템
- [ ] 회원 가입/로그인
- [ ] 관심 종목 저장

## 📄 라이선스

MIT License

## 👨‍💻 제작자

매일주식 팀

---

**⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!**
