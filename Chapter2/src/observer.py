from abc import ABCMeta, abstractmethod
from subject import Subject

class Display(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass # 온도, 습도, 기온 출력

# push 방식의 observer
class ObserverPush(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temperature, humidity, chance_of_rain):
        pass # 온도, 습도, 기온 업데이트
    
    @abstractmethod
    def change_subject(self, new_subject):
        pass # subject 변경
    
class WeatherDisplayPush(ObserverPush, Display):
    def __init__(self, weather_data: Subject, region: str):
        self.__region = region
        self.__temperature = 0
        self.__humidity = 0
        self.__chance_of_rain = 0
        self.__weather_data = weather_data
        weather_data.register_observer(self)
    
    def update(self, temperature, humidity, chance_of_rain):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__chance_of_rain = chance_of_rain
        self.display()
    
    def change_subject(self, new_subject):
        self.__weather_data.remove_observer(self)
        self.__weather_data = new_subject
    
    def display(self):
        print(
            f"[WeatherDisplayPush] {self.__region} 날씨 - " \
            + f"온도: {self.__temperature}도, " \
            + f"습도: {self.__humidity}%, " \
            + f"강수확률: {self.__chance_of_rain}%"
        )

# pull 방식의 observer
class ObserverPull(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass
        
    @abstractmethod
    def change_subject(self, new_subject):
        pass
    
class WeatherDisplayPull(ObserverPull, Display):
    def __init__(self, weather_data: Subject, region: str):
        self.__region = region
        self.__temperature = 0
        self.__humidity = 0
        self.__chance_of_rain = 0
        self.__weather_data = weather_data
        weather_data.register_observer(self)
    
    def update(self):
        self.__temperature = self.__weather_data.temperature
        self.__humidity = self.__weather_data.humidity
        self.__chance_of_rain = self.__weather_data.chance_of_rain
        self.display()
    
    def change_subject(self, new_subject):
        self.__weather_data.remove_observer(self)
        self.__weather_data = new_subject
    
    def display(self):
        print(
            f"[WeatherDisplayPull] {self.__region} 날씨 - " \
            + f"온도: {self.__temperature}도, " \
            + f"습도: {self.__humidity}%, " \
            + f"강수확률: {self.__chance_of_rain}%"
        )