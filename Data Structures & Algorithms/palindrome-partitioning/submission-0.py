class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # aab 
        # [a,a,b] [aa,b]
        #                                 aab
        #(parse)          a               aa                     aab
        #(reminder)      ab                b                     None
        #(parse)     a        ab           b                     None
        #(reminder)  b        None       None                    None
        #(parse)     b        None       None                    None

        res=[]
        def backTracking(st,part):
            # st reached the end of the string
            if len(s)==st:
                res.append(part.copy())
                return

            for ed in range(st+1,len(s)+1):
                current=s[st:ed]
                if current==current[::-1]:
                    part.append(current)
                    # backTrack the reminder
                    backTracking(ed,part)
                    part.pop()
        backTracking(0,[])
        return res