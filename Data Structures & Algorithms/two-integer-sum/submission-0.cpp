class Solution {
public:
    //Running Time: O(n) iteration through nums once!
    //Space Complexity: O(n) worst case where second index is at nums' last index and list grows to size of nums.size()-1
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> list;

        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];

            if(list.count(diff)){
                return {list[diff], i};
            }
            else list.insert({nums[i], i});
        }
    }
};
