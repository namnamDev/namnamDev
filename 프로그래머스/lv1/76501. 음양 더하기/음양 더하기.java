class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int size = absolutes.length;
        for (int i = 0; i < size; i++){
            int temp = absolutes[i];
            if (signs[i] == false){
                temp *= -1;
            }
            answer += temp;
        }
        return answer;
    }
}