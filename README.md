# Goods-accounting-system
### Система учета проданных товаров


`/ ` 
Главная страница сайта на Django(просмотр содержимого магазинов, 
складов и проданных товаров с указанием его категории, магазина, 
который его продал и склада, с которого он был отгружен.
Только для зарегистрированных пользователей.  

![alt tag](https://i.ibb.co/rm7Y0d3/Peek-2021-03-01-23-09.gif)


##### API(Только для зарегистрированных пользователей):

[POST] `/auth/users/` - Регистрация (username, password, email(не обязательно))  

Request:
```json
{
    "username": "test1",
    "password": "test123"
}
```
Response:  

```json
{
    "email": "",
    "username": "test1",
    "id": 2
}
```

[POST] `/auth/token/login/` - Получение токена  

Request:
```json
{
    "username": "test1",
    "password": "test123"
}
```
Response:  

```json
{
    "auth_token": "e8a55fa93dbc2255dadd7e53aa7b3f6a8b9051f8"
}
```

[GET] `/auth/users/me/`  - Данные о текущем пользователе  
Response:  

```json
{
    "email": "",
    "id": 2,
    "username": "test1"
}
```

[POST] `/auth/token/logout/` - Выход и удаление токена


[GET] `/api/products/` - возвращает список товаров  

Response:
```json
{
  "id": 3,
  "name": "Кофе Jacobs",
  "price": 13,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
},
{
  "id": 4,
  "name": "Кофе Jacobs2",
  "price": 15,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```
[POST] `/api/products/` - добавление товара  

Request:
```json
{
  "name": "Кофе Jacobs",
  "price": 13,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```
Response:  

```json
{
  "id": 3,
  "name": "Кофе Jacobs",
  "price": 13,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```

[GET] `/api/products/{productsId}/` - запроса отдельного товара по id  

Response:  

```json
{
  "id": 3,
  "name": "Кофе Jacobs",
  "price": 13,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```

[PUT] `/api/products/{productsId}/` - запрос для изменения товара  

Request:
```json
{
  "name": "Кофе Jacobs",
  "price": 15,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```
Response:  

```json
{
  "id": 3,
  "name": "Кофе Jacobs",
  "price": 15,
  "sold_out": false,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```

[PATCH] `/api/products/{productsId}/` - добавление в список проданных  

Request:
```json
{
  "sold_out": true
}
```
Response:  

```json
{
  "id": 3,
  "name": "Кофе Jacobs",
  "price": 15,
  "sold_out": true,
  "category": 2,
  "warehouse": 4,
  "shop": 6
}
```
[DELETE] `/api/products/{productsId}/` - удаление товара

[GET] `/api/category/` - запрос списка категорий  

Response: 
```json
{
    "id": 1,
    "title": "Обувь"
},
{
    "id": 2,
    "title": "Кофе"
}
```
[POST] `/api/category/` - добавление категорий  

Request:
```json
{
  "title": "Обои"
}
```

Response: 
```json
{
    "id": 8,
    "title": "Обои"
}
```
[GET] `/api/category/{categoryId}/` - запрос отдельной категории

Response: 
```json
{
    "id": 1,
    "title": "Обувь"
}
```

[PUT] `/api/category/{categoryId}/` - изменение категории

Request: 
```json
{
    "title": "Кроссовки"
}
```
Response: 
```json
{
    "id": 1,
    "title": "Кроссовки"
}
```
[DELETE] `/api/category/{categoryId}/` - удаление категории

[GET] `/api/shops/` - запрос списка магазинов  

Response:
```json
{
    "id": 1,
    "name": "Waikiki",
    "domain": "waikiki.by",
    "link": "https://waikiki.by"
},
{
    "id": 2,
    "name": "БелОбувь",
    "domain": "bel-shoes.by",
    "link": "https://bel-shoes.by"
}
```
[POST] `/api/shops/` - добавление магазина  

Request:
```json
{
    "name": "H&M",
    "domain": "hm.by",
    "link": "https://hm.by"
}
```
Response:
```json
{
    "id": 3,
    "name": "H&M",
    "domain": "hm.by",
    "link": "https://hm.by"
}
```
[GET] `/api/shops/{shopsId}/` - запрос отдельного магазина

Response: 
```json
{
    "id": 1,
    "name": "Waikiki",
    "domain": "waikiki.by",
    "link": "https://waikiki.by"
}
```

[PUT] `/api/shops/{shopsId}/` - изменение магазина

Request: 
```json
{
    "name": "H&M_UPDATE",
    "domain": "hm.by",
    "link": "https://hm.by"
}
```
Response: 
```json
{
    "id": 3,
    "name": "H&M_UPDATE",
    "domain": "hm.by",
    "link": "https://hm.by"
}
```
[DELETE] `/api/shops/{shopsId}/` - удаление магазина


[GET] `/api/warehouse/` - запрос списка складов  

_Response:_
```json
{
    "id": 1,
    "name": "Брест",
    "shop": [
        1
    ]
},
{
    "id": 2,
    "name": "Минск",
    "shop": [
        1,
        2
    ]
},
```
[POST] `/api/warehouse/` - добавление склада  

_Request:_
```json
{
    "name": "Витебск",
    "shop": [
        2
    ]
}
```
_Response:_
```json
{
    "id": 6,
    "name": "Витебск",
    "shop": [
        2
    ]
}
```
[GET] `/api/warehouse/{warehouseId}/` - запрос отдельного склада

_Response:_ 
```json
{
    "id": 5,
    "name": "Могилев",
    "shop": [
        4
    ]
}
```

[PUT] `/api/warehouse/{warehouseId}/` - изменение склада

_Request:_ 
```json
{
    "name": "Могилев_UPDATE",
    "shop": [
        4
    ]
}
```
_Response:_ 
```json
{
    "id": 5,
    "name": "Могилев_UPDATE",
    "shop": [
        4
    ]
}
```
[DELETE] `/api/warehouse/{warehouseId}/` - удаление склада

[GET] `/api/sold_out_product/` - запрос списка проданных товаров  

_Response:_ 
```json
{
    "id": 19,
    "name": "Чай Tess3",
    "price": "11.66",
    "sold_out": true,
    "category": 3,
    "warehouse": 5,
    "shop": 5
},
{
    "id": 20,
    "name": "Чай Tess4",
    "price": "11.76",
    "sold_out": true,
    "category": 3,
    "warehouse": 1,
    "shop": 5
}
```
Фильтрация проданных товаров по полям: 'name', 'shop', 'category', 'warehouse'

[GET] `/api/sold_out_product/?shop=3` - пример фильтрации товаров по магазину  

_Response:_ 
```json
{
    "id": 26,
    "name": "Стул Ikea",
    "price": "19.52",
    "sold_out": true,
    "category": 5,
    "warehouse": 4,
    "shop": 3
},
{
    "id": 5,
    "name": "Стул",
    "price": "22.50",
    "sold_out": true,
    "category": 5,
    "warehouse": 2,
    "shop": 3
}
```