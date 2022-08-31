class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = [0] * 60
        count = 0
        for i in range(len(time)):
            given_time = time[i] % 60
            matches = (60 - given_time) % 60
            count += freq[matches]
            freq[given_time] += 1
        return count
            