package Command;

// 커맨드 인터페이스
public interface Command {
    Command NoCommand = (Command) () -> {};
    void execute();
}
