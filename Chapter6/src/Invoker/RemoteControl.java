package Invoker;

import Command.*;

class CommandSet{
    Command onCommand;
    Command offCommand;
    public  CommandSet() {
        this.onCommand = Command.NoCommand;
        this.offCommand = Command.NoCommand;
    }

}

// invoker
public class RemoteControl {
    CommandSet[] commandSets;

    public RemoteControl() {
        commandSets = new CommandSet[7];
        for (int i=0; i<commandSets.length; i++){
            commandSets[i] = new CommandSet();
        }
    }

    public void setCommand(int slot, Command onCommand, Command offCommand) {
        commandSets[slot].onCommand = onCommand;
        commandSets[slot].offCommand = offCommand;
    }

    public void onButton(int slot) {
        commandSets[slot].onCommand.execute();
    }

    public void offButton(int slot) {
        commandSets[slot].offCommand.execute();
    }
}