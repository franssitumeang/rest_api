# REST API Python

This REST API develop with python(django_rest) and has been deployed to [heroku](https://www.heroku.com/)

## API Documentation
### Topic Management

* **List Topic - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/topic/list](https://rest-api-ku.herokuapp.com/api/topic/list)
* **View Detail Topic - GET**<br>
[https://rest-api-ku.herokuapp.com/api/topic/detail/{id}](https://rest-api-ku.herokuapp.com/api/topic/detail/3)
* **Create Topic - POST**<br>
[https://rest-api-ku.herokuapp.com/api/topic/create](https://rest-api-ku.herokuapp.com/api/topic/create)

**body param**
```json
{
  "name": "topic_name" 
}
```
* Update Topic --> method **PUT**<br>
[https://rest-api-ku.herokuapp.com/api/topic/update/{id}](https://rest-api-ku.herokuapp.com/api/topic/update/{id})

**body param**
```json
{
  "name": "topic_name" 
}
```
* Delete Topic --> method **DELETE**<br>
[https://rest-api-ku.herokuapp.com/api/topic/delete/{id}](https://rest-api-ku.herokuapp.com/api/topic/delete/{id})

### News Management

* List News --> method **GET**<br>
[https://rest-api-ku.herokuapp.com/api/news/list](https://rest-api-ku.herokuapp.com/api/news/list)
* View Detail News --> method **GET**<br>
[https://rest-api-ku.herokuapp.com/api/news/detail/{id}](https://rest-api-ku.herokuapp.com/api/news/detail/3)
* Create News --> method **POST**<br>
[https://rest-api-ku.herokuapp.com/api/news/create](https://rest-api-ku.herokuapp.com/api/news/create)

**body param**
```json
{
  "title": "news_title",
  "status": "news_status",
  "topic": [3,4] 
}
```
* Update News -	-> method **PUT**<br>
[https://rest-api-ku.herokuapp.com/api/news/update/{id}](https://rest-api-ku.herokuapp.com/api/news/update/{id})

**body param**
```json
{
  "title": "news_title",
  "status": "news_status",
  "topic": [3,4] 
}
```
* Delete News --> method **DELETE**<br>
[https://rest-api-ku.herokuapp.com/api/news/delete/{id}](https://rest-api-ku.herokuapp.com/api/news/delete/{id})
* Filter by News Status --> method **GET**<br>
[https://rest-api-ku.herokuapp.com/api/news/filter/status/{status}](https://rest-api-ku.herokuapp.com/api/news/filter/status/{status})
* Filter News by its Topics --> method **GET**<br>
[https://rest-api-ku.herokuapp.com/api/news/filter/topik/{id_topik}](https://rest-api-ku.herokuapp.com/api/news/filter/topik/{id_topik})