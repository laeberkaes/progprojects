import java.lang.Math;
import java.util.*;

public class AB3 {
    public static int[] list (int ... nums) {
        return nums;
    }

    public static double nah(int n) {
        double sum = 0.0;
        for (double i = 1; i<=n; i++) {
            sum += 1/Math.pow(i,3.0);
        }
        return sum;
    }

    public static double pi(int n) {
        double sum = 0.0;
        for (double i = 1; i<=n; i++) {
            sum += Math.sqrt((1/(Math.pow(i,2)))*6);
        }
        return Math.sqrt(sum);
    }

    public static double pi2(int n) {
        double sum = 0;
        for (double i = 0; i<n; i++) {
            sum+=(1/Math.pow(16,i))*((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)));
        }
        return sum;
    }

    public static List<String> words() {
        List<String> wordlist = new ArrayList<>();
        char[] alph = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        char[] kons = "aeiou".toCharArray();
        int i = 0;
        for (char a : alph) {
            for (char b : alph) {
                for (char c : kons) {
                    for (char d : alph) {
                        wordlist.add(String.valueOf(a)+String.valueOf(b)+String.valueOf(c)+String.valueOf(d));
                        i++;
                    }
                }
            }
        }
        return wordlist;
    }

    public static void dicts() {
        Dictionary dictionary = new Hashtable();

        dictionary.put("Dog","Barks");
        dictionary.put("Cat",2);
        System.out.println(dictionary.keys());
    }
}
