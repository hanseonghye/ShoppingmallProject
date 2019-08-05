# API



# 1. API 명세

# 회원 + 비회원 :person_with_pouting_face:



## 회원 정보

| API 목록         | URL                                   | 일정 | 소요시간 | 개발 완료 | 작업 결과서                                                  |
| ---------------- | ------------------------------------- | ---- | -------- | --------- | ------------------------------------------------------------ |
| 회원가입         | post : /users                         | 7/22 | 3h       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.md#%EA%B0%80%EC%9E%85-%EB%93%B1%EB%A1%9D-%EC%9A%94%EC%B2%AD) |
| 아이디 중복 확인 | get : /users/check/id/{check_id}      | 7/22 | 30m      | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.md#%EC%95%84%EC%9D%B4%EB%94%94-%EC%A4%91%EB%B3%B5-%EC%B2%B4%ED%81%AC-%EC%9A%94%EC%B2%AD) |
| 로그인           |                                       | 8/8  | 1h       | X         |                                                              |
| 로그아웃         |                                       | 8/8  | 30m      | X         |                                                              |
| 회원정보조회     | get:/users/{user_id or pk}            | 7/19 | 10m      | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%ED%83%88%ED%87%B4.md) |
| 회원정보수정     | put : /users/{user_id or pk}          | 7/19 | 10m      | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%ED%83%88%ED%87%B4.md) |
| 회원탈퇴         | delete : /users/{user_id or pk}       | 7/19 | 10m      | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%ED%83%88%ED%87%B4.md) |
| 회원 주소 확인   | get : /users/{user_id or pk}/address  | 7/22 | 30m      | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EB%B0%B0%EC%86%A1%EC%A7%80%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 회원 주소 추가   | post : /users/{user_id or pk}/address | 7/22 | 30m      | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EB%B0%B0%EC%86%A1%EC%A7%80%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 회원 주소 삭제   |                                       | 7/22 | 10m      | X         |                                                              |



## 상품

| API 목록  | URL                  | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| --------- | -------------------- | ---- | --------- | --------- | ------------------------------------------------------------ |
| 상품 조회 | get : /products/{pk} | 7/27 | 1h        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C.md) |



## 장바구니

| API 목록             | URL                                                | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| -------------------- | -------------------------------------------------- | ---- | --------- | --------- | ------------------------------------------------------------ |
| 장바구니 조회        | get : /carts/user/{user-pk}                        | 7/31 | 30m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 장바구니 추가        | post : /carts/user/{user-pk}                       | 7/31 | 1m        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 장바구니 수정        | put : /carts/user/{user-pk}/{cart-pk}              | 7/31 | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 장바구니 삭제        | delete : /carts/user/{user-pk}/{cart-pk}           | 7/31 | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 비회원 장바구니 조회 | get : /carts/nonuser/{nonuser-number}              | 8/2  | 30m       | O         |                                                              |
| 비회원 장바구니 추가 | post : /carts/nonuser/{nonuser-number}             | 8/2  | 30m       | O         |                                                              |
| 비회원 장바구니 수정 | put : /carts/nonuser/{nonuser-number}/{cart-pk}    | 8/2  | 10m       | O         |                                                              |
| 비회원 장바구니 삭제 | delete : /carts/nonuser/{nonuser-number}/{cart-pk} | 8/2  | 10m       | O         |                                                              |



## 주문

| API 목록         | URL                                                | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| ---------------- | -------------------------------------------------- | ---- | --------- | --------- | ------------------------------------------------------------ |
| 주문 등록        | post : /orders                                     | 7/28 | 5h        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0.md) |
| 주문 조회        | get : /orders/user/{user-pk or user_id}            | 7/28 | 30m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%A3%BC%EB%AC%B8%EC%A1%B0%ED%9A%8C.md) |
| 특정 주문 조회   | get : /orders/user/{user-pk or user_id}/{order-pk} | 7/28 | 30m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%A3%BC%EB%AC%B8%EC%A1%B0%ED%9A%8C(%ED%8A%B9%EC%A0%95).md) |
| 비회원 주문 조회 | get : /orders/nonuser/{nonuser-number}             | 8/1  | 30m       | x         |                                                              |



## 카테고리

| API 목록             | URL                           | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| -------------------- | ----------------------------- | ---- | --------- | --------- | ------------------------------------------------------------ |
| 카테고리로 상품 조회 | get : /categorys/{id or name} | 7/18 | 1h 30m    | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EB%A1%9C%20%EC%83%81%ED%92%88%20%EC%A1%B0%ED%9A%8C.md) |



------

----





# 관리자 :information_desk_person:



## 관리자 정보

| API 목록         | URL                          | 일정 | 소요 시간 | 개발 완료 | 작업 결과서 |
| ---------------- | ---------------------------- | ---- | --------- | --------- | ----------- |
| 전체 관리자 조회 | get : /admin/manager         | 7/22 | 30m       | X         |             |
| 관리자 등록      | post : /admin/manager        | 7/22 | 2m        | X         |             |
| 특정 관리자 조회 | get : /admin/manager/{id}    | 7/22 | 30m       | X         |             |
| 관리자 정보 수정 | put : /admin/manager/{id}    | 7/22 | 10m       | X         |             |
| 관리자 삭제      | delete : /admin/manager/{id} | 7/22 | 10m       | X         |             |



## 회원 

