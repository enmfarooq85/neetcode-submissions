class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;

        for(int  &  num : nums){
            mp[num]++;
        }

        for(auto const& [key, value] : mp){
            if (value >= 2){
                return true;
            }
        }

        return false;
    }
};