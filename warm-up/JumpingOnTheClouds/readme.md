# Hacker Rank - Warm-up Challenges
**Challenge**: Jumping on the clouds
**Goal:** Based on an array find the best number of jumps to avoid hitting a bad cloud (1)

**Link**: https://bit.ly/3goh6oU

The challenge is always solvable, this means you will not find an scenario where [0,1,0,1,1,0]
Knowing this, followed up a guess strategy in which always checked for two indexes ahead (less jumps), if value: 1 is found
reduce the index to 1 and iterate until reaching the end of the array
