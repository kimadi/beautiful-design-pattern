package adaptor;

class Client {

    public static void main(String[] args) {
        Duck duck = new MallardDuck();

        Turkey turkey = new WildTurkey();
        Duck turkeyAdapter = new TurkeyAdapter(turkey);

        System.out.println("Turkey say");
        turkey.gobble();
        turkey.fly();

        System.out.println("\nDuck say");
        testDuck(duck);

        System.out.println("\nTurkeyAdapter say");
        testDuck(turkeyAdapter);
    }

    static void testDuck(Duck duck) {
        duck.quack();
        duck.fly();
    }
}