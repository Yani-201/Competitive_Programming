class Solution:
    def numberOfWays(self, s: str) -> int:
        track = defaultdict(int)
        count_01 = [0]*len(s)
        count_10 = [0]*len(s)
        prefix = [0]*len(s)
        acc = 0
        for i in range(len(s)):
            acc += int(s[i])
            prefix[i] = acc
            if s[i] == '1':
                track[1] += 1
                count_01[i] = track[0]
            else:
                track[0] += 1
                count_10[i] = track[1]
        # print(count_01, count_10, prefix)

        valid = 0
        zeros = len(s) - prefix[-1]
        for idx in range(len(s)):
            num_zeros = zeros - (idx+1-prefix[idx])
            # print("0s", num_zeros)
            num_ones = prefix[-1] - prefix[idx]
            # print("1s", num_ones)
            valid += num_zeros * count_01[idx]
            valid += num_ones * count_10[idx]
        return valid

        