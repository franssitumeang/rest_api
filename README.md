# REST API Python

This REST API develop with python(django_rest) and has been deployed to [heroku](https://www.heroku.com/)

## API Documentation
### Topic Management

* **List Topic - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/topic/list](https://rest-api-ku.herokuapp.com/api/topic/list)
* **View Detail Topic - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/topic/detail/{id}](https://rest-api-ku.herokuapp.com/api/topic/detail/3)
* **Create Topic - <i>POST</i>**<br>
[https://rest-api-ku.herokuapp.com/api/topic/create](https://rest-api-ku.herokuapp.com/api/topic/create)

**body param**
```json
{
  "name": "topic_name" 
}
```
* **Update Topic - <i>PUT</i>**<br>
[https://rest-api-ku.herokuapp.com/api/topic/update/{id}](https://rest-api-ku.herokuapp.com/api/topic/update/{id})

**body param**
```json
{
  "name": "topic_name" 
}
```
* **Delete Topic - <i>DELETE</i>**<br>
[https://rest-api-ku.herokuapp.com/api/topic/delete/{id}](https://rest-api-ku.herokuapp.com/api/topic/delete/{id})

### News Management

* **List News - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/list](https://rest-api-ku.herokuapp.com/api/news/list)
* **View Detail News - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/detail/{id}](https://rest-api-ku.herokuapp.com/api/news/detail/3)
* **Create News - <i>POST</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/create](https://rest-api-ku.herokuapp.com/api/news/create)

**body param**
```json
{
  "title": "news_title",
  "status": "draft",
  "topic": [3,4] 
}
```
* **Update News - <i>PUT</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/update/{id}](https://rest-api-ku.herokuapp.com/api/news/update/{id})

**body param**
```json
{
  "title": "news_title",
  "status": "publish",
  "topic": [3,4] 
}
```
* **Delete News - <i>DELETE</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/delete/{id}](https://rest-api-ku.herokuapp.com/api/news/delete/{id})
* **Filter by News Status - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/filter/status/{status}](https://rest-api-ku.herokuapp.com/api/news/filter/status/{status})
* **Filter News by its Topics - <i>GET</i>**<br>
[https://rest-api-ku.herokuapp.com/api/news/filter/topic/{id_topic}](https://rest-api-ku.herokuapp.com/api/news/filter/topic/{id_topic})