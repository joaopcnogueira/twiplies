twiplies
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

`pip install twiplies`

## How to use

``` python
from twiplies.core import Twiplies
```

``` python
robot = Twiplies(
    username='joaopcnogueira',
    consumer_key="<your-consumer-key>", 
    consumer_secret="<your-consumer-secret>", 
    access_token="<your-access-token>", 
    access_token_secret="<your-access-token-secret>"
)
```

``` python
robot.get_replies_from_tweet(tweet_id='1549897550953603074')
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tweet_original</th>
      <th>tweet_replies</th>
      <th>tweet_user</th>
      <th>tweet_location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1549897550953603074</td>
      <td>@joaopcnogueira Novo qteste do tweet</td>
      <td>mamede86</td>
      <td>São Paulo, Brasil</td>
    </tr>
  </tbody>
</table>
</div>
