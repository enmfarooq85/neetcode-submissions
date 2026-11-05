class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();

        for (int i = 0; i < n; i++) {
            int complement = target - numbers[i];
            
            int start = i + 1;
            int end = n - 1;

            while (start <= end) {
                int mid = start + (end - start) / 2;

                if (numbers[mid] == complement) {
                    return {i + 1, mid + 1};
                }
                
                if (numbers[mid] < complement) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }

        return {-1, -1};
    }
};
