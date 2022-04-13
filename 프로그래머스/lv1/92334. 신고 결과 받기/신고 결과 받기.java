import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int id_size = id_list.length;
        int[] answer = new int[id_size];
        
        int[][] an = new int[id_size][id_size];
        HashMap<String, Integer> dic= new HashMap<String,Integer>();
        for (int i = 0; i < id_size;i++){
            dic.put(id_list[i],i);
        }
        for(String test:report){
            String[] splited = test.split(" ");
            an[dic.get(splited[1])][dic.get(splited[0])] = 1;
        }
        for (int[] i:an){
            int cnt = 0;
            ArrayList<Integer>temp = new ArrayList<>();
            for (int ii = 0; ii<id_size; ii++){
                if (i[ii] == 1){
                    cnt ++;
                    temp.add(ii);
                }
            }
            if (cnt >= k){
                for(int t:temp){
                    answer[t] ++;
                }
            }
        }
        return answer;
    }
}