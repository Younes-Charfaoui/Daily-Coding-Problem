/*This problem was asked by Google.

Given a string, return the length of the longest palindromic subsequence in the string.

For example, given the following string:

MAPTPTMTPA
Return 7, since the longest palindromic subsequence in the string is APTMTPA. 
Recall that a subsequence of a string does not have to be contiguous!

Your algorithm should run in O(n^2) time and space.
*/

int longestPalindrome(string s) {
        int n = (int)s.size();
        if (!n) return 0;
        int ans_i = 1, ans_j = 0;
        int mx = 0;
        for(int i = 0; i < n; i++){
            int a = i, b = i;
            while (a - 1 >= 0 && b + 1 < n && s[a - 1] == s[b + 1]) a--, b++;
            if (b - a >= mx){
                mx = b - a;
                ans_i = a;
                ans_j = b;
            }
            a = i, b = i - 1;
            while (a - 1 >= 0 && b + 1 < n && s[a - 1] == s[b + 1]) a--, b++;
            if (b - a >= mx){
                mx = b - a;
                ans_i = a;
                ans_j = b;
            }
            
        }
        return mx + 1;
        
    }
