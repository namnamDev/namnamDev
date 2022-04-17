import java.util.*;

class Solution {
    static ArrayList<ArrayList<Integer>> tree;
    public int solution(int n, int[][] wires) {
        tree = new ArrayList<ArrayList<Integer>>();
        int answer = n;
        for(int i = 0; i < n+1; i ++){
            ArrayList<Integer> node = new ArrayList<Integer>();
            tree.add(node);
        }
        
        for (int[] a :wires){
            ArrayList<Integer> temp = new ArrayList<Integer>();
            int s = a[0];
            int e = a[1];
            tree.get(s).add(e);
            tree.get(e).add(s);
        }
        for (int[] a : wires){
            Queue<Integer> queue = new LinkedList<Integer>();
            queue.add(1);
            int []visit= new int[n+1];
            visit[1] = 1;
            while (!queue.isEmpty()){
                Integer now = queue.poll();
                ArrayList<Integer> nowLine = tree.get(now);
                for (Integer node: nowLine){
                    if (visit[node] == 0 && !(now == a[0] && node == a[1]) && 
                        !(now == a[1] && node == a[0])){
                        visit[node] = visit[now] + 1;
                        queue.add(node);
                    }
                }
            }
            // System.out.println(Arrays.toString(a));
            // System.out.println(Arrays.toString(visit));
            int cnt = 0;
            for (int i = 1 ; i < n+1;i++){
                if (visit[i]>0) cnt++;
            }
            int Zcnt = n- cnt;
            int aa = Math.abs(cnt-Zcnt);
            // System.out.println(aa);
            answer = (answer > aa)? aa:answer;
        }
        // System.out.println(tree);
        return answer;
    }
}