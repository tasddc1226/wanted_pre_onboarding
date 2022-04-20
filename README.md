## 프리온보딩 - Backend 과정 선발과제

### 😎 서비스 개요
- 크라우드 펀딩을 받기 위한 상품을 등록한다.
- 펀딩하기를 클릭하면 '1회 펀딩 금액'만큼 펀딩한다.

### 🚧 요구사항 구현 목록
- [x] 상품 등록하기


- [x] 상품 수정하기
  - '목표 금액' 수정 못하게 하기

- [x] 상품 삭제하기

- [x] 상품 목록 가져오기
  - 제목, 게시자, 총 펀딩 금액, 달성률, D-Day 포함
  - 상품 검색 기능 구현 : 제목을 포함한 상품을 검색하도록
  - 상품 정렬 기능 구현 : 생성일, 총 펀딩 금액을 기준으로 정렬하도록

- [x] 상품 상세 페이지 구현하기
  - 제목, 게시자, 총 펀딩 금액, 달성률, D-Day, 설명, 목표 금액 및 참가자 수 포함

### 사용 기술 스택
<img src="https://img.shields.io/badge/python-007396?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-6DB33F?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/postgresql-4479A1?style=for-the-badge&logo=postgresql&logoColor=white">

### API 응답 테스트 화면
- 모든 상품 목록 GET 요청 : `http://127.0.0.1:8000/product/`

![Screen Shot 2022-04-20 at 2 32 44 PM](https://user-images.githubusercontent.com/55699007/164157305-6a73b7a6-7daf-45a8-a575-c5f7d67cd146.png)


- 상품 등록 POST 요청 : `http://127.0.0.1:8000/product/`

![Screen Shot 2022-04-20 at 2 34 19 PM](https://user-images.githubusercontent.com/55699007/164157473-6e3e425a-6e1a-4acf-8a5d-24c556de647b.png)

![Screen Shot 2022-04-20 at 2 35 32 PM](https://user-images.githubusercontent.com/55699007/164157630-f06842f8-ef17-4993-8103-7323ad95e454.png)

- 특정 상품 GET 요청 : `http://127.0.0.1:8000/product/12`

![Screen Shot 2022-04-20 at 2 36 44 PM](https://user-images.githubusercontent.com/55699007/164157769-6b77b16d-564b-40ca-8e32-ec1ab55d2c04.png)

- 상품 수정 : 처음 만든 target_price는 제외하고 수정하도록 함.

![Screen Shot 2022-04-20 at 2 37 59 PM](https://user-images.githubusercontent.com/55699007/164157924-60c701ad-3c42-4bbd-8db1-31f786750b8b.png)

![Screen Shot 2022-04-20 at 2 38 19 PM](https://user-images.githubusercontent.com/55699007/164157973-5ae12255-529f-48e7-8880-475611bb25a2.png)

- 상품 DELETE 요청 : `http://127.0.0.1:8000/product/12`

![Screen Shot 2022-04-20 at 2 40 24 PM](https://user-images.githubusercontent.com/55699007/164158237-2eae0013-f059-4a15-ae65-68e574b630e1.png)


- 검색 요청 : `http://127.0.0.1:8000/product/?search=test`

![Screen Shot 2022-04-20 at 2 41 39 PM](https://user-images.githubusercontent.com/55699007/164158402-ca808f60-26ca-44c9-b79a-5f3f89cb3359.png)

- 정렬 요청

  - `GET /product/?ordering=created_at` : 상품 생성일 기준 오름차순 정렬
  - `GET /product/?ordering=-created_at` : 상품 생성일 기준 내림차순 정렬
  - `GET /product/?ordering=total_cost` : 총 펀딩 금액 기준 오름차순 정렬
  - `GET /product/?ordering=-total_cost` : 총 펀딩 금액 기준 오름차순 정렬

- 상품 펀딩 PUT 요청 : `http://localhost:8000/product/11/funding`

  - 요청 전
  - ![Screen Shot 2022-04-20 at 2 48 42 PM](https://user-images.githubusercontent.com/55699007/164159245-4c8555ac-b296-4b5a-91f9-67238d042c54.png)

  - 요청 후 : 총 펀딩 금액, 달성률, 참여자 수 변경
  - ![Screen Shot 2022-04-20 at 2 50 32 PM](https://user-images.githubusercontent.com/55699007/164159512-7490532b-8ef6-4753-bf88-9fa83da6b0c3.png)





