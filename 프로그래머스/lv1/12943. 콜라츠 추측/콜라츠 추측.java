class Solution {
    public int solution(int num) {
        long answer = num;
        int c;
        for (c = 0 ; c<500;c++){
            if (answer == 1){
                return c;
            }
            if (answer%2 == 0){
                answer /=2;
            }else{
                answer *= 3;
                answer ++;
            } 
        }
        
        return -1;
    }
}