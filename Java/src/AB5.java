import javax.print.DocFlavor;
import java.util.ArrayList;
import java.util.List;

public class AB5 {
    public static class Person {
        String lname;
        String fname;
        int age;
        int size;
        List<Person> friendsList = new ArrayList<>();

        public Person(String ln, String fn, int ag, int s) {
            lname=ln;
            fname=fn;
            age=ag;
            size=s;
        }

        public void getOlder() {
            age++;
        }

        public boolean isBaby() {
            return age <= 1;
        }

        public void newFriend (Person f) {
            friendsList.add(f);
        }

        public List<Person> friends () {
            return friendsList;
        }

        public String oldestFriend () {
            String oldest = "";
            int old = 0;

            for (Person friend : friendsList) {
                if (friend.age > old) {
                    oldest = friend.fname;
                    old = friend.age;
                }
            }
            return oldest;
        }
    }

    public static class Pupil extends Person {
        int matr;
        String school;

        public Pupil(String ln, String fn, int ag, int s, int m, String sch) {
            super(ln, fn, ag, s);
            matr = m;
            school = sch;

        }
    }

    Pupil pup = new Pupil("Pan","Peter",19,158,123456,"Albstadt");
}
