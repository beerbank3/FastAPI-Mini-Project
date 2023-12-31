**FastAPI 게시판 미니 프로젝트**

# 개요
- 기간: 2023-09-15 ~ 2023-09-18

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
|List|게시판 목록을 조회합니다. 본인이 생성하거나, 전체 공개된 게시판을 조회할 수 있습니다. 게시판 목록은 **해당 게시판에 작성된 게시글의 갯수** 순으로 정렬 가능해야 합니다.|**완료**|

3. 게시글 API  

|기능|기능설명|완료|
|------|---------------|----|
|Create|게시판 id, title, content 를 입력 받아 게시글을 생성합니다. 본인이 조회할 수 있는 게시판의 id 만 사용이 가능합니다.|**완료**|
|Update|게시글 id, title, content 을 입력 받아 해당 게시글의 title, content 를 수정합니다. 타 유저가 생성한 게시글은 수정할 수 없습니다.|**완료**|
|Delete|게시글 id 를 입력 받아 해당 게시글을 삭제합니다. 타 유저가 생성한 게시글은 삭제할 수 없습니다.|**완료**|
|Get|게시글 id 를 입력 받아 게시글을 조회합니다. 본인이 생성하거나, 전체 공개된 게시판의 게시글을 조회할 수 있습니다.|**완료**|
|List|게시판 id 을 입력 받아 해당 게시판에 있는 게시글 목록을 조회합니다. 본인이 조회할 수 있는 게시판의 id 만 사용이 가능합니다|**완료**|

# API 명세서
1. 계정 API  

    - SingUp

    ```
    POST /users/signup/
    ```

    ```
    // header
    {
    "Content-type": "application/json"
    }
    // body
    {
    "email": "user@example.com",
    "full_name": "string",
    "password": "string"
    }
    ```

    - Login

    ```
    POST /login/
    ```

    ```
    // header
    {
    "Content-type": "application/json"
    }
    // body
    {
    "email": "user@example.com",
    "password": "string"
    }
    ```

    - Logout
    ```
    POST /logout/
    ```

    ```
    // header
    {
    "Content-type": "application/json"
    }
    ```

2. 게시판 API 

    - Create
    ```
    POST /boards/create/
    ```
    ```
    // header
    {
    "Content-type": "application/json"
    }
    // body
    {
    "name": "string",
    "public": true
    }
    ```
    - Update
    ```
    /boards/update/
    ```
    ```
    // header
    {
    "Content-type": "application/json"
    }
    // body
    {
    "name": "string",
    "public": true,
    "id": 0
    }
    ```
    - Delete
    ```
    POST /boards/delete/
    ```
    ```
    // header
    {
    "Content-type": "application/json"
    }
    // body
    {
    "id": 0
    }
    ```
    - Get
    ```
    GET /boards/{board_id}/
    ```

    ```
    // Responses
    {
    "name": "string",
    "public": true,
    "id": 0
    }
    ```
    - List

    ```
    GET /boards/skip={int}
    ```

3. 게시글 API

    - Create
    ```
    POST /posts/create/
    ```
    ```
    // header
    {
        "Content-type": "application/json"
    }
    // body
    {
    "title": "string",
    "content": "string",
    "board_id": 0
    }
    ```
    - Update
    ```
    POST /posts/update/
    ```
    ```
    // header
    {
        "Content-type": "application/json"
    }
    // body
    {
    "title": "string",
    "content": "string",
    "id": 0
    }
    ```
    - Delete
    ```
    POST /posts/delete/
    ```
    ```
    // header
    {
        "Content-type": "application/json"
    }
    // body
    {
    "id": 0
    }
    ```
    - Get
    ```
    GET /posts/get/{post_id}
    ```
    ```
    // Responses
    {
    "id": 0,
    "title": "string",
    "content": "string",
    "board_id": 0
    }

    ```
    - List
    ```
    GET /posts/{board_id}/skip={int}
    ```

# 기능 구현
- docs, Postman으로 API 테스트
1. 계정 API  
    - SingUp  
    ![회원가입](README/Singup.gif)
    - Login  
    ![로그인](README/Login.gif)
    - Logout  
    ![로그아웃](README/Logout.gif)
2. 게시판 API
    - Create  
    ![생성](README/BoardCreate.gif)
    - Update  
    ![수정](README/BoardUpdate.gif)
    - Delete  
    ![삭제](README/BoardDelete.gif)
    - Get  
    ![상세보기](README/BoardGet.gif)
    - List  
    ![리스트](README/BoardList.gif)
3. 게시글 API
    - Create  
    ![생성](README/PostCreate.gif)
    - Update  
    ![수정](README/PostUpdate.gif)
    - Delete  
    ![삭제](README/PostDelete.gif)
    - Get  
    ![상세보기](README/PostGet.gif)
    - List  
    ![리스트](README/PostList.gif)

# 폴더 구조
```
Interview_Project
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
│  │  ├─ crud_board.py
│  │  ├─ crud_post.py
│  │  └─ crud_user.py
│  ├─ db
│  │  └─ database.py
│  ├─ main.py
│  ├─ models
│  │  └─ model.py
│  └─ schemas
│     ├─ board.py
│     ├─ post.py
│     ├─ token.py
│     └─ user.py
├─ docker-compose.yml
├─ Dockerfile
├─ README
├─ README.md
└─ requirements.txt
```

# 참고
1. Google
2. ChatGPT
3. https://github.com/tiangolo/full-stack-fastapi-postgresql