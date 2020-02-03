# uploooaad

## Getting Started using Docker

```sh
docker-compose up
```

Send the http requests using curl or Postman (sample data file `data.csv` is provided in repository).

To view the mongodb collection:

```sh
docker exec -it uploooaad_mongodb mongo # open mongo shell
use uploooaad # select database
show collections
db.uploadtest.count() # number of rows in uploaded data file
db.uploadtest.find() # show all the rows in this file
```

## APIs: Sample request/response

### `POST /upload`

#### request:

```sh
curl --location --request POST 'http://127.0.0.1:5000/upload?file=data.csv' --form 'file=@/Users/rajdeep/uploooaad/data.csv'
```

#### response:

```json
{
  "Message": "Succesfully added file to database",
  "code": "1",
  "status": "success"
}
```

### `POST /pause`

#### request:

```sh
curl --location --request POST 'http://127.0.0.1:5000/pause'
```

#### response:

```sh
paused at row 12/26
```

### `POST /resume`

#### request:

```sh
curl --location --request POST 'http://127.0.0.1:5000/resume'
```

#### response:

```sh
resumed from row 12/26
```
