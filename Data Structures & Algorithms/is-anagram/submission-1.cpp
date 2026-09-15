class Solution {
public:
    //Runtime = O(1) + O(1) + O(1) + O(n) + O(1) = O(n) time complexity
    //Space Complexity = O(2n) = O(n) for 2 hash maps on top of both s and t char[]
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> countS;
        unordered_map<char, int> countT;
        
        //Not for (char c : s) or for(char c : t) because we want to do it for both at same time
        for (int i = 0; i < s.length(); i++){
            countS[s[i]]++;
            countT[t[i]]++;
        }

        return (countS == countT);

    }
};
