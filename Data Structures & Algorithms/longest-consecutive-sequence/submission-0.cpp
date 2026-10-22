class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(),nums.end());

        int c = 1;
        int max = 0;
        for (int i=0;i<nums.size() - 1;i++) {
            if (nums[i] + 1 == nums[i+1]) {
                c++;
            } else if (nums[i] == nums[i+1]) {
                continue;
            } else {
                max = std::max(max , c);
                c = 1;
            }
        }
        if (c >= max) {
            return c;
        }
        return max;
    }
};