| API 목록         | URL                | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| ---------------- | ------------------ | ---- | --------- | --------- | ------------------------------------------------------------ |
| 회원 리스트 조회 | get : /admin/users | 7/19 | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%ED%9A%8C%EC%9B%90%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%A1%B0%ED%9A%8C.md) |




## 상품

| API 목록                  | URL                                                          | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| ------------------------- | ------------------------------------------------------------ | ---- | --------- | --------- | ------------------------------------------------------------ |
| 상품 등록                 | post : /admin/products                                       | 8/1  | 3h        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EB%93%B1%EB%A1%9D.md) |
| 상품 조회                 | get : /admin/products/{pk}                                   | 8/1  | 20m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md#%EC%83%81%ED%92%88-%EC%A1%B0%ED%9A%8C) |
| 상품 수정                 | put : /admin/products/{pk}                                   | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md#%EC%83%81%ED%92%88-%EC%88%98%EC%A0%95) |
| 상품 삭제                 | delete : /admin/products/{pk}                                | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md#%EC%83%81%ED%92%88-%EC%82%AD%EC%A0%9C) |
| 특정 상품 총 옵션명 조회  | get : /admin/products/{id}/options                           | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EB%AA%85%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 상품 옵션명 추가          | post : /admin/products/{id}/options                          | 8/1  | 1h        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EB%AA%85%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 옵션 명 조회              | get : /admin/products/{pk}/options/{option_pk}               | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 옵션 명 수정              | put : /admin/products/{pk}/options/{option_pk}               | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 옵션 명 삭제              | delete : /admin/products/{pk}/options/{option_pk}            | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 특정 상품 총 옵션 값 조회 | get : /admin/products/{pk}/options/{option_pk}/detail        | 8/1  | 20m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 옵션 값 추가              | post : /admin/products/{pk}/options/{option_pk}/detail       | 8/1  | 30m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 옵션 값 조회              | get : /admin/products/{pk}/options/{option-pk}/detail/{optiondetail-pk} | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 옵션 값 수정              | put : /admin/products/{pk}/options/{option-pk}/detail/{optiondetail-pk} | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 옵션 값 삭제              | delete : /admin/products/{pk}/options/{option-pk}/detail/{optiondetail-pk} | 8/1  | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |



## 주문

| API 목록  | URL                      | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| --------- | ------------------------ | ---- | --------- | --------- | ------------------------------------------------------------ |
| 주문 조회 | get : /admin/orders      | 8/1  | 1h        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%A3%BC%EB%AC%B8%EC%A1%B0%ED%9A%8C(%EA%B4%80%EB%A6%AC%EC%9E%90).md) |
| 주문 수정 | put : /admin/orders/{pk} | 8/1  | 30m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%A3%BC%EB%AC%B8%EC%88%98%EC%A0%95.md) |




## 카테고리

| API 목록           | URL                                   | 일정 | 소요 시간 | 개발 완료 | 작업 결과서                                                  |
| ------------------ | ------------------------------------- | ---- | --------- | --------- | ------------------------------------------------------------ |
| 전체 카테고리 조회 | get : /admin/category                 | 7/18 | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 카테고리 추가      | post : /admin/category                | 7/18 | 1h        | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 카테고리 수정      | put : /admin/category/{pk or name}    | 7/18 | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 카테고리 삭제      | delete : /admin/category/{pk or name} | 7/18 | 10m       | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.API/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |



# 2. 기타 사항

- patch method

  update할 시, 현재 put method를 쓴다. 이 경우 회원 정보 수정을 예로 들때, 비밀번호를 수정하고자 하면 비밀번호 뿐만 아니라 이름, 이메일과 같은 다른 모든 정보가 save된다. (따로 비밀번호 수정 method가 아닌, 회원 정보 수정 method로 진행되기 때문.) 하지만 patch method를 할 경우 하나의 회원정보 수정method로 변경 된 정보만을 update할 수 있다. 따라서 모든 update는 api명세서에 작성된 put method가 아닌, patch method로 변경할 예정이다. (혹은 둘다 가능)

- url 고민

  url을 구성할 때, 통일성 부분을 고민했다.

  예를 들어 주문 조회의 경우 `orders/user/{user-pk}`로 특정 user의 모든 주문을 확인할 수 있다. 이때, user의 모든 특정 주문을 확인할려면, `orders/user/{user-pk}/{oder-pk}`로 접근한다. 그런데 이때 특정 주문의 경우 `order-pk`로 가져오기 때문에 `user-pk`값은 필요없다. 하지만 뭔가 user의 모든 주문 조회 url과 통일성을 줘야할 것 같아서 `orders/user/{user-pk}/{oder-pk}`로 설정했다. 이 사항은 계속 생각하고 질문하면서 변경될 수 있다.

- 상품추가와 옵션 추가

  현재 상품 추가와 상품의 옵션 추가는 각각 별개의 api에서 이뤄진다. 추가적으로 상품을 추가할 때 옵션도 함께 추가하는 api를 만들 것 이다.

- 관리자 가입

  관리자는 관리자 테이블을 만들지 않고 회원 테이블에 별도록 컬럼을 통해 구분할려고 했다. 그런데 oauth2를 적용할려면 관리자와 회원 구분을 이런식으로 해도되는지  확실하지 않아 미뤄놨다.
  
- validation

  전체적인 validation은 아직 미흡하다. 프론트단 하면서 시간이 남을 시 보완할 것이다.