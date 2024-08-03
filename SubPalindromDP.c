#include <stdio.h>
#include <string.h>

int longestPalindrom(char str[]) {
    int len = strlen(str);
    int dp[len][len];
    
 
    for (int i = 0; i < len; i++) {
        dp[i][i] = 1;
    }
    
   
    for (int cl = 2; cl <= len; cl++) { 
        for (int i = 0; i < len - cl + 1; i++) { 
            int j = i + cl - 1;
            
            if (str[i] == str[j] && cl == 2) {
                dp[i][j] = 2;
            } else if (str[i] == str[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = (dp[i][j - 1] > dp[i + 1][j]) ? dp[i][j - 1] : dp[i + 1][j];
            }
        }
    }
    
    
    return dp[0][len - 1];
}

int main() {
    char str[] = "AYANOCHOCHI";
    printf("Length of Longest Palindromic Subsequence is %d\n", longestPalindrom(str));
    return 0;
}
