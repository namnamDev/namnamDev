class Solution {
    static String pivot;
    static int answer;
    static String[] words = {"A","E","I","O","U"};
    static int cnt;
    public void lec(String pArr){
        if (pArr.equals(pivot)){
            answer = cnt;
            return;
        }
        if (pArr.length() == 5){
            return;
        }
        for (String a :words){
            cnt++;
            lec(pArr+a);
        }
        
        
    }
    public int solution(String word) {
        pivot = word;
        answer = 0;
        cnt = 0;
        lec("");
        return answer;
    }
}