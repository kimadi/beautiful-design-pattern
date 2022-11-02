# 8장 템플릿 메소드 패턴 - 알고리즘 캡슐화 하기

## 템플릿 메소드 패턴이란?

알고리즘의 틀을 만들기 위한 패턴이다.

이 패턴에서 틀(템플릿)이란 일련의 단계들로 알고리즘을 정의한 메소드다. 여러 던계 가운데 하나 이상이 추상 메소드로 정의되며, 그 추상 메소드는 서브클래스에서 구현된다. 이렇게 하면 서브클래스에서 일부분의 단계를 구현할 수 있도록 하면서도 알고리즘의 구조는 바꾸지 않아도 되도록 할 수 있다.

- 메소드에서 알고리즘의 골격을 정의한다.
- 알고리즘의 여러 단계 중 일부는 서브클래스에서 구현할 수 있다.
- 템플릿 메소드를 이용하면 알고리즘의 구조는 그대로 유지하면서 서브클래스에서 특정 단계를 재정의 할 수 있다.


## 템플릿 메소드 패턴 예시

#### 커피와 차가 만들어 지는 법을 비교해보자

```
1. 커피 만드는 법

1) 물을 끓인다. 

2) 끓는 물에 커피를 우려낸다.

3) 커피를 컵에 따른다.

4) 설탕과 우유를 추가한다.



2. 홍차 만드는 법

1) 물을 끓인다.

2) 끓는 물에 차를 우려낸다.

3) 차를 컵에 따른다.

4) 레몬을 추가한다.
```

#### 중복된 부분이 많으니 공통적인 부분을 추상화 시켜서 클래스를 만들어볼까?

![image](https://user-images.githubusercontent.com/66015002/199402745-00e4f764-d8df-4eca-a3a1-b6c399b5ec0e.png)

#### Coffee와 Tea 둘 다 만드는 알고리즘이 동일하다!
#### 알고리즘 자체를 추상화시켜보자!


```java
void prepareRecipe() {

	boilWater();

	brew();

	pourInCup();

	addCondiments();

}
```


### 전체 코드

```java
public abstract class CaffeineBeverage {

	final void prepareRecipe() {

		boilWater();

		brew();

		pourInCup();

		addcondiments();

	}

	abstract void brew();

	abstract void addcondiments();

	void boilWater() {

		System.out.println("물 끓이는 중");

	}

	void pourInCup() {

		System.out.println("컵에 따르는 중");

	}

}
```

```java
public class Coffee extends CaffeineBeverage {

	@Override
	void brew() {

		System.out.println("필터를 통해 커피를 우려내는 중");

	}

	@Override
	public void addCondiments() {

		System.out.println("설탕과 우유를 추가하는 중");

	}

}
```

```java
public class Tea extends CaffeineBeverage {

	@Override
	void brew() {

		System.out.println("차를 우려내는 중");

	}

	@Override
	public void addCondiments() {

		System.out.println("레몬을 추가하는 중");

	}

}
```

```java
1. Tea 객체를 만들고.

Tea myTea = new Tea();



2. 템플릿 메소드를 호출한다.

myTea.prepareRecipe(); 카페인 음료를 만들기 위한 알고리즘이 돌아간다.



3. 물을 끓인다.

boilWater(); 이 단계는 CaffeineBeverage 에서 처리된다.



4. 이제 차를 우려낸다. 

brew(); 이방법은 서브클래스만 알고있다.



5. 차를 컵에 따른다.

pourInCup(); 이 단계도 공통적인 부분이기 때문에 Caffeinebeverage 에서 맡아서 처리된다.



6. 마지막으로 첨가물을 추가한다.

addCondiments(); 첨가물은 음료마다 다르기때문에 서브클래스에서 처리된다.
```


### 적용한 후 얻은 이점
- CaffeineBeverage 덕분에 서브클래스에서 코드를 재사용 가능
- CaffeineBeverage 알고리즘을 독점하고 있기 때문에 유지보수 용이
- 다른 음료도 메소드 몇개로 쉽게 추가할 수 있는 구조


## 후크란?

- 후크(hook)는 추상클래스에서 선언되는 메소드긴 하지만 기본적인 내용만 구현되어 있거나 아무 코드도 들어있지 않은 메소드이다.
- 후크를 사용하면 서브클래스 입장에서는 다양한 위치에서 알고리즘에 끼어들수 있는 이점이 있다.

```java
public abstract class CaffeineBeverageWithHook {

	final void prepareRecipe() {

		boilWater();

		brew();

		pourInCup();

		if (customerWantsCondiments()) {

			addcondiments();

		}

	}

	abstract void brew();

	abstract void addcondiments();

	void boilWater() {

		System.out.println("물 끓이는 중");

	}

	void pourInCup() {

		System.out.println("컵에 따르는 중");

	}

	boolean customerWantsCondiments() { // 이 메소드는 서브클래스에서 필요에 따라

		return true; // 오버라이드 할수 있는 메소드이므로 후크이다.

	}

}
```

```java
public class CoffeeWithHook extends CaffeineBeverageWithHook {

	@Override
	void brew() {

		System.out.println("필터를 통해 커피를 우려내는 중");

	}

	@Override
	public void addCondiments() {

		System.out.println("설탕과 우유를 추가하는 중");

	}

	@Override
	public boolean customerWantsCondiments() {

		String answer = getUserInput();

		if (answer.toLowerCase().startWith("y"))
			return true;

		else
			return false;

	}

	private String getUserInput() {

		// 입력받는 로직

	}

}
```

#### 알고리즘에서 필수적이지 않은 부분을 필요에 따라 선택적으로 서브클래스에서 구현하든 말든 하도록 하는 경우에 후크를 사용할 수 있다.


## 할리우드 원칙


한 줄 요약
> 먼저 연락하지 마세요. 저희가 연락 드리겠습니다.

- 이 디자인 원칙을 활용하면 의존성 부패(dependency rot)를 방지 할수 있다.

- 어떤 고수준 구성요소가 저수준 구성요소에 의존하고, 그 저수준 구성요소는 다시 고수준 구성요소에 의존하고, 그 고수준 구성요소는 다시 또 다른 구성요소에 의존하고.. 이런 식으로 의존성이 복잡하게 꼬여있는 것을 의존성 부패라고 한다.

 - 헐리우드 원칙을 사용하면, 저수준 구성요소에서 시스템에 접속을 할수는 있지만, 언제 어떤 식으로 그 구성요소들을 사용할지는 고수준 구성요소에서 결정하게 된다.

- 즉 저수준 구성요소는 컴퓨테이션에 참여할 수는 있지만 절대 고수준 구송요소를 직접 호출하면 안된다는 것이다.
