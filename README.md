# Semaphore-Detection-API 🔥
<details>
<summary> Documentation </summary>


test_url : `https://complete-goose-helping.ngrok-free.app`

Method: 
- POST 

URI: 
- {test_url}/classify_semaphore

Headers:
- Content-Type: multipart/form-data

Request Body: 
- `image` as `file`, must be a valid image, large size


Response:
```
{
    "confidence": 1.0,
    "predicted_class": "e"
}
```

*notes: for better classification, image should be taken potrait in camera or image size ratio should be 3:4

