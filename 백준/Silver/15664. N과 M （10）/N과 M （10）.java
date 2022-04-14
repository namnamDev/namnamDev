import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
public class Main {
	private static int n, m;
	private static ArrayList<String> arr;
	private static HashMap<String, Integer> dic;
	private static ArrayList<String> forDfs;
	private static int arr_size; 
	public static void lec(int idx,int depth){
		if (depth == m){
			String an =  String.join(" ",forDfs);
			System.out.println(an);
			return;
		}
		for(int i = idx;i < arr_size; i++){
			String t = arr.get(i);
			if (dic.get(t) > 0){
				dic.put(t, dic.get(t) - 1);
				forDfs.set(depth, t);
				lec(i, depth + 1);
				dic.put(t, dic.get(t) + 1);
			} 
		}
	}
	public static void main(String[] args)   {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt(); 
    ArrayList<Integer> temp_arr = new ArrayList<>();
		dic = new HashMap<String,Integer>();
		for (int i = 0 ; i < n; i++) {
			String temp = sc.next();
			if (dic.get(temp) == null){
        temp_arr.add(Integer.valueOf(temp));
				dic.put(temp, 1);
			}else{
				dic.put(temp,(dic.get(temp)+1));
			}
		}
    Collections.sort(temp_arr);
    arr = new ArrayList<String>();
    for (int i: temp_arr){
      arr.add(Integer.toString(i));
    }

		arr_size = arr.size();
		forDfs = new ArrayList<String>();
		for (int i = 0; i < m ; i ++ ){
			forDfs.add("0");
		}
		lec(0,0);
    sc.close();
	}

}