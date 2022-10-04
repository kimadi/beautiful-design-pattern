# Ch.5 


## 싱글턴 패턴
싱글턴 패턴(Singleton Pattern)은 클래스 인스턴스를 하나만 만들고, 그 인스턴스로의 전역 접근을 제공한다.
- 전역 변수를 사용할 때와 마찬가지로 객체 인스턴스를 어디서든지 접근 할 수 있다
- 전역변수에 어떤 객체를 담아놓고 프로그램이 끝날 동안 사용하지 않는다면, 자원이 낭비되지만, 싱글턴은 필요할 때만 객체를 만들 수 있다


> 고전적인 싱글톤 패턴 구현

```kotlin
class Singleton private constructor() {
    companion object {    // java 의 static
        var uniqueInstance: Singleton? = null
        fun getSingleton() : Singleton {
            if (uniqueInstance == null) {
                uniqueInstance =  Singleton()
            }
            return uniqueInstance!!
        }
    }
}
```

## 고전적인 싱글톤 패턴의 문제
멀티쓰레드로 사용했을 경우 첫 번째 쓰레드에서 인스턴스를 만들어내기 전에 두 번째 쓰레드에서도 인스턴스 생성을 요청 할 수 있기 때문에, 원자성을 보장할 수 없다.
<br>
`Synchronized` 를 사용하면 해당 문제를 해결할 수 있으나, 속도에 문제가 생길 수 있다.


```kotlin
class Singleton private constructor() {
    companion object {
        var uniqueInstance: Singleton? = null

        @Synchronized
        fun getSingleton() : Singleton {
            if (uniqueInstance == null) {
                uniqueInstance =  Singleton()
            }
            return uniqueInstance!!
        }
    }
}
```


속도가 중요하지 않다면 그냥 두어도 되지만, 다른 해결방법도 있다.<br>

객체를 null로 두는게 아니라 생성하며 초기화하거나, DCL(Double-Checking Locking)을 사용해서 getInstance에서 동기화 되는 부분을 줄일 수도 있다. (volatile)


```kotlin
class Singleton private constructor() {
    companion object {
        @Volatile
        var uniqueInstance: Singleton? = null

        @Synchronized
        fun getSingleton() : Singleton {
            if (uniqueInstance == null) {
                uniqueInstance =  Singleton()
            }
            return uniqueInstance!!
        }
    }
}
```


### Volatile
`@Volatile`을 붙이면 변수의 값이 메인 메모리에만 저장되며, 멀티 쓰레드 환경에서 메인 메모리의 값을 참조하므로 변수 값 불일치 문제를 해결할 수 있게된다.
<br> 다만 CPU캐시를 참조하는 것보다 메인 메모리를 참조하는 것이 더 느리므로, 성능은 떨어질 수 밖에 없다.


### 전역 변수와 싱글톤

![image](https://user-images.githubusercontent.com/75432228/193805018-b9be105f-3fdb-406b-9f26-7cdf638d4d5c.png)


전역변수는 data section에 들어가 고정적인 메모리를 할당한다. (= 어플리케이션이 종료될 때까지 해당 영역을 차지한다)
<br>
<br>
반면에 heap 영역은 유동적이다.
<br> 싱글턴 패턴은 서비스에서 사용할 때 인스턴스를 생성해 heap 메모리에 할당하고 사용이 다 끝나면 메모리 해제를 하여 다시 사용할 수 있도록 관리한다.
