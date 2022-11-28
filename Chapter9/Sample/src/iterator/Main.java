package iterator;

public class Main {
    public static void main(String[] args) {
        Waitress waitress = new Waitress(new ACafeMenu(), new BCafeMenu());
        waitress.printMenu();
    }
}
