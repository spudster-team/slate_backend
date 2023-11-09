# Slate Backend

## The Documentation is Coming Soon

### Register

- **post**: /api/user
- **body**:

```json
{
  "email": "24email@gmail.com",
  "password": "strong_password",
  "first_name": "Nomeniavo Joe",
  "last_name": "Fitahiana",
  "photo": null
}
```

- **response**: ```201 created```

```json
{
  "user": {
    "id": 1,
    "email": "24email@gmail.com",
    "first_name": "Nomeniavo Joe",
    "last_name": "Fitahiana",
    "photo": null
  },
  "token": "d75dad1a0db1c2b01cfb3b67d0f68b1e7dda2ed8"
} 
```

___

### Login

- **post**: /api/user/auth
- **body**:

```json
{
  "email": "24email@gmail.com",
  "password": "strong_password"
}
```

- **response**: ```200 ok```

```json
{
  "user": {
    "id": 1,
    "email": "24email@gmail.com",
    "first_name": "Nomeniavo Joe",
    "last_name": "Fitahiana",
    "photo": null
  },
  "token": "d75dad1a0db1c2b01cfb3b67d0f68b1e7dda2ed8"
} 
```

___

### Add Question

- **post**: /api/question
- **need authentication**:
- **Authorization**: `token d75dad1a0db1c2b01cfb3b67d0f68b1e7dda2ed8`
- **body**:

```json
{
  "title": "Comment résoudre une équation à 3 inconnue ?",
  "content": "Quelqu'un peut-il m'aider?",
  "photo": null
}
```

- **response**: ```201 created```

```json
```

___

### Get All Question

- **get**: /api/question

```json
[
    {
        "id": 19,
        "owner": "Nomeniavo Joe",
        "title": "J'ai une erreur de code avec python",
        "content": "voici",
        "date_posted": "2023-11-09T14:01:13.003538Z",
        "response": [],
        "tag": [],
        "up_vote": 1,
        "down_vote": 0,
        "n_response": 0,
        "info": {
            "is_already_voted": true,
            "is_upvote": true
        },
        "photo": {
            "id": 8,
            "path": "https://slate-service-api.onrender.com/media/images/image_capture.png_1699538472.8806033.png"
        }
    }
]
```