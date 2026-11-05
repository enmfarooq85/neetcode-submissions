class Solution {
   public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> bucket(nums.size() + 1);

        unordered_map<int, int> frequencyMap;

        for (int n : nums) {
            frequencyMap[n]++;
        }

        for (auto& [key, frequency] : frequencyMap) {
            bucket[frequency].push_back(key);
        }

        vector<int> topK;

        for (int pos = bucket.size() - 1; pos >= 0 && topK.size() < k; pos--) {
            if (!bucket[pos].empty()) {
                for (int num : bucket[pos]) {
                    topK.push_back(num);

                    if (topK.size() == k) {
                        break;
                    }
                }
            }
        }

        return topK;
    }
};
