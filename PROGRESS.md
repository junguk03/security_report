# PROGRESS

## 현재 단계
PortSwigger SQL injection — SQL injection UNION attack, finding a column containing text 진행 예정

## 다음 할 일
- SQLi 랩 체크리스트 진행 (남은 15개)
- 블로그 규칙 파일 받기 (블로그 초안 쓰기 전에 필요)
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
