import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // int i = 0, f = 0;
        // System.out.printf("%d,%d", i, f);
        HashMap<String,Integer> parts = new HashMap<String,Integer>();
        for(String p : participant){
            if (parts.get(p) == null){
                parts.put(p,1);
            }else{
                parts.put(p, parts.get(p)+1);
            }
        }
        String answer = "";
        for (String c : completion){
            if (parts.get(c) != null){
                parts.put(c,parts.get(c) - 1);
                if (parts.get(c) == 0){
                    parts.remove(c);
                }
            }
        }
        for (String a : parts.keySet()){
            answer = a;
        }

        return answer;
    }
}