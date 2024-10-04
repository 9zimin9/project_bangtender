# 🍸 방텐더 (project_bangtender)

방텐더 (project_bangtender)는 Django 와 Django REST Framework를 기반으로 **사용자 맞춤** 칵테일 추천 및 주류 정보를 제공하는 웹 애플리케이션(서비스@임시)입니다. 사용자 맞춤 칵테일, 양주 추천 기능과 주류 매장 찾기 등의 기능을 통해 칵테일을 좋아하는 사용자에게 유용한 정보를 제공합니다.

---

## 📚 목차

- [프로젝트 개요](#-프로젝트-개요)
- [팀 구성 및 역할분담](#-팀-구성-및-역할분담)
- [개발일정](#-개발일정)
- [주요 기능](#-주요-기능)
- [설치 방법](#-설치-방법)
- [와이어 프레임](#-와이어-프레임)
- [API 사용법](#-api-사용법)
- [ERD (Entity Relationship Diagram)](#️-erd-entity-relationship-diagram)
- [회원 기반 접근 제어](#️-회원-기반-접근-제어)
- [데이터베이스 관리](#️-데이터베이스-관리)
- [시스템 아키텍처](#-시스템-아키텍처)
- [개발 환경 및 사용 기술](#-개발-환경-및-사용-기술)
- [통합 및 인터페이스](#-통합-및-인터페이스)
- [보안](#-보안)

---

## 🔖 프로젝트 개요

### 🏞 프로젝트 개발 배경
코로나 이후로 회식이 적어진 국내 사회에서 20~30대 소비층에 국내의 주요 소비 주류인 소주나 맥주가 아닌 양주의 인기가 커지고 있다는 정보를 보게 되었고, 양주의 정보 제공과 다양한 칵테일 제조 방법을 추천 및 제공해 주는 플랫폼이 있으면 좋겠다고 생각하였습니다. 이와 같은 배경으로 사용자의 선호 취향을 토대로 칵테일 및 양주를 추천해 주는 OPENAI를 이용한 방텐더 봇, 지도 API를 통해 사용자 주변의 주류 매장을 보여주는 기능과 함께 주류나 칵테일에 대한 정보를 같이 제공할 수 있는 웹 사이트를 생각하게 되었습니다.

### 📈 프로젝트 기대 효과
서비스를 이용하는 유저가 주류나 칵테일에 대한 정보가 부족하더라고 쉽게 정보를 찾을 수 있으며, 자신의 기호에 맞는 주류와 칵테일을 방텐더 봇을 이용하여 추천받으며 잘 알지 못하는 주류에 대한 정보나 구매하기에 비싼 가격의 벽에 막혀 접하기 힘들었던 부분에 대해 다양한 정보를 제공하여 주류에 대해 쉽고 친근하게 접근할 수 있을 것입니다.
또한 어필리에이트 마케팅을 통해 제휴를 맺은 온라인 스토어로 연결되는 어필리에이트 링크를 제공하거나 주류 관련 브랜드들과 제휴를 맺어, 웹사이트에 배너 광고나 스폰서쉽을 유치하는 등의 서비스를 제공하고, 지역 주류 매장 검색 시 특정 매장을 상단에 노출하는 유료 광고나 지역 주류 매장에서의 주문 서비스를 제공해 수수료를 제공받아 수익화를 기대해 볼 수 있습니다.

---

## 🧑‍🤝‍🧑 팀 구성 및 역할분담
| **이름** | **기능**            | **날짜**                          |
|:------------:|--------------------------|----------------------------------|
| 김동민(팀장)     |회원 기능, 인증/보안, F.E  |          2024.9.23 ~ 10.23              | 
| 김진영(부팀장)     | AI(방텐더) 및 서브 콘텐츠, ERD 제작     |            2024.9.23 ~ 10.23                 |
| 남지민     | 주류 페이지 & 모델 설계, F.E  |          2024.9.23 ~ 10.23           |
| 배민석     | 칵테일 페이지 & 모델 설계   |       2024.9.23 ~ 10.23             |

---

---

## ⌛ 개발일정

- **기획 및 설계**: 9/23 ~ 9/25
- **MVP 개발**: 9/26 ~ 10/8
- **중간 발표회 준비**: 10/8 ~ 10/10
- **배포 및 추가 기능 구현**: 10/11 ~ 10/16
- **테스트 및 디버깅**: 10/17 ~ 10/20
- **최종 발표회 준비**: 10/21 ~ 10/23

---

## 🌟 주요 기능 
(1차 분류 - 회원 비회원 기능으로 나눌지 고민중)

- **회원가입 및 로그인**: JWT를 커스텀 한 인증 시스템을 사용하여 사용자 관리.
- **마이 프로필**: 회원 정보 및 설정 관리, 북마크한 술과 칵테일 페이지로 이동 기능
- **메인 페이지**: 일별로 무작위 칵테일 레시피 제공, 회원에게는 회원 정보에 따른 맞춤형 칵테일 추천 기능, 팁, 역사, 재밌는 이야기 등의 서브 데이터 info를 제공
- **회원 기능 관리**: 관리자, 일반 사용자에 따른 권한 부여. 회원 비회원 기능 분리
- **랜덤 칵테일 레시피**: 모든 사용자에게 랜덤하게 제공되는 칵테일 레시피를 제공. 일별로 업데이트
- **맞춤 칵테일 추천**: 회원에게만 제공되며, 사용자가 프로필에 입력한 정보(보유한 술, 선호하는 술, 싫어하는 술)를 바탕으로하여 추천하는 칵테일 레시피를 제공
- **Bangtenderbot 기능**: 웹사이트 데이터와 회원 정보를 기반으로 칵테일 및 주류 추천
- **주변 주류 매장 찾기**: 사용자의 주소 정보를 이용해 주변 주류 매장 정보를 제공
- **주류, 칵테일 페이지**: 주류 및 칵테일에 대한 이름, 가격, 이미지 등을 보여주고 이미지 클릭시 상세페이지 로 이동
- **주류 상세 페이지**: 주류의 맛, 도수, 가격, info 등 상세 정보를 제공
- **칵테일 상세 페이지**: 칵테일의 레시피, 맛, 만드는 법 등 상세 정보를 제공

---

## 🛠️ 설치 방법

### 1️⃣ 저장소 클론

```bash
git clone 
cd 
```

### 2️⃣ 가상 환경 설정 및 패키지 설치

```bash
python -m venv venv
source venv/bin/activate  # Mac
source venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 4️⃣ 슈퍼유저 생성 (관리자 계정)

```bash
python manage.py createsuperuser
```

### 5️⃣ 개발 서버 실행

```bash
python manage.py runserver
```

---

## 🖇️ 와이어 프레임
![image (2)](https://github.com/user-attachments/assets/8208f8a4-f69e-4394-845e-edece3fd36fb)

---

## 📋 API 사용법

자세한 API 명세서는 [Postman API Documentation](__추가예정)에서 확인할 수 있습니다.

### Accounts

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **비고**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| POST       | /api/v1/accounts/    | 회원가입                       | `username`, `password`, `password_confirm`, `name`, `email`, `address`  |        |
| DELETE       | /api/v1/accounts/      | 회원탈퇴                           | `password`                 |         |
| POST       | /api/v1/accounts/login/     | 로그인                         | `username`, `password`                                   |         |
| POST       | /api/v1/accounts/logout/     | 로그아웃                         | 없음                                   |         |
| GET       | /api/v1/accounts/<int:pk>/     | 프로필 확인                     | 없음                                   |         |
| PUT        | /api/v1/accounts/<int:pk>/     | 회원정보 수정      | `name`, `email`, `address`                |         |
| GET        | /api/v1/accounts/<int:pk>/bookmark/     | 내 북마크    | 없음                |         |
| PUT        | /api/v1/accounts/<int:pk>/password/     | 비밀번호 변경    | `old_password`, `new_password`                |         |


### Liquor

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **비고**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/v1/liquor/            | Liquor 조회                   | 없음                                   |         |
| POST       | /api/v1/liquor/            | Liquor 추가                        | `name`, `classification`, `img`, `content`, `taste`, `abv`, `price` |         |
| GET        | /api/v1/liquor/<int:pk>/       | 상세 조회                   | 없음                                   |         |
| PUT        | /api/v1/liquor/<int:pk>/       | Liquor 수정                        | `name`, `classification`, `img`, `content`, `taste`, `abv`, `price` |         |
| DELETE     | /api/v1/liquor/<int:pk>/       | Liquor 삭제                        | 없음                                   |         |
| POST       | /api/v1/liquor/<int:pk>/bookmark/ | 북마크               | 없음                                   |         |

### Cocktail

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **비고**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/v1/cocktail/            | Cocktail 조회                   | 없음                                   |         |
| POST       | /api/v1/cocktail/            | Cocktail 추가                        | `name`, `img`, `content`, `ingredients`, `taste`, `abv`  |         |
| GET        | /api/v1/cocktail/<int:pk>/       | 상세 조회                   | 없음                                   |         |
| PUT        | /api/v1/cocktail/<int:pk>/       | Cocktail 수정                        | `name`, `img`, `content`, `ingredients`, `taste`, `abv`  |         |
| DELETE     | /api/v1/cocktail/<int:pk>/       | Cocktail 삭제                        | 없음                                   |         |
| POST       | /api/v1/cocktail/<int:pk>/bookmark/ | 북마크               | 없음                                   |         |

### Subcontent

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **비고**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/v1/            | 메인 페이지                   | 없음                                   |         |
| GET        | /api/v1/search/            | 검색 기능                        | `message`                 |         |
| POST        | /api/v1/subcontent/fine-tuning/       | 파인튜닝                   | `진행중`                                   |         |
| GET        | /api/v1/subcontent/bangtenderbot/       | 추천 AI                       | `진행중`                              |         |
| GET     | /api/v1/subcontent/map/       | 주변 주류매장 찾기                      | `map`                                   |         |


---

## 🖼️ ERD (Entity Relationship Diagram)

### ERD 이미지
![스크린샷 2024-10-04 211454](https://github.com/user-attachments/assets/a2d018e0-ecb0-4e46-b9a5-fc488a5cffe8)
### ERD 설명

- **User 모델**: 각 사용자 계정 정보 및 역할 관리. 소프트 삭제(soft_delete) 기능으로 사용자 탈퇴 시 계정 비활성화.
- **Liquor 모델**: 양주 정보들. '좋아요'와 '북마크'를 할 수 있음.
- **Cocktail 모델**: 칵테일 정보들. '좋아요'와 '북마크'를 할 수 있음.
- **Info 모델**: 팁, 역사, 재밌는 이야기 등의 서브 데이터 제공.

---

## 🥃 회원 기반 접근 제어

- **관리자**: 모든 기능(게시글 생성, 삭제, 수정 등 게시글 관리)에 접근할 수 있습니다.
- **일반 사용자 (비회원)**: 랜덤 칵테일 레시피, 주류, 칵테일 정보, info 제공.
- **일반 사용자 (회원)**: 비회원 기능을 포함한 맞춤 칵테일 추천, Bangtenderbot 기능, 주변 주류 매장 찾기 기능 제공.

---

## 🛠️ 데이터베이스 관리

방텐더 프로젝트는 **postgresql**을 기본 데이터베이스로 사용합니다.

---

## 🌐 시스템 아키텍처

### 프론트엔드 구성

- **docker** : 추후 프론트엔드 추가

### 백엔드 구성

- **Django REST Framework**: API 설계를 위한 프레임워크
- **postgresql**: 데이터베이스
- **JWT**: 사용자 인증을 위한 토큰 방식 인증 시스템
- **ChatGPT**: GPT-4o-mini
- **bcrypt**: 사용자 비밀번호 해싱

---

## 🌕 개발 환경 및 사용 기술
    IDE : VSCODE
    Windows 10, 11  ,   MacOS
    Python 3.10.14
    Django 4.2
    djangorestframework 3.15.2 
    djangorestframework-simplejwt 5.3.1
    chatGPT GPT-4o-mini
    bycrypt 4.2

---

## 🛠️ 통합 및 인터페이스

- **REST API**: 프론트엔드와의 통신은 JSON 형식으로 데이터를 주고받습니다.
- **Postman**: API 문서화

---

## 🔐 보안

- **HTTPS 사용**: 모든 API 요청은 HTTPS를 통해 암호화되어 전송
- **JWT 인증**: JWT 토큰을 이용한 사용자 인증
- **비밀번호 암호화**: 사용자 비밀번호는 bcrypt 라이브러리를 사용하여 해시화하여 저장
- **역할 기반 권한 관리**: 관리자만 글 게시 및 수정 삭제 가능
