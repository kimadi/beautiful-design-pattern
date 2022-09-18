from abc import ABCMeta, abstractmethod

# subject를 구현하는 abstract class
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, new_observer):
        pass # 옵저버 등록
    
    @abstractmethod
    def remove_observer(self, observer):
        pass # 옵저버 제거
    
    @abstractmethod
    def notify_observers(self):
        pass # 옵저버에게 새로운 데이터 전달

# Subject를 상속하는 WeatherData 클래스 (push 방식)
class WeatherDataPush(Subject):
    def __init__(self):
        self.__observers = set()
        self.__temperature = 0
        self.__humidity = 0
        self.__chance_of_rain = 0
    
    # 추상 메소드 구현
    def register_observer(self, new_observer):
        self.__observers.add(new_observer)
        
    def remove_observer(self, observer):
        self.__observers.remove(observer)
        
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

# Subject를 상속하는 WeatherData 클래스 (pull 방식)            
class WeatherDataPull(Subject):
    def __init__(self):
        self.__observers = set()
        self.__temperature = 0
        self.__humidity = 0
        self.__chance_of_rain = 0
    
    # 추상 메소드 구현
    def register_observer(self, new_observer):
        self.__observers.add(new_observer)
        
    def remove_observer(self, observer):
        self.__observers.remove(observer)
        
    def notify_observers(self):
        for observer in self.__observers:
            observer.update()
    
    # 온도, 습도, 강수확률 설정
    def set_measurament(self, temperature, humidity, chance_of_rain):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__chance_of_rain = chance_of_rain
        self.notify_observers()

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
    