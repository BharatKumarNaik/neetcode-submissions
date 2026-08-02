class Twitter:

    def __init__(self):
        self.data={} # UserId:{Tweets:[(-time,TweetID1)],followers:[]}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.data:
            self.data[userId]={"tweets":[],"followers":[]}
        self.data[userId]["tweets"].append((-self.time,tweetId))
        print("Post",self.data)

    def getNewsFeed(self, userId: int) -> List[int]:
        # 10 most recent tweets, includes tweet from the followers
        allRelevantTweets=self.data[userId]['tweets'].copy()
        followers=self.data[userId]['followers']
        for uid in followers:
            allRelevantTweets.extend(self.data[uid]['tweets'])
        allRelevantTweets=list(set(allRelevantTweets))
        heapq.heapify(allRelevantTweets)
        TopTweets=[]
        i=0
        while allRelevantTweets and i<10:
            t,tweet=heapq.heappop(allRelevantTweets)
            TopTweets.append(tweet)
            i+=1
        print("New feeds",TopTweets)
        return TopTweets
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.data:
            self.data[followerId]={"tweets":[],"followers":[]}
        if followeeId not in self.data[followerId]['followers']:
            self.data[followerId]['followers'].append(followeeId)
        print("follow",self.data)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.data[followerId]['followers']:
            self.data[followerId]['followers'].remove(followeeId)
        print("unfollow",self.data)

