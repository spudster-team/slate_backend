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
[
  {
    "id": 19,
    "owner": "Nomeniavo Joe",
    "title": "J'ai une erreur de code avec python",
    "content": "voici",
    "date_posted": "2023-11-09T14:01:13.003538Z",
    "response": [],
    "tag": [],
    "up_vote": 0,
    "down_vote": 0,
    "n_response": 0,
    "photo": {
      "id": 8,
      "path": "https://slate-service-api.onrender.com/media/images/image_capture.png_1699538472.8806033.png"
    }
  }
]
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

---

### Get one Question

- **get**: /api/question/<id:question_id>

```json
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
  
```
---

### Delete Question

- **get**: /api/question/<int:question_id>
- **need authentication**:
- **Authorization**: `token d75dad1a0db1c2b01cfb3b67d0f68b1e7dda2ed8`
- 
- **response**: ```204 no content```
___
### Vote Question

**post**: /api/question/vote/<int:question_id>
- **need authentication**:
- **Authorization**: `token d75dad1a0db1c2b01cfb3b67d0f68b1e7dda2ed8`

- **body**:

```json
{
  "is_upvote": true
}
```
- **response**: ```200 ok```

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

### Response question

- **post**: /api/question/response/<int:question_id>
- **need authenticaiton**:

- **body**
```json
{
    "content": "",
    "photo": null
}

```
  
- **resposne**
```json
{
  "id": 19,
  "owner": {
    "id": 1,
    "email": "24email@gmail.com",
    "first_name": "Nomeniavo Joe",
    "last_name": "Fitahiana",
    "photo": {
      "path": null
    }
  },
  "title": "J'ai une erreur de code avec python",
  "content": "test",
  "date_posted": "19 hours, 21 minutes",
  "response": [
    {
      "id": 1,
      "owner": "Nomeniavo Joe",
      "content": "Essai resonse",
      "date_posted": "2023-11-10T09:22:35.713150Z",
      "up_vote": 0,
      "down_vote": 0,
      "photo": {
        "path": null
      }
    }
  ],
  "tag": [],
  "up_vote": 0,
  "down_vote": 1,
  "n_response": 1,
  "info": {
    "is_already_voted": true,
    "is_upvote": false
  },
  "photo": {
    "id": 11,
    "path": "https://slate-service-api.onrender.com/media/images/image_capture.png_1699590711.0925508.png"
  }
}
  ```
---
### Search Question

- **get**: /api/question?search=python
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
