import twint
import asyncio
import json
import os
import uuid
from datetime import datetime, timedelta


class Tweet:
    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def hourAgo(hours: int = 1):
        last_hour_date_time = datetime.now() - timedelta(hours=1)
        return last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def minuteAgo(minutes: int = 5):
        last_hour_date_time = datetime.now() - timedelta(minutes=5)
        return last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S')

    def search(self, symbol: str, since: str, callback=None):
        # Configure
        c = twint.Config()
        # c.Username = "now"
        c.Since = since
        c.Search = symbol
        c.Store_json = True
        c.Output = str(uuid.uuid4()) + ".json"

        # Run
        asyncio.set_event_loop(asyncio.new_event_loop())
        twint.run.Search(c)

        # read one line at a time from a file
        asyncio.set_event_loop(asyncio.new_event_loop())
        with open(c.Output, "r") as f:
            for line in f:
                try:
                    tweet = json.loads(line)
                    data = {
                        "type": "TWEET",
                        "symbol": symbol,
                        "id": tweet["id"],
                        "username": tweet["username"],
                        "text": tweet["tweet"],
                        "created": tweet["created_at"],
                        "timezone": tweet["timezone"],
                        "likes": tweet["likes_count"],
                        "retweets": tweet["retweets_count"],
                        "replies": tweet["replies_count"],
                        "link": tweet["link"]
                    }
                    if callback:
                        callback(data)
                    else:
                        print(data)
                except Exception as e:
                    print(e)
                    continue  # skip this line
        os.remove(c.Output)

    def SearchTweets(self, symbol: str = None, since: str = None):
        if not symbol:
            symbol = self.symbol
        tweets = []
        if since is None:
            since = Tweet.minuteAgo(6)
        self.search(symbol, since, tweets.append)
        return tweets
