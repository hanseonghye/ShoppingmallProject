# API



# 회원 :person_with_pouting_face:



## 회원 정보

| API 목록         | URL                                   | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| ---------------- | ------------------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 회원가입         | post : /users                         |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.md#%EA%B0%80%EC%9E%85-%EB%93%B1%EB%A1%9D-%EC%9A%94%EC%B2%AD) |
| 아이디 중복 확인 | get : /users/check/id/{check_id}      |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.md#%EC%95%84%EC%9D%B4%EB%94%94-%EC%A4%91%EB%B3%B5-%EC%B2%B4%ED%81%AC-%EC%9A%94%EC%B2%AD) |
| 로그인           |                                       |         | X         |                                                              |
| 로그아웃         |                                       |         | X         |                                                              |
| 회원정보조회     | get:/users/{user_id or pk}            |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%ED%83%88%ED%87%B4.md) |
| 회원정보수정     | put : /users/{user_id or pk}          |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%ED%83%88%ED%87%B4.md) |
| 회원탈퇴         | delete : /users/{user_id or pk}       |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%ED%83%88%ED%87%B4.md) |
| 회원 주소 확인   | get : /users/{user_id or pk}/address  |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EB%B0%B0%EC%86%A1%EC%A7%80%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 회원 주소 추가   | post : /users/{user_id or pk}/address |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EB%B0%B0%EC%86%A1%EC%A7%80%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 회원 주소 삭제   |                                       |         | X         |                                                              |



## 상품

| API 목록  | URL                  | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| --------- | -------------------- | ------- | --------- | ------------------------------------------------------------ |
| 상품 조회 | get : /products/{pk} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C.md) |



## 장바구니

| API 목록      | URL                                      | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| ------------- | ---------------------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 장바구니 조회 | get : /carts/user/{user-pk}              |         | X         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 장바구니 추가 | post : /carts/user/{user-pk}             |         | X         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 장바구니 수정 | put : /carts/user/{user-pk}/{cart-pk}    |         | X         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 장바구니 삭제 | delete : /carts/user/{user-pk}/{cart-pk} |         | X         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |



## 주문

| API 목록      | URL                                                | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| ------------- | -------------------------------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 주문 등록     | post : /orders                                     |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0.md) |
| 주문 조회     | get : /orders/user/{user-pk or user_id}            |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%A3%BC%EB%AC%B8%EC%A1%B0%ED%9A%8C.md) |
| 특정 주문조회 | get : /orders/user/{user-pk or user_id}/{order-pk} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%A3%BC%EB%AC%B8%EC%A1%B0%ED%9A%8C(%ED%8A%B9%EC%A0%95).md) |



## 카테고리

| API 목록             | URL                           | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| -------------------- | ----------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 카테고리로 상품 조회 | get : /categorys/{id or name} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EB%A1%9C%20%EC%83%81%ED%92%88%20%EC%A1%B0%ED%9A%8C.md) |



------

----





# 관리자 :information_desk_person:



## 관리자 정보

| API 목록         | URL                          | 개발 일 | 개발 완료 | 작업 결과서 |
| ---------------- | ---------------------------- | ------- | --------- | ----------- |
| 전체 관리자 조회 | get : /admin/manager         |         | X         |             |
| 관리자 등록      | post : /admin/manager        |         | X         |             |
| 특정 관리자 조회 | get : /admin/manager/{id}    |         | X         |             |
| 관리자 정보 수정 | put : /admin/manager/{id}    |         | X         |             |
| 관리자 삭제      | delete : /admin/manager/{id} |         | X         |             |



## 회원 

| API 목록         | URL                | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| ---------------- | ------------------ | ------- | --------- | ------------------------------------------------------------ |
| 회원 리스트 조회 | get : /admin/users |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%ED%9A%8C%EC%9B%90%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%A1%B0%ED%9A%8C.md) |




## 상품

| API 목록                  | URL                                                          | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| ------------------------- | ------------------------------------------------------------ | ------- | --------- | ------------------------------------------------------------ |
| 상품 등록                 | post : /admin/products                                       |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EB%93%B1%EB%A1%9D.md) |
| 상품 조회                 | get : /admin/products/{pk}                                   |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md#%EC%83%81%ED%92%88-%EC%A1%B0%ED%9A%8C) |
| 상품 수정                 | put : /admin/products/{pk}                                   |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md#%EC%83%81%ED%92%88-%EC%88%98%EC%A0%95) |
| 상품 삭제                 | delete : /admin/products/{pk}                                |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md#%EC%83%81%ED%92%88-%EC%82%AD%EC%A0%9C) |
| 특정 상품 총 옵션명 조회  | get : /admin/products/{id}/options                           |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EB%AA%85%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 상품 옵션명 추가          | post : /admin/products/{id}/options                          |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EB%AA%85%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 옵션 명 조회              |                                                              |         | O         |                                                              |
| 옵션 명 수정              |                                                              |         | O         |                                                              |
| 옵션 명 삭제              |                                                              |         | O         |                                                              |
| 특정 상품 총 옵션 값 조회 | get : /admin/products/{pk}/options/{option_pk}/detail        |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 옵션 값 추가              | post : /admin/products/{pk}/options/{option_pk}/detail       |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 옵션 값 조회              | get : /admin/products/{pk}/options/{option-pk}/detail/{optiondetail-pk} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 옵션 값 수정              | put : /admin/products/{pk}/options/{option-pk}/detail/{optiondetail-pk} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 옵션 값 삭제              | delete : /admin/products/{pk}/options/{option-pk}/detail/{optiondetail-pk} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%83%81%ED%92%88%EC%98%B5%EC%85%98%EA%B0%92%20%EC%A1%B0%ED%9A%8C%2B%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |



## 주문

| API 목록  | URL                      | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| --------- | ------------------------ | ------- | --------- | ------------------------------------------------------------ |
| 주문 조회 | get : /admin/orders      |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%A3%BC%EB%AC%B8%EC%A1%B0%ED%9A%8C(%EA%B4%80%EB%A6%AC%EC%9E%90).md) |
| 주문 수정 | put : /admin/orders/{pk} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%A3%BC%EB%AC%B8%EC%88%98%EC%A0%95.md) |




## 카테고리

| API 목록           | URL                                   | 개발 일 | 개발 완료 | 작업 결과서                                                  |
| ------------------ | ------------------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 전체 카테고리 조회 | get : /admin/category                 |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 카테고리 추가      | post : /admin/category                |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%A1%B0%ED%9A%8C%2B%EC%B6%94%EA%B0%80.md) |
| 카테고리 수정      | put : /admin/category/{pk or name}    |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |
| 카테고리 삭제      | delete : /admin/category/{pk or name} |         | O         | [문서](https://github.com/hanseonghye/ShoppingmallProject/blob/master/docs/2.Swagger%26TDD/api/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%20%EC%88%98%EC%A0%95%2B%EC%82%AD%EC%A0%9C.md) |

