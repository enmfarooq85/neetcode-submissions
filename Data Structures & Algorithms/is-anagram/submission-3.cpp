class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> mp1;
        unordered_map<char, int> mp2;

        for (char &ch: s){
            mp1[ch]++;
        }

        for (char &ch: t){
            mp2[ch]++;
        }

        for (auto const &  [key, value]: mp1){
            if(mp2[key] !=mp1[key]){
                return false;
            }
        }

        return true;
    }
};
