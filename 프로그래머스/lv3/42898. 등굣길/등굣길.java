class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dp = new int[n][m];
        for (int[]p :puddles){
            dp[p[1]-1][p[0]-1] = -1;
        }
        for (int y = 1; y < n; y++){
            if (dp[y][0]==0){
                dp[y][0] = 1;
            }else{
                break;
            }
        }
        for (int x = 1; x < m; x++){
            if (dp[0][x]==0){
                dp[0][x] = 1;
            }else{
                break;
            }
        }
        for(int y = 1; y < n ; y++){
            for (int x = 1;x < m ; x++){
                if (dp[y][x] != -1){
                    if (dp[y-1][x] == -1){
                        dp[y][x]++;
                    }
                    if (dp[y][x-1]==-1){
                        dp[y][x]++;
                    }
                    dp[y][x] += (dp[y-1][x] + dp[y][x-1])% 1000000007;

                }
            }
        }
        
        return dp[n-1][m-1] % 1000000007;
    }
}