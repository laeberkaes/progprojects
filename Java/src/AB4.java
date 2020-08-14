import java.util.ArrayList;
import java.util.List;

public class AB4 {
    public static boolean prim (int i) {
        boolean check = true;
        for (int k = 2; k<((i/2)+1); k++) {
            if (i%k==0) {
                check=false;
                break;
            }
        }
        return check;
    }
    public static List<Integer> twins() {
        List<Integer> twinList = new ArrayList<>();
        for (int i = 2; i<10001; i++) {
            if (prim(i) && prim(i+2)) {
                twinList.add(i);
            }
        }
        return twinList;
    }
}
