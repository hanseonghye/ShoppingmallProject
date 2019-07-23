# /users/check/id/{user_id}

## id 중복 체크

■ url

 `get : /users/check/id/{user_id}`

■ request

- path

  `user_id : 중복 확인하고 싶은 ID 값 `

■ response

- 형식에 맞지 않는 id : status code `400`

  ```python
  {"result": "fail", "message": "id양식을 맞춰주세요", "data": null}
  ```

- 중복된 id : status code `400`

  ```python
  {"result": "fail", "message": "이미 사용하고 있는 id입니다.", "data": null}
  ```

- 사용할 수 있는 id : status code `200`

  ```python
  {"result": "success", "message": null, "data": "ok"}
  ```