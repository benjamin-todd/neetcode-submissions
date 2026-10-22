class Solution {
public:
    bool isPalindrome(string s) {
        std::string str = "";
        for (int i=0;i<s.length(); i++) {
            if (isalnum(s[i])) {
                str += tolower(s[i]);
            }
        }

        std::string strr = str;
        reverse(strr.begin(), strr.end());
        return str == strr;
    }
};