class Solution {
    static String[] word = {
      "zero", "one", "two", "three", "four", "five", "six" , "seven" , "eight", "nine"  
    };
    public int solution(String s) {
        int answer = 0;
        for (int i = 0; i < 10;i++){
            s = s.replaceAll(word[i],Integer.toString(i));
        }
        answer = Integer.valueOf(s);
        return answer;
    }
}