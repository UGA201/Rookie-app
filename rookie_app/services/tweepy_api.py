import tweepy

api_key = 'e9VJ2E66qqfQcGWRW1k9CbKGY'
api_secret = 'qsbpDfNd0WPzL090qwKoFJcPFtWSsQiNQvvbZLrl1ujPUe7V0x'

access_token = '1372382199748567042-5cY2FjeWLZ9d0EtAGqg7esBHE8E94W'
access_secret = '3FT384NVPJCndU0WWqprUbMRUkug4cueQgKcAq7zeDn8B'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def get_tweets(group_name):
    """
    `get_tweets` 함수는 'group_name' 이 주어지면 tweepy 를 통해 해당 키워드를 검색결과로 하는 트윗들을 조회한 리스트를 리턴.
     - 한 그룹 당 10건을 가져오고, 검색결과는 'latest'를 기준으로 함
    """

    raw_tweets = api.search(group_name, count=3,
                            result_type='recent')
                                   
    return raw_tweets
