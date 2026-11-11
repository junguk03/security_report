# security_report

웹 취약점 분석가를 목표로 공부하는 기록이다. PortSwigger Web Security Academy 랩 → 같은 유형의 워게임 → n-day 재현 순서로 진행한다.

## 진행 상황

마지막 갱신: 2026-11-12

| 순서 | 주제 | 진행 |
|---|---|---|
| 1 | PortSwigger SQL injection (Blind 포함) | 3 / 18 |
| 2 | PortSwigger Authentication (브루트포스 관련) | 시작 전 |
| 3 | PortSwigger OS command injection (Blind 포함) | 시작 전 |
| 4 | PortSwigger Access control | 시작 전 |

### SQL injection

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

### 워게임

- [ ] 드림핵 Addition calculator (진행 중)

### n-day 재현

아직 없음

## 폴더

| 폴더 | 내용 |
|---|---|
| `portswigger/` | PortSwigger 랩 기록 |
| `wargame/` | 워게임 풀이 기록과 익스플로잇 코드 |
| `nday/` | n-day 재현 (취약점별 폴더) |
| `blog/` | 블로그 초안 |
