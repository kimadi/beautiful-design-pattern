from subject import WeatherDataPush, WeatherDataPull
from observer import WeatherDisplayPush, WeatherDisplayPull

if __name__ == "__main__":
    # 옵저버 패턴 예시 코드
    # 1. subject 생성
    # 2. observer 생성 후 subject에 등록
    # (예시에는 생성자에 subject에 등록 과정이 포함되어 있음)
    # 3. subject의 데이터를 update하면 observer에 변경사항이 전달됨
    
    # push 방식
    weather_data_push = WeatherDataPush()
    weather_display_push = WeatherDisplayPush(weather_data_push, "서울")
    weather_data_push.set_measurament(26, 75, 2)
    
    # pull 방식
    weather_data_pull = WeatherDataPull()
    weather_display_pull = WeatherDisplayPull(weather_data_pull, "부산")
    weather_data_pull.set_measurament(25, 89, 97)
    