# Predict API

Prosty serwis predykcyjny.

## Endpoint

`GET /api/v1.0/predict?num1=3.1&num2=4.0`

### Zwraca:

```json
{
  "features": {
    "num1": 3.1,
    "num2": 4.0
  },  
  "prediction": 1
}
