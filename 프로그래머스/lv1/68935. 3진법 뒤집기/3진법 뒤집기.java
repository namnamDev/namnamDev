class Solution {
    public int solution(int n) {
        int answer = 0;
        String num = "";
        while (n > 0){
            num += Integer.toString(n % 3);
            n = (int)n/3;
        }
        int idx = num.length()-1;
        for (char one : num.toCharArray()){
            answer += ((int)Math.pow(3, idx))*(Integer.valueOf(one)-48);
            idx --;
        }
        System.out.println(num);
        return answer;
    }
}