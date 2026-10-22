class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> map;

        for (int i=0;i<nums.size();i++) {
            int key = nums[i];

            if (map.count(key) == 0) {
                map[key] = false;
            } else {
                map[key] = true;
            }
        }

        for (int i=0;i<nums.size();i++) {
            int key = nums[i];
            if (map[key] == true) {
                return map[key];
            }
        }

        return false;
    }
};