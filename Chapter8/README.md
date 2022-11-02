# 8장 템플릿 메소드 패턴 - 알고리즘 캡슐화 하기

## 플릿 메소드 패턴이란?

알고리즘의 틀을 만들기 위한 패턴이다.

이 패턴에서 틀(템플릿)이란 일련의 단계들로 알고리즘을 정의한 메소드다. 여러 던계 가운데 하나 이상이 추상 메소드로 정의되며, 그 추상 메소드는 서브클래스에서 구현된다. 이렇게 하면 서브클래스에서 일부분의 단계를 구현할 수 있도록 하면서도 알고리즘의 구조는 바꾸지 않아도 되도록 할 수 있다.

- 메소드에서 알고리즘의 골격을 정의한다.
- 알고리즘의 여러 단계 중 일부는 서브클래스에서 구현할 수 있다.
- 템플릿 메소드를 이용하면 알고리즘의 구조는 그대로 유지하면서 서브클래스에서 특정 단계를 재정의 할 수 있다.


## 책 예시

#### 커피와 차가 만들어 지는법을 비교해보자

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


### 템플릿 메소드 패턴 전체 코드

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
