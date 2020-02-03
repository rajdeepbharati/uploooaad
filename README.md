# uploooaad

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
paused at row 12/26
```
