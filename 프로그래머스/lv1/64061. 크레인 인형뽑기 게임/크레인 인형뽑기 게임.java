import java.util.*;

class Solution {
    static int size;
    static Stack<Integer> stack;
    static int[][] bBoard;
    static int cnt;
    public Integer search(int num){
        int res = 0;
        for (int y = 0; y< size; y++){
            if (bBoard[y][num] > 0){
                res = bBoard[y][num];
                bBoard[y][num] = 0;
                break;
            }
        }
        return res;
    }
    public void doStack(int num){
        if (stack.size() == 0){
            stack.push(num);
        }else if (stack.peek() == num){
            stack.pop();
            cnt += 2;
        } else{
             stack.push(num);
        }
    }
    public int solution(int[][] board, int[] moves) {
        stack = new Stack<Integer>();
        size = board.length;
        cnt = 0;
        bBoard = board;
        for (int i : moves){
            int temp = search(i-1);
            if (temp > 0) doStack(temp);
        }
        int answer = cnt;
        return answer;
    }
}