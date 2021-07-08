package coTe.BOJ;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class NQueen {
   
   static int[][] arr;
   static int[][] visit;
   static int count = 0;
   public static void main(String[] args) throws IOException {

      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

      int N = Integer.parseInt(br.readLine());

      visit = new int [N][N];
      
      queen(N, 0);
      
      System.out.println(count);
      
   }

   public static void queen(int N, int depth) {
      
      int temp = 0;
      
      
      if(depth == N-1) {
         
         for( int i = 0; i < N; i++ ) {
            
            if(visit[N-1][i] ==0) {
               
               count ++;
               
            }
             
         }
         
         return;
      }
      
      for(int l = 0; l < N; l++) {
         
         if(visit[depth][l] > 0) {
            temp++;
         }
         
      }
      
      if(temp == N) {
         return;
      }
            
      for(int j = 0; j < N; j++) {
            
         if(visit[depth][j] == 0) {
            
            visit[depth][j]++;
            for( int k = 1; k < N - depth; k++ ) {
               
               
               visit[depth+k][j]++;
               if(j+k < N)
                  visit[depth+k][j+k]++;
               if(j-k >= 0)
                  visit[depth+k][j-k]++;
               
            }
            
            queen(N,depth+1);
            
            visit[depth][j]--;
            for( int k = 1; k < N - depth; k++ ) {
               
               visit[depth+k][j]--;
               
               if(j+k < N)
                  visit[depth+k][j+k]--;
               if(j-k >= 0)
                  visit[depth+k][j-k]--;
               
            }

         }
         
      }
      
   }
   
}