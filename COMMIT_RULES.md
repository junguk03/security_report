# 커밋 메시지 규칙

이 저장소에서 커밋 메시지를 쓸 때 따르는 규칙이다.

## 형식

```
<Type>(<scope>): <Description>

<본문>
```

- `Type`: 커밋 종류. 첫 글자는 대문자로 쓴다.
- `scope`: 바뀐 범위. 필요할 때만 쓴다. 예: `portswigger`, `wargame`, `nday`
- `Description`: 무엇을 하는 커밋인지 영어 명령형으로 짧게 쓴다.

## 제목

- 50자를 넘기지 않는다.
- 첫 글자는 대문자로 쓴다.
- 끝에 마침표를 찍지 않는다.
- 명령형으로 쓴다. `Add lab notes` (O), `Added lab notes` (X)

## 본문

- 제목 아래 한 줄을 비우고 쓴다.
- 한 줄이 72자를 넘으면 줄을 바꾼다.
- 어떻게 바꿨는지보다 무엇을, 왜 바꿨는지 쓴다.
- Claude 출처 표기(`Co-Authored-By: Claude`, `Generated with Claude Code` 등)는 넣지 않는다.

## Type

| Type | 쓰는 경우 |
|---|---|
| Feat | 새 기능이나 새 코드 추가 (익스플로잇, PoC, 퍼저 등) |
| Fix | 잘못된 내용이나 코드 수정 |
| Docs | 기록, 블로그 초안, README 같은 문서 추가·수정 |
| Style | 내용은 그대로 두고 서식만 정리 |
| Refactor | 동작은 그대로 두고 코드 구조만 개선 |
| Test | 테스트 코드 추가·수정 |
| Chore | 폴더 구조, 설정, 환경 관련 변경 |

## 예시

```
Docs(portswigger): Add SQLi UNION lab notes

Record the approach and the stuck points from the UNION
column-count lab so the study log stays complete.
```

참고: [Conventional Commits](https://www.conventionalcommits.org/)
