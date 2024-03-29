class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() != goal.size()){
            return false;
        }
        if ( s == goal && set<char>(s.begin(),s.end()).size() < s.size()){
            return true;
        }

        vector<int> diff; // store indexes of different 
        for (int i = 0;i < s.size();i++){
            if (s[i] != goal[i]){
                diff.push_back(i);
            }
        }
        return diff.size() == 2 && s[diff[0]] == goal[diff[1]] && s[diff[1]] == goal[diff[0]];
    }
};