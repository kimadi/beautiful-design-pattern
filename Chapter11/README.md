# Ch10. 프록시 패턴

## 프록시 패턴

특정 객체로의 접근을 제어하는 대리인을 제공

# 프록시 패턴의 장단점

## 프록시패턴 장점

- 사이즈가 큰 객체가 로딩되기 전에도 프록시를 통해 참조를 할 수 있다.
- 실제 객체의 public, protected 메소드를 숨기고 인터페이스를 통해 노출시킬 수 있다.
- 로컬에 있지 않고 떨어져있는 객체를 사용할 수 있다.
- 원래 객체에 접근에 대해 사전처리를 할 수 있다.

## 프록시패턴의 단점

- 객체를 생성할 때 한 단계를 거치게 되므로, 빈번한 객체 생성이 필요한 경우 성능이 저하될 수 있다.
- 프록시 내부에서 객체 생성을 위해 스레드가 생성, 동기화가 구현되어야 하는 경우 성능이 저하될 수 있다.
- 로직이 난해해져 가독성이 떨어질 수 있다.

# 프록시의 종류

## 원격 프록시

> 다른 JVM에 들어있는 객체의 대리인에 해당하는 로컬 객체

프록시의 메소드를 호출하면 그 호출이 네트워크로 전달되어 결국 원격 객체의 메소드가 호출된다. 그리고 그 결과는 다시 프록시를 거쳐서 클라이언트에게 전달된다.

- RMI(Remote Method Invocation, 원격 메소드 호출)을 사용
- 클라이언트 보조 객체(스텁)와 서비스 보조 객체(스켈레톤)를 만든다.
- 클라이언트에서 원격 객체를 찾아 접근하기 위해 쓸 수 있는 룩업 서비스도 제공한다.
- 클라이언트 입장에서는 로컬 메소드 호출과 같은 방식으로 메소드를 호출하지만, 실제로 클라이언트 보조객체에서 네트워크를 통해 호출을 전송할 수 있다.
- 네트워킹 및 입출력 기능이 필수적이며, 이에 대한 주의가 필요하다.

## 가상 프록시

> 생성하기 힘든 자원으로의 접근을 제어

생성하는 데 많은 비용이드는 객체를 대신한다.
진짜 객체가 필요한 상황이 오기 전까지 객체의 생성을 미루는 기능을 제공한다. 객체 생성전이나 객체 생성 도중에 객체를 대신하기도 하고, 객체 생성이 끝나면 RealSubject에 직접 요청을 전달한다.

<br>
데이터베이스 접근은 데이터가 실제로 사용되기 전까지 프록시가 대신함

## 보호 프록시

> 접근 권한이 필요한 자원으로의 접근을 제어

`java.lang.reflect` 패키지 안에 프록시 기능이 내장되어 있다. 이 패키지를 사용하면 즉석에서 하나 이상의 인터페이스를 구현하고, 지정한 클래스에 메소드 호출을 전달하는 프록시 클래스를 만들 수 있다. 진짜 프록시는 실행 중에 생성되므로 이러한 자바 기술을 동적 프록시(dynamic proxy)라고 부른다.

> ### Dynamic Proxy
- 런타임에 동적으로 만들어지는 오브젝트
- 리플렉션 이용
- 타깃 인터 페이스와 동일한 형태
- FactoryBean 사용

<br>

ex. `Collections.unmodifiableCollection` 을 통해 받은 Collection 구현체

# Appendix

### JDK Dynamic Proxy

```java
Object proxy=Proxy.newProxyInstance(ClassLoader       // 클래스로더
        ,Class<?>[]        // 타깃의 인터페이스
        ,InvocationHandler // 타깃의 정보가 포함된 Handler
        );
```

![](https://gmoon92.github.io/md/img/aop/jdk-dynamic-proxy-and-cglib/jdk-dynamic-proxy1.png)

1. 타깃의 인터페이스를 자체적인 검증 로직을 통해 ProxyFactory에 의해 타깃의 인터페이스를 상속한 Proxy 객체 생성
2. Proxy 객체에 InvocationHandler를 포함시켜 하나의 객체로 반환

```java

@Controller
public class UserController {
    @Autowired
    private MemberService memberService;
    // 인터페이스가 아닌 클래스를 Autowired 하여 Runtime Exception 발생
  ...
}

@Service
public class MemberService implements UserService {
    @Override
    public Map<String, Object> findUserId(Map<String, Object> params) {
    ...isLogic
        return params;
    }
}
```

### 인터페이스 기준

```java
public Object invoke(Object proxy,Method proxyMethod,Object[]args)throws Throwable{
        Method targetMethod=null;
        // 주입된 타깃 객체에 대한 검증 코드
        if(!cachedMethodMap.containsKey(proxyMethod)){
            targetMethod=target.getClass().getMethod(proxyMethod.getName(),proxyMethod.getParameterTypes());
            cachedMethodMap.put(proxyMethod,targetMethod);
        } else {
            targetMethod=cachedMethodMap.get(proxyMethod);
        }

        // 타깃의 메소드 실행
        Ojbect retVal=targetMethod.invoke(target,args);
        return retVal;
}

```

![](https://gmoon92.github.io/md/img/aop/jdk-dynamic-proxy-and-cglib/jdk-dynamic-proxy2.png)

### CGLib

```java
Enhancer enhancer=new Enhancer();
enhancer.setSuperclass(MemberService.class); // 타깃 클래스
enhancer.setCallback(MethodInterceptor);     // Handler
Object proxy=enhancer.create(); // Proxy 생성
```

![](https://gmoon92.github.io/md/img/aop/jdk-dynamic-proxy-and-cglib/cglib1.png)

https://web.archive.org/web/20150520175004/https://docs.codehaus.org/display/AW/AOP+Benchmark

### 이전에 CGlib 를 사용하지 않은 이유

- 의존성 추가
- Default 생성자 필요
- target의 생성자 2번 출출

# REFERENCE

- https://johngrib.github.io/wiki/pattern/proxy/
- https://gmoon92.github.io/spring/aop/2019/04/20/jdk-dynamic-proxy-and-cglib.html
