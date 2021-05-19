![](https://images.velog.io/images/hability24/post/60c0b2f9-e2c9-4f01-9810-74cd903eee22/image.png)

# Rookie-app
- 영화, 음악 추천은 많은데 **신인 아이돌 추천은 없을까?**
- KPOP fan을 위한 신인아이돌 추천 시스템

![](https://images.velog.io/images/hability24/post/bf57c953-3038-4ecd-92cd-f43bf88e9cb5/image.png)


- 자료수집에 Twitter API 활용
- 추천은 RandomForestClassifier 활용(아래 로직 설명 참고)

## 기능소개
![](https://images.velog.io/images/hability24/post/4590a901-7698-4168-88bb-28ca68fc268c/image.png)
- 유저 입력, 삭제
- 선호그룹 입력, 업데이트
- 신인 추천

## Logic & Schema
![](https://images.velog.io/images/hability24/post/bba4dcc0-d6bd-42f4-a164-7f6c2e35655d/image.png)

![](https://images.velog.io/images/hability24/post/a7083d62-d069-4972-abbf-78cf5602b53d/image.png)
- 트위터에서 그룹 이름 검색 시 나오는 실시간 트윗들을 활용
- 기존 그룹 중 선호 그룹을 조사 후
- 신인 그룹 트윗 검색 결과로 선호도 분석
![](https://images.velog.io/images/hability24/post/04c758a1-d18a-430f-96bf-bc771b8e617d/image.png)


### 바로가기 - https://rookie-app.herokuapp.com/


### 주의사항
* 아이디어 및 추천시스템의 도용을 금지합니다.
