import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        Set<Integer> aa = new HashSet<Integer>();
        for (int wins:win_nums){
            aa.add(wins);
        }
        int cnt = 0;
        int zeroCnt = 0;
        for (int fir: lottos){
            if (fir == 0){
                zeroCnt ++;
            } else if(aa.contains(fir)){
                cnt ++;
            }
        }
        int [] t = {6,6,5,4,3,2,1};
        return new int[]{t[cnt+zeroCnt],t[cnt]};
    }
}