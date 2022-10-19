package Command;

import Receiver.TV;

//커맨드 클래스
public class TVOnCommand implements Command {
    TV tv;

    public TVOnCommand(TV tv) {
        this.tv = tv;
    }

    @Override
    public void execute() {
        tv.wakeUp();
    }

}
