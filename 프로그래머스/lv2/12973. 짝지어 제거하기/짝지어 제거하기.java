import java.util.*;

class Solution
{
    static Stack<Character> stack;
    
    public int solution(String s)
    {
        stack = new Stack<Character>();
        int answer = 0;
        
        // char[] t= s.toCharArray();
        for (char one :s.toCharArray()){
            if (stack.size()>0){
                if (stack.peek() == one){
                    stack.pop();
                }else{
                    stack.push(one);
                }
            }else{
                stack.push(one);
            }
            
        }

        return stack.size() > 0 ? 0 : 1;
    }
}