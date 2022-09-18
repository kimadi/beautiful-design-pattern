# Ch2. 옵저버 패턴
## 옵저버 패턴의 원리
> **신문사와 구독자**
> 
> 한 객체의 상태가 바뀌면 그 객체에 의존하는 다른 객체에게 연락이 가고 자동으로 내용이 갱신
> 
> 일대다(one-to-many) 의존성 관계

- 주제(subject): 데이터의 상태를 관리
- 옵저버(observer): 데이터를 활용하기 위해 주제를 구독

1. 주제는 데이터를 관리하고 있음
2. 주제의 데이터를 활용하려는 옵저버가 주제를 구독 (주제 객체에 옵저버 객체 등록)
3. 주제가 관리하는 데이터가 바뀔 때 옵저버에게 갱신 내용 전달



## 옵저버 패턴의 구현
- `src` 디렉토리에서 예제 코드의 원본 확인 가능
- `python ./src/main.py`로 예제 코드를 실행해볼 수 있음

1. 주제 클래스 구현
```
# subject를 구현하는 abstract class
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, new_observer):
        pass # 옵저버 등록

    ...
    
    @abstractmethod
    def notify_observers(self):
        pass # 옵저버에게 새로운 데이터 전달
```

2. 옵저버 클래스 구현
```
class ObserverPush(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temperature, humidity, chance_of_rain):
        pass # 온도, 습도, 기온 업데이트
```

3. 옵저버 인스턴스가 주제 인스턴스 구독
```
class WeatherDisplayPush(ObserverPush, Display):
    def __init__(self, weather_data: Subject, region: str):
        ...
        weather_data.register_observer(self)
```

4. 주제 인스턴스에서 관리하는 상태가 변할 때 옵저버에 변경내용이 업데이트 되도록 코드 작성
```
class WeatherDataPush(Subject):
    ...

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(
                self.__temperature, self.__humidity, self.__chance_of_rain
            )
    
    # 온도, 습도, 강수확률 설정
    def set_measurament(self, temperature, humidity, chance_of_rain):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__chance_of_rain = chance_of_rain
        self.notify_observers()

class WeatherDisplayPush(ObserverPush, Display):
    ...

    def update(self, temperature, humidity, chance_of_rain):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__chance_of_rain = chance_of_rain
        self.display()
```

5. 예시 코드와 결과
```
    weather_data_push = WeatherDataPush()
    weather_display_push = WeatherDisplayPush(weather_data_push, "서울")
    weather_data_push.set_measurament(26, 75, 2)
```



## 푸시(push) 방식과 풀(pull) 방식
### 푸시(push) 방식
- 주제가 옵저버에 상태를 알리는 방식
- 주제의 상태가 업데이트 될 때 미리 지정된 모든 데이터의 현재 상태를 보냄
- 위에서 본 구현 에시가 푸시 방식

### 풀(pull) 방식
- 옵저버가 주제로부터 상태를 끌어오는 방식
- 주제의 상태가 업데이트 될 때 옵저버가 getter를 통해 필요한 데이터만 가져옴
- 코드를 일반화할 수 있으므로 더 유리함
- 예시 코드
    ```
    class WeatherDataPull(Subject):
        ...

        # 온도, 습도, 강수확률 getter
        @property
        def temperature(self):
            return self.__temperature
        
        @property
        def humidity(self):
            return self.__humidity
        
        @property
        def chance_of_rain(self):
            return self.__chance_of_rain
    

    class ObserverPull(metaclass=ABCMeta):
        @abstractmethod
        def update(self):
            pass

    class WeatherDisplayPull(ObserverPull, Display):
        ...

        def update(self):
            self.__temperature = self.__weather_data.temperature
            self.__humidity = self.__weather_data.humidity
            self.__chance_of_rain = self.__weather_data.chance_of_rain
            self.display()
    ```
    - 옵저버의 update 메소드 파라미터에 어떤 데이터를 가져올 지 명시하지 않음
    - 해당 함수 내부 구현에서 getter를 통해 필요한 데이터를 가져옴



## 느슨한 결합(Loose Coupling)

- 객체들이 상호작용할 수는 있지만 서로를 잘 모르는 관계
- 옵저버 패턴은 느슨한 결합을 보여주는 좋은 사례
  - 주제는 옵저버가 구현하는 인터페이스만 알면 됨 (내부 구현을 알 필요는 없음)
  - 주제에 옵저버를 언제든 추가 가능
  - 새로운 옵저버를 추가할 때 주제의 코드를 바꿀 필요가 없음
  - 주제와 옵저버는 서로 독립적으로 재사용 가능
  - 주제와 옵저버 간에 인터페이스만 지킨다면 내부 구현이 어떻게 바뀌든 문제가 없음
