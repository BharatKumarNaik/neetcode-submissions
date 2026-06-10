class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if we consider k as max of the piles
        # then it will take len(piles) hours to eat.
        if len(piles) == h:
            return max(piles)
        # Approach:
        # Iterate thorugh max(piles) - 1 as arb k value.
        # Till we find the lowest k which fit the constraint.
        # But this approach will take O(len(1 to max(piles))) time to find K.
        # if we notice here it's a sorted array [1 to max(piles)].
        # so in order to find the optimal k value which fits the constraint, 
        # we can use binary search tree
        i,j = 1,max(piles)
        k=max(piles)
        while i<=j:
            arb_k = (i+j)//2
            arb_h = 0
            for pile in piles:
                # print(pile)
                arb_h += (pile)//arb_k
                if pile%arb_k !=0:
                    arb_h+=1
                # print(arb_h,arb_k)

            if arb_h<=h:
                k = arb_k
                j = arb_k-1
            else:
                i = arb_k+1
        # print(i,j)
        return k