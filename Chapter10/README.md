# Ch10. 상태 패턴
## 상태 패턴의 원리
> 객체의 내부 상태를 바꾸는 것으로 객체의 행동을 바꿈

- Context
  - State 클래스 인스턴스를 가짐
  - 어떤 행동이 필요할 때 현재 State 클래스의 행동 메소드를 호출
- State
  - 현재 상태를 나타내는 클래스
  - 행동에 대한 메소드 정의

## 상태 패턴의 구현
- `src` 디렉토리에서 예제 코드의 원본 확인 가능
- `python ./src/main.py`로 예제 코드를 실행해볼 수 있음


![image](https://user-images.githubusercontent.com/54832818/199292038-64fa439d-f4df-46a8-b3d3-f7d6b47ad9a6.png)
- 위 상태 다이어그램을 기반으로 코드 작성 ([Link](https://www.figma.com/file/zTG1R9YxLjGGDBmgRILR8h/%EA%B9%80%EC%95%84%EB%94%94_10%EC%9E%A5_%EC%83%81%ED%83%9C?node-id=0%3A1))
- 4개의 State 클래스: Happy, Hungry, Tired, Unhappy
- 위 State 클래스 중 하나를 가지고 있는 Context 클래스: Milky

## 상태 패턴 & 전략 패턴
- 비슷하면서도 용도가 다르다.
- 상태 패턴
  - State 객체에 일련의 행동을 캡슐화하는 것이 목적
  - Context 객체의 행동은 현재의 state 객체에 따라 결정
  - 클라이언트는 state 객체를 알 필요가 없음
- 전략 패턴
  - 상속을 사용하지 않은 채 행동을 정의하는 객체를 유연하게 지정하는 것이 목표
  - 클리이언트가 어떤 전략 객체를 사용할지 지정


## QnA
- Q. State 클래스에서 다음으로 넘어갈 state 클래스를 꼭 지정해야 하는지?
  - A. Context에서 해도 된다. 

- Q. 클라이언트에서 state 객체에 직접 접근하는 경우가 있는지?
  - A. 그럴 일 없다. 클라이언트는 오직 context 객체와 상호작용한다.

- Q. 여러 context 객체에서 state 객체를 공유해도 되는지?
  - A. 가능하다면 그래도 된다.

- Q. 상태 패턴을 사용하면 state 클래스가 지나치게 많아지게 되는 게 아닌지?
  - A. 그렇긴 한데 state 클래스는 클라이언트에게 노출되는 영역이 아닌데다 상태 패턴을 쓰지 않는다면 상태 관리를 위한 분기 처리가 매우 복잡해진다.
