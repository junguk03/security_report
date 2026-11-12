# PROGRESS

## 현재 단계
PortSwigger SQL injection — SQL injection UNION attack, finding a column containing text 진행 예정 (PortSwigger 집중)

## 다음 할 일
- SQLi 랩 체크리스트 진행 (남은 15개)
- Addition calculator 블로그 초안 남은 질문: 다음 글 제목, chr(39) 시도 결과 (blog/261112_wargame-addition-calculator.md 끝)
- Addition calculator 공개 전: 드림핵 워게임 풀이 외부 공개 허용 여부 확인 (공식 정책 못 찾음)
- n-day 재현 추천은 보류 (사용자가 PortSwigger 집중 중, 말하기 전까지 추천하지 않음)
- SQLi 끝나면 워게임 추천 받기

## SQL injection 체크리스트
([전체 랩 목록](https://portswigger.net/web-security/all-labs#sql-injection) 기준, 18개)

- [x] SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
- [x] SQL injection vulnerability allowing login bypass
- [ ] SQL injection attack, querying the database type and version on Oracle
- [ ] SQL injection attack, querying the database type and version on MySQL and Microsoft
- [ ] SQL injection attack, listing the database contents on non-Oracle databases
- [ ] SQL injection attack, listing the database contents on Oracle
- [x] SQL injection UNION attack, determining the number of columns returned by the query
- [ ] SQL injection UNION attack, finding a column containing text
- [ ] SQL injection UNION attack, retrieving data from other tables
- [ ] SQL injection UNION attack, retrieving multiple values in a single column
- [ ] Blind SQL injection with conditional responses
- [ ] Blind SQL injection with conditional errors
- [ ] Visible error-based SQL injection
- [ ] Blind SQL injection with time delays
- [ ] Blind SQL injection with time delays and information retrieval
- [ ] Blind SQL injection with out-of-band interaction
- [ ] Blind SQL injection with out-of-band data exfiltration
- [ ] SQL injection with filter bypass via XML encoding

## 기록
- 261111 저장소 세팅 (CLAUDE.md, PROGRESS.md, 폴더 구조, .gitignore). 이 시점까지 SQLi 랩 2개 완료, 기록 파일 없음
- 261111 SQL injection UNION attack, determining the number of columns 완료 (완료 체크만, 기록 파일 없음). README.md, COMMIT_RULES.md 추가
- 261112 GitHub 연결 확인 (origin/main), 드림핵 Addition calculator 시작
- 261112 UNION columns 랩 실제로 풀어서 solved 확인 (Burp Repeater로 `ORDER BY`, `UNION SELECT NULL` 요청, 스크린샷 2장). 기록 파일 없음
- 261112 드림핵 Addition calculator 해결 (플래그 획득). wargame/261112_dreamhack_addition-calculator.md, .py 작성. 블로그 초안은 규칙 파일 대기
- 261112 블로그 규칙서 받음 (blog/). CLAUDE.md에 개인 글 적용 방법, CTF·해커톤 예외, 앞으로 할 공부(자동화·CTF·시스템보안·리버싱·포너블·기사) 추가
- 261112 Addition calculator 블로그 초안 작성 blog/261112_wargame-addition-calculator.md, wargame 기록에 답변 반영
