class Solution {
    static boolean[] visited;
    static int size;
    static int [][] d;
    static int answer;
    public void lec(int energy,int depth){
        answer = (answer < depth)? depth: answer;
        for (int i = 0; i < size; i ++ ){
            int[] oneD = d[i];
            if (!visited[i] && energy >= oneD[0] && energy>=oneD[1]){
                visited[i] = true;
                lec(energy - oneD[1], depth+1);
                visited[i] = false;
            }
        }
    }
    public int solution(int k, int[][] dungeons) {
        answer = -1;
        size = dungeons.length;
        d = dungeons;
        visited = new boolean[size];
        lec(k,0);
        return answer;
    }
}