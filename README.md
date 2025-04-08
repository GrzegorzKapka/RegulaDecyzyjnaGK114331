# Predict API

Prosty serwis predykcyjny.

## Endpoint

`GET /api/v1.0/predict?x=3.1&y=4.0`

### Zwraca:

```json
{
  "prediction": 1,
  "features": {
    "x": 3.1,
    "y": 4.0,
    "sum": 7.1
  }
}
