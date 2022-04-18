import java.util.*;
class Solution {
    static HashMap<String,Integer> map;
    static int wordSize;
    public boolean check(String fir ,String sec){
        int an = 0;
        
        for (int i = 0; i < wordSize; i++){
            if (fir.charAt(i) != sec.charAt(i)){
                an++;
            }
            if (an>1){
                return false;
            }
        }
        return true;
    }
    public int solution(String begin, String target, String[] words) {
        map = new HashMap<String,Integer>();
        int size = words.length;
        wordSize = words[0].length();
        int[][]board = new int[size][size];
        
        int targetIdx = -1;
        for (int i = 0 ; i < size;i++){
            map.put(words[i],i);
            if (words[i].equals(target)){
                targetIdx = i;
            }
        }
        if (targetIdx == -1){
            return 0;
        }
        
        for(int i = 0; i < size; i++){
            for (int f = i + 1; f< size; f++){
                if(check(words[i],words[f])){
                    board[i][f] = 1;
                    board[f][i] = 1;
                }
            }
        }
        // for(int[]t : board){
        //     System.out.println(Arrays.toString(t));
        // }
        
        
        int[] visited = new int[size];
        Queue<Integer> q = new LinkedList<Integer>();
        for (int i =0;i < size;i++){
            if (check(begin,words[i])){
                visited[i]++;
                q.add(i);
            }
        }
        // System.out.println(q);
        while (!q.isEmpty()){
            // System.out.println(q);
            Integer n = q.poll();
            
            if(visited[targetIdx]>0){
                break;
            }
            int[] nowLine = board[n];
            for (int i = 0;i<size;i++){
                if (nowLine[i] > 0 && visited[i] ==0 && check(words[n],words[i])){
                    visited[i] = visited[n]+1;
                    q.add(i);
                }
            }
        }
        // System.out.println(Arrays.toString(visited));
        int answer = visited[targetIdx];
        return answer;
    }
}