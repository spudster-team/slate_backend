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
    "last_name": "Fitahiana" 
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
