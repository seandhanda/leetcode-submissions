class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #    approach 1 - using array = inefficient
        #  check = []
         
        #  for x in nums:
        #     if x in check:
        #         return True
        #     check.append(x)
        #  return False


# 2nd approach - using dict (or hashtable)
        # check = {}

        # for x in nums:
        #     if x in check:
        #         return True
        #     check[x] = True
        # return False

    # approach 3 - using set, equally efficient (implemented using hashtable)
        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False