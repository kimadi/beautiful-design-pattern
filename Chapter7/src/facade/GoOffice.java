package facade;

public class GoOffice {

    public void goToWork() {
        Wash wash = new Wash();
        Breakfast breakfast = new Breakfast();
        Move move = new Move();

        wash.brushTeeth();
        wash.shower();
        breakfast.eat();
        breakfast.water();
        move.bus();
    }
}