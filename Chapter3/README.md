# Ch3. 데코레이터 패턴
## OCP 디자인 원칙이란?
- OCP(Open-Closed Principle)
- 클래스는 확장에 열려 있어야 하지만 변경에는 닫혀 있어야 한다.
- 2장의 옵저버 패턴 또한 주제에 코드를 추가하지 않으면서도 얼마든지 확장할 수 있는 패턴이다.


## 데코레이터 패턴 정의

![image](https://user-images.githubusercontent.com/66015002/193959548-94253862-ad80-4f55-a8bc-808fd87e0bec.png)

- 데코레이터 패턴으로 객체에 추가 요소를 동적으로 더할 수 있다.
  - 데코레이터는 자신이 장식하고 있는 객체에게 어떤 행동을 위임하는 일 말고도 추가 작업을 수행할 수 있다.
- 데코레이터를 사용하면 서브클래스를 만들 때보다 훨씬 유연하게 기능을 확장할 수 있다.
  - 한 객체를 여러 개의 데코레이터로 감쌀 수 있다.g 
  - 객체는 언제든지 감쌀 수 있으므로 실행 중에 필요한 데코레이터를 마음대로 적용할 수 있다.
  
## 데코레이터 적용 예: 자바I/O

![image](https://user-images.githubusercontent.com/66015002/193959499-5ce4e39d-f8e2-4768-a2d4-6386e3750c43.png)

### FilterInputStream의 소스 구조
```java
public class FilterInputStream extends InputStream {
    protected volatile InputStream in;
    // 접근제어자가 proteced이므로 생성자를 사용할 수 없습니다.
    protected FilterInputStream(InputStream in){ 
        this.in = in;
    }

    public int read() throws IOException{
        return in.read();
    }
    ...
}
```

### 대문자를 소문자로 바꿔주는 데코레이터 만들어보기
```java
public class LowerCaseInputStream extends FilterInputStream {
    public LowerCaseInputStream(InputStream in) {
        super(in);
    }

    public int read() throws IOException {
        int c = in.read();
        return (c == -1 ? c : Character.toLowerCase((char)c));
    }
    
    public int read(byte[] b, int offset, int len) throws IOException {
        int result = in.read(b, offset, len);
        for(int i = offset; i < offset + result; i++) {
            b[i] = (byte)Character.toLowerCase((char)b[i]);
        }
        
        return result;
    }

}
```
