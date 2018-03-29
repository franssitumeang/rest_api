# REST API Python

This REST API develop with python(django_rest) and has been deployed to [heroku](https://www.heroku.com/)

## API Documentation
### Topic Management

* List Topic --> method **GET**<br>
[https://rest-api-ku.herokuapp.com/api/topic/list](https://rest-api-ku.herokuapp.com/api/topic/list)
* View Detail Topic --> method **GET**<br>
[https://rest-api-ku.herokuapp.com/api/topic/detail/{id}](https://rest-api-ku.herokuapp.com/api/topic/detail/3)
* Create Topic --> method **POST**<br>
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