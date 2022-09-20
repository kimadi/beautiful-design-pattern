
// FLY
interface FlyBehavior {
    fun fly()
}

class FlyWithWings : FlyBehavior {
    override fun fly() {
        println("난다")
    }
}

class FlyNoWay : FlyBehavior {
    override fun fly() {
        println("못난다ㅜㅜ")
    }
}

// QUACK
interface QuackBehavior {
    fun quack()
}

class Quack : QuackBehavior {
    override fun quack() {
        println("꽥")
    }
}

class MuteQuack : QuackBehavior {
    override fun quack() {
        println("조용")
    }
}

class Squeck : QuackBehavior {
    override fun quack() {
        println("삑")
    }
}

// DUCK
abstract class Duck (
    var quackBehavior : QuackBehavior,
    var flyBehavior : FlyBehavior
){
    abstract fun display()

    fun swim() {
        println("오리는 다 뜬다")
    }

    fun performFly() {
        flyBehavior.fly()
    }
    
    fun performQuak() {
        quackBehavior.quack()
    }
    
}

class MallarDuck : Duck (Quack(), FlyWithWings())  {

    override fun display() {
        println("물오리")
    }

}

// RUN
fun main() {
    val mallar = MallarDuck()
    mallar.performFly()
    mallar.performQuak()

    mallar.quackBehavior = Squeck()

    mallar.performQuak()
}