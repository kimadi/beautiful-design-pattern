import Invoker.RemoteControl;
import Receiver.Light;
import Receiver.TV;

public class Client {
    public static void main(String[] args) {

        TV tv = new TV();
        Light light = new Light();

        RemoteControl remoteControl = new RemoteControl();
        remoteControl.setCommand(0, light::on, light::off);
        remoteControl.setCommand(1, tv::wakeUp, tv::sleep);

        remoteControl.onButton(0);
        remoteControl.offButton(1);

    }
}