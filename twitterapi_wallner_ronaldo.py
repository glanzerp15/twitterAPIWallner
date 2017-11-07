import tweepy
import time


def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api


def post_tweets():
    consumer_key = 'B'
    consumer_secret = 'L'
    access_token = '9'
    access_token_secret = 'h'

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)
    search_term = '#cr7'

    media_list = list()
    response = api.media_upload('picture.jpg')
    media_list.append(response.media_id_string)
    user_list = []
    while True:
        cursor = tweepy.Cursor(api.search, q=search_term, count=100)
        for item in cursor.items():
            tweet_author = item.author._json['screen_name']
            if tweet_author in user_list:
                print("User already in List " + tweet_author)
                continue
            else:
                print("new user " + tweet_author)
                user_list.append(tweet_author)
                api.update_status('@' + tweet_author + ' Football god Roman Wallner', item.id, media_ids=media_list)

            time.sleep(180)

if __name__ == '__main__':
    post_tweets()