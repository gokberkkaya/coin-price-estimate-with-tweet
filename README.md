# Coin Price Estimate With Tweet

This Flask API predicts the potential price change of a tweet based on its content and owner.

------

### API Endpoints

- **POST /api/get-tweet-estimate**: Used to estimate the impact of a tweet.
  - ###### Request Body:
    ```json
    {
        "tweet": "Tweet content",
        "tweet_owner": "Tweet owner"
    }
    ```
  - ###### Response:
    ######
    Indicates that the tweet is likely to increase the price
    ```json
    {
        "estimate": true
    }
    ```
    or
    ######
    Indicates that the tweet may not affect the price or could decrease it
    ```json
    {
        "estimate": false
    }
    ```
<br>

#### Install Requirements

```
pip install -r requirements.txt
```

#### Run App

```
python api.py
```
