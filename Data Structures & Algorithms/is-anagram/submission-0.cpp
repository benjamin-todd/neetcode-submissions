class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> map1;
        std::unordered_map<char, int> map2;

        int n = s.length();
        if (n != t.length()) {
            return false;
        }
        for (int i=0;i<n;i++){
            char key1 = s.at(i);
            char key2 = t.at(i);
            map1[key1]++;
            map2[key2]++;
        }

        for (int i=0;i<n;i++) {
            char key = s.at(i);
            if (map1[key] != map2[key]) {
                return false;
            }
        }

        return true;
    }
};
