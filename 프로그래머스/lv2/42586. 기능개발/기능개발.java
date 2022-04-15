import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int size = speeds.length;
        int[] workDay = new int[size];
        for (int i = 0; i < size; i++){
            int t = (100- progresses[i]);
            int tempCal = (int)(t / speeds[i]);
            if (t % speeds[i] >0) tempCal ++;
            workDay[i] = tempCal;
        }
        int cnt = 1;
        ArrayList<Integer> aa = new ArrayList<Integer>();
        
        int idx = 0;
        while (idx<size){
            int i;
            for (i = idx+1; i<size; i++){
                if (workDay[idx] < workDay[i]){
                    // System.out.println(i - idx);
                    aa.add(i - idx);
                    idx = i;
                    cnt ++;
                    break;
                }
            }
            if (i == size){
                // System.out.println(i - idx);
                aa.add(i - idx);
                break;
            }
        }
        int[] answer = new int[aa.size()];
        for (int i=0; i < aa.size(); i++){
            answer[i] = aa.get(i);
        }
        return answer;
    }
}