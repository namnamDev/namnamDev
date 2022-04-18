import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int size = computers.length;
        int[] visit = new int[size];
        
        
        for(int i = 0;i<size; i++){
            if (visit[i] == 0){
                answer++;
                Queue<Integer> q = new LinkedList<Integer>();
                q.add(i);
                visit[i] = 1;
                while (!q.isEmpty()){
                    int now = q.poll();
                    int[]nowLine = computers[now];
                    for(int f = 0 ;f < size; f++){
                        if (nowLine[f] == 1 && visit[f] == 0){
                            visit[f] = 1;
                            q.add(f);
                        }
                    }
                }
            }
        }
        return answer;
    }
}