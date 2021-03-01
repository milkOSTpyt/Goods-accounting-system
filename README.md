# Goods-accounting-system
Система учета проданных товаров


/  
Главная страница сайта на Django(просмотр содержимого магазинов, 
складов и проданных товаров с указанием его категории, магазина, 
который его продал и склада, с которого он был отгружен.
Только для зарегистрированных пользователей.


API(Только для зарегистрированных пользователей):

http://127.0.0.1:8000/auth/users/ - Регистрация (username, password, email(не обязательно))

http://127.0.0.1:8000/auth/token/login/ - Вход для получения токена 

http://127.0.0.1:8000/auth/users/me/  - Данные о текущем пользователе

http://127.0.0.1:8000/auth/token/logout/ - Выход и удаление токена


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

http://127.0.0.1:8000/api/category/1
Ссылка для запроса отдельной категории по id(GET) и для изменения категории(PUT)

http://127.0.0.1:8000/api/shops/
Ссылка для просмотра списка магазинов(GET) и для добавления магазина(POST)

http://127.0.0.1:8000/api/shops/1
Ссылка для просмотра отдельного магазина по id(GET) и для изменения магазина(PUT)

http://127.0.0.1:8000/api/warehouse/
Ссылка для запроса списка складов(GET) и для добавления склада(POST)

http://127.0.0.1:8000/api/warehouse/1
Ссылка для запроса отдельного склада по id(GET) и для изменения склада(PUT)

http://127.0.0.1:8000/api/sold_out_product/
Ссылка для запроса списка проданных товаров с возможностью фильтрации ( 'name', 'shop', 'category', 'warehouse')

Пример фильтрации - http://127.0.0.1:8000/api/sold_out_product/?shop=1