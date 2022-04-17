class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 1;
        while(i <= n){
            if (n%i== 0){
                answer += i;
                // answer += (int)n/i;   
            }
            i++;
        }
        return answer;
    }
}