# /users/{user_pk or user_id}

## 회원 가입

■ url

 `post : /users/{user_pk or user_id}`

■ request

- path

  `user_id or pk : user id나 pk `
  
- parameter : json

  ```json
  {
      username : string,
      user_id : string,
      password : string,
      email : string,
      phone_number : string
  }
  ```

  

■ response : 200

- 성공

  ```json
  {
      "result": "success", 
      "message": null, 
      "data":{ // 생성된 user 정보
          username : string,
          user_id : string,
          password : string,
          email : string,
          phone_number : string
      }
  }
  ```

- 실패

  ```json
  {
      "result":"fail",
      "message":"실패 원인",
      "data":null
  }
  ```



## 회원 정보 수정

■ url

 `put : /users/{user_pk or user_id}`

■ request

- path

  `user_id or pk : user id나 pk `

- parameter : json

  ```json
  {
      username : string,
      user_id : string,
      password : string,
      email : string,
      phone_number : string
  }
  ```

  

■ response : 200

- 성공

  ```json
  {
      "result": "success", 
      "message": null, 
      "data":{ // 생성된 user 정보
          username : string,
          user_id : string,
          password : string,
          email : string,
          phone_number : string
      }
  }
  ```

- 실패

  ```json
  {
      "result":"fail",
      "message":"실패 원인",
      "data":null
  }
  ```



## 회원 탈퇴

■ url

 `delete : /users/{user_pk or user_id}`

■ request

- path

  `user_id or pk : user id나 pk `

■ response : 200

- 성공

  ```json
  {
      "result": "success", 
      "message": null, 
      "data":"ok"
  }
  ```

- 실패

  ```json
  {
      "result":"fail",
      "message":"실패 원인",
      "data":null
  }
  ```

