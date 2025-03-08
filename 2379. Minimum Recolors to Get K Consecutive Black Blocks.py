# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        res=100000
        for i in range(n-k+1):
            x=0
            for j in blocks[i:i+k]:
                if j=='W':
                    x+=1
            res=min(res,x)
        return res
