import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;
import java.security.SecureRandom;

public class AB2 {
    public static void lower(String s) {
        if (s.startsWith("A")) {
            System.out.println("a" + s.substring(1,s.length()));
        }
    }
    public static void rate() {
        SecureRandom rand = new SecureRandom();
        Scanner antwort = new Scanner(System.in);
        int randint = rand.nextInt(101);
        int c = 0;

        while (true) {
            ++c;
            System.out.println("Gib eien Zahl ein: ");
            int ant = antwort.nextInt();

            if (ant==randint) {
                System.out.println("Richtige Zahl wurde mit " + c + " Versuchen gefunden.");
                break;
            }
            else if (ant<randint) {
                System.out.println("Zu klein!");
            }

            else if (ant>randint) {
                System.out.println("Zu groß!");
            }
        }
    }
    public static void ratespielOwn() {
        Scanner antwort = new Scanner(System.in);
        int max = 100;
        int min = 0;

        while (true) {
            SecureRandom rand = new SecureRandom();
            int randint = rand.nextInt(max-min+1)+min;
            System.out.println("Ist deine Zahle die " + randint + "?");
            System.out.println("zu groß/zu klein/richtig?");
            String antstr = antwort.nextLine();
            if ("zu groß".equalsIgnoreCase(antstr)) {
                max = randint;
            }
            else if ("zu klein".equalsIgnoreCase(antstr)) {
                min = randint;
            }
            else if ("richtig".equalsIgnoreCase(antstr)) {
                System.out.println("Super Sache!");
                break;
            }
        }
    }
}