import java.util.*;

class Solution {
    static final char[] SDT = {'S','D','T'};
    static ArrayList<Integer> scores;
    public int solution(String dartResult) {
        int answer = 0;
        char[] splited  = dartResult.toCharArray();
        String temp = Character.toString(splited[0]);
        String score = temp;
        scores= new ArrayList<Integer>();
        scores.add(0);
        scores.add(0);
        for (int i = 1; i < splited.length; i++){
            char t = splited[i] ;
            if (!('0' <= t && t<='9')){//숫자가 아닐때
                Integer tempScore= null;
                for (int sdt = 0; sdt<3;sdt++){
                    if (SDT[sdt] ==t){
                        tempScore = (int)Math.pow(Integer.valueOf(score),sdt+1);
                    } 
                }
                if (tempScore != null){
                    scores.add(tempScore);
                    tempScore = null;
                    score = "";
                    continue;
                }
                int before = scores.get(scores.size()-1);
                if(t == '#'){
                    scores.set(scores.size()-1,before*-1);
                }else if (t == '*'){
                    int bbefore = scores.get(scores.size()-2);
                    scores.set(scores.size()-1, before*2);
                    scores.set(scores.size()-2, bbefore*2);
                }
            }else{
                score += Character.toString(t);
                //숫자일때
            }
        }
        for (Integer s : scores){
            answer += s;
        }
        // System.out.println(scores);
        return answer;
    }
}