class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        for (int n : nums){
            count[n]++;
        }

        //Now we need to find k most frequent ints - reorganize this into an array where wer can sort indices as count
        vector<vector<int>> freq(nums.size()+1);

        for (const auto& entry : count){
            freq[entry.second].push_back(entry.first);
        }

        vector<int> submission;
        //could either use freq.size()-1 or nums.size()+1;
        for (int i = freq.size()-1; i > 0; i--){
            for (int n : freq[i]){
                submission.push_back(n);
                //No need for variable to track k, just use this:
                if (submission.size() == k){
                    return submission;
                }
            }
        }
        return submission;
    }
};
