class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        vector<vector<string>> v;
        for (int i=0;i < strs.size(); i++) {
            bool t = true;
            int b = 0;
            string s = strs[i];
            sort(s.begin(),s.end());
            while (t && b<v.size()) {
                for (int j=0;j<v[b].size();j++){
                    string a = v[b][j];
                    sort(a.begin(),a.end());
                    if (s == a) {
                        v[b].push_back(strs[i]);
                        t = false;
                        break;
                    }
                }
                b++;
            }
            if (t == true) {
                v.push_back({strs[i]});
            }
        }
        return v;
    }
};
