import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i = 0; i < commands.length;i++){
            int[] oneLine = commands[i];
            ArrayList<Integer> temp = new ArrayList<Integer>();
            System.out.printf("%d, %d",oneLine[0]-1,oneLine[1]-1);
            for (int j = oneLine[0]-1; j < oneLine[1]; j++){
                temp.add(array[j]);
            }
            Collections.sort(temp);
            answer[i]= temp.get(oneLine[2]-1);
        }
        return answer;
    }
}