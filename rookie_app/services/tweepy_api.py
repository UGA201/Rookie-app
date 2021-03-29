import tweepy

api_key = '6cfRJZasFXbSieAlecgxEmq4a'
api_secret = 'Tss8Sn4lkL8TjahC3Vu8MtbXqp79CiV3454r6TLRiKLWVAetIr'

access_token = '1372382199748567042-U0Ia3vsMhpkuLjkNwNdf3lrpR187pF'
access_secret = 'j1KvxfVyWHkFldGVYLrUzrwPYiRtgG2NRmldyOSvzP6gm'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def get_tweets(group_name):
    """
    `get_tweets` 함수는 'group_name' 이 주어지면 tweepy 를 통해 해당 키워드를 검색결과로 하는 트윗들을 조회한 리스트를 리턴.
     - 한 그룹 당 10건을 가져오고, 검색결과는 'latest'를 기준으로 함
    """

    raw_tweets = api.search(group_name, count=100, 
                            result_type='latest')
                                   
    return raw_tweets
