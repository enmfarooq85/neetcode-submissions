class Solution {
   public:
    int maxArea(vector<int>& heights) {
        int lB = 0;
        int rB = heights.size() - 1;
        int ans = INT_MIN;
        while (lB < rB) {
            int width = rB - lB;
            int height = min(heights[lB], heights[rB]);
            int currWater = height * width;
            ans = max(currWater, ans);

            heights[lB] < heights[rB] ? lB++ : rB--;
        }

        return ans;
    }
};
