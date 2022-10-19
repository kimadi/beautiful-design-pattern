package Command;

import Receiver.TV;

//커맨드 클래스
public class TVOffCommand implements Command {
    TV tv;

    public TVOffCommand(TV tv) {
        this.tv = tv;
    }

    @Override
    public void execute() {
        tv.sleep();
    }

}
