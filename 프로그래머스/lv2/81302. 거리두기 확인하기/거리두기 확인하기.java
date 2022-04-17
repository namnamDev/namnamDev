import java.util.*;
class Solution {
    static int[] dry = {-1,1,0,0};
    static int[] drx = {0,0,-1,1};
    public int find(String[][]parr){
        int[][] visit = new int[5][5];
        for (int y = 0; y <5;y++){
            for (int x = 0;x<5;x++){
                int pCnt= 0;
                int wy,wx;
                for (int d = 0; d<4;d++){
                    wy = y+dry[d];
                    wx = x+drx[d];
                    if (0 <= wy && wy<5 && 0 <= wx && wx < 5 && parr[wy][wx].equals("P")){
                        pCnt++;
                        }
                    }
                if (parr[y][x].equals("P") && pCnt>0){
                    return 0;
                }else if (parr[y][x].equals("O") && pCnt>1){
                    return 0;
                }
            }
        }
    return 1;
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        int cnt = 0;
        for (String[] placesOne:places){
            String[][] p = new String[5][5];
            for (int i = 0 ; i < 5; i++){
                p[i] = placesOne[i].split("");
                // System.out.println(Arrays.toString(p[i]));
            }
            answer [cnt] = find(p);
            cnt++;
        }
        return answer;
    }
}