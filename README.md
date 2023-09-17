# Interview_Project
**[엘리스] 미니 프로젝트**

# 기능
1. 계정 API  

|기능|기능설명|완료|
|------|---------------|----|
|SingUp|계정 정보(fullname, email, password) 를 입력 받아 계정을 생성합니다.|**완료**|
|Login|email, password 를 입력 받아 계정에 로그인하고, 해당 로그인 세션의 access token 을 반환합니다.|**완료**|
|Logout|현재 로그인 세션을 로그아웃 합니다.|**완료**|

2. 게시판 API 

|기능|기능설명|완료|
|------|---------------|----|
|Create|name, public (boolean) 을 입력 받아 게시판을 생성합니다. name 은 unique 해야합니다. public 이 true 이면 전체 로그인 된 유저에게 공개, public 이 false 이면 생성자에게만 공개되는 게시판입니다.|**완료**|
|Update|게시판 id, name, public 을 입력 받아 해당 게시판의 name, public 을 수정합니다. 타 유저가 생성한 게시판은 수정할 수 없습니다.|**완료**|
|Delete|게시판 id 를 입력 받아 해당 게시판을 삭제합니다. 타 유저가 생성한 게시판은 삭제할 수 없습니다.|**완료**|
|Get|게시판 id 를 입력 받아 게시판을 조회합니다. 본인이 생성하거나, 전체 공개된 게시판을 조회할 수 있습니다.|**완료**|
|List|게시판 목록을 조회합니다. 본인이 생성하거나, 전체 공개된 게시판을 조회할 수 있습니다. 게시판 목록은 **해당 게시판에 작성된 게시글의 갯수** 순으로 정렬 가능해야 합니다.|**미완**|

3. 게시글 API  

|기능|기능설명|완료|
|------|---------------|----|
|Create|게시판 id, title, content 를 입력 받아 게시글을 생성합니다. 본인이 조회할 수 있는 게시판의 id 만 사용이 가능합니다.|**완료**|
|Update|게시글 id, title, content 을 입력 받아 해당 게시글의 title, content 를 수정합니다. 타 유저가 생성한 게시글은 수정할 수 없습니다.|**완료**|
|Delete|게시글 id 를 입력 받아 해당 게시글을 삭제합니다. 타 유저가 생성한 게시글은 삭제할 수 없습니다.|**완료**|
|Get|게시글 id 를 입력 받아 게시글을 조회합니다. 본인이 생성하거나, 전체 공개된 게시판의 게시글을 조회할 수 있습니다.|**완료**|
|List|게시판 id 을 입력 받아 해당 게시판에 있는 게시글 목록을 조회합니다. 본인이 조회할 수 있는 게시판의 id 만 사용이 가능합니다|**완료**|

# 폴더 구조
```
Interview_Project
├─ .gitignore
├─ app
│  ├─ api
│  │  ├─ api.py
│  │  ├─ endpoints
│  │  │  ├─ board.py
│  │  │  ├─ login.py
│  │  │  ├─ posts.py
│  │  │  ├─ users.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ core
│  │  └─ security.py
│  ├─ crud
│  │  ├─ base.py
│  │  ├─ crud_board.py
│  │  ├─ crud_post.py
│  │  └─ crud_user.py
│  ├─ db
│  │  └─ database.py
│  ├─ main.py
│  ├─ models
│  │  ├─ board.py
│  │  ├─ post.py
│  │  └─ user.py
│  └─ schemas
│     ├─ board.py
│     ├─ post.py
│     ├─ token.py
│     └─ user.py
├─ docker-compose.yml
├─ Dockerfile
├─ README.md
└─ requirements.txt