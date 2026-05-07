class Solution:
    countup = 0
    countdown = 0
    def goup(self, map:{}) -> bool:
        self.curr_num1 += 1
        n = self.curr_num1
        if n in map:
            self.countup += 1
            return True
        else:
            False
    
    def godown(self, map:{}) -> bool:
        self.curr_num2 -= 1
        n = self.curr_num2
        if n in map:
            self.countdown += 1
            return True
        else:
            False    

    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        #populate the hashmap
        # 'i' is the index, 'num' is the value from nums
        for i, num in enumerate(nums):
            if num not in map:  # Check if the VALUE is already a key
                map[num] = i    # Store the VALUE as key, INDEX as value
        counts = []
        for num in nums:
            self.countup = 0
            self.countdown = 0
            self.curr_num1 = num
            self.curr_num2 = num
            while True:
                if not self.goup(map):
                    break
            while True:
                if not self.godown(map):
                    break
            print(f"countup for {num} is {self.countup}")
            print(f"countdown for {num} is {self.countdown}")
            counts.append(self.countup + self.countdown + 1)
    
        print(map)

        max = 0
        for count in counts:
            if count > max:
                max = count
        
        return max

