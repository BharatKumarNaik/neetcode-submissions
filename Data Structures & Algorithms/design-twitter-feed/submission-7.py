class Twitter:

    def __init__(self):
        self.data={} # UserId:{Tweets:[(-time,TweetID1)],followers:[UID]}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.data:
            self.data[userId]={"tweets":[],"followers":{userId}}
        self.data[userId]["tweets"].append((-self.time,tweetId))
        print("Post",self.data)

    def getNewsFeed(self, userId: int) -> List[int]:
        # 10 most recent tweets, includes tweet from the followers
        # Instead of collecting all the tweets from followers
        # we know last element in tweets is the latest tweet done by each follower
        # so, we will store only the latest post done by users in the heap
        # we start looking at the latest post out of all the other users.
        # then iteratively push the next tweet of latest user into heap.
        # if that's also the latest among existing user's tweet it automatically come up, if not other user's tweet will come up in a heap
        minHeap=[]
        followers=self.data[userId]['followers']
        for uid in followers:
            index=len(self.data[uid]['tweets'])-1
            if index>=0:
                latestTime,latestTweet=self.data[uid]['tweets'][index]
                heapq.heappush(minHeap,(latestTime,latestTweet,uid,index))
        # minHeap has all the user's latest tweet
        i=0
        topTweets=[]
        while minHeap and i<10:
            i+=1
            time,tweet,uid,index=heapq.heappop(minHeap)
            topTweets.append(tweet)
            index-=1
            if index>=0:
                # there are some tweets in this uid
                latestTime,latestTweet=self.data[uid]['tweets'][index]
                heapq.heappush(minHeap,(latestTime,latestTweet,uid,index))

        print("New feeds",topTweets)
        return topTweets
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.data:
            self.data[followerId]={"tweets":[],"followers":{followerId}}
        self.data[followerId]['followers'].add(followeeId)
        print("follow",self.data)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        if followeeId in self.data[followerId]['followers']:
            self.data[followerId]['followers'].remove(followeeId)
        print("unfollow",self.data)

