# coin-price-estimate-with-tweet

This Flask API predicts the potential price change of a tweet based on its content and owner.

## Usage

### API Endpoints

- **POST /api/get-tweet-estimate**: Used to estimate the impact of a tweet.
  - Request Body:
    ```json
    {
        "tweet": "Tweet content",
        "tweet_owner": "Tweet owner"
    }
    ```
  - Response:
    ```json
    {
        "estimate": true  # Indicates that the tweet is likely to increase the price
    }
    ```
    or
    ```json
    {
        "estimate": false  # Indicates that the tweet may not affect the price or could decrease it
    }
    ```
<br>

#### Install Requirements

```
pip install -r requirements.txt
```

#### Run App

```
python run.py
```
