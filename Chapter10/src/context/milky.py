from state.happy import Happy
from state.hungry import Hungry
from state.tired import Tired
from state.unhappy import Unhappy
from constant.constant import MAX_NUMS


class Milky:
    def __init__(self):
        self.__states = {
            "happy": Happy(self),
            "hungry": Hungry(self),
            "tired": Tired(self),
            "unhappy": Unhappy(self)
        }
        self.__current_state = self.__states["happy"]
        self.nums = {
            "health": MAX_NUMS["health"],
            "hunger": MAX_NUMS["hunger"],
            "sleep": MAX_NUMS["sleep"],
        }

    def work(self):
        print("일해라 밀키!")
        self.__current_state.work()

    def discuss(self):
        print("회의 가자 밀키!")
        self.__current_state.discuss()

    def eat_food(self):
        print("밀키야 밥먹자~")
        self.__current_state.eat_food()

    def drink_coffee(self):
        print("밀키야 커피 먹자~")
        self.__current_state.drink_coffee()

    def go_home(self):
        print("밀키야 집에 가자~")
        self.__current_state.go_home()

    def how_are_you(self):
        print("[밀키의 상태]", end='')
        self.__current_state.how_are_you()

    def set_next_state(self):
        if self.nums["health"] == 0 \
                or (self.nums["hunger"] == 0 and self.nums["sleep"] == 0):
            self.__current_state = self.__states["unhappy"]
        elif self.nums["hunger"] == 0:
            self.__current_state = self.__states["hungry"]
        elif self.nums["sleep"] == 0:
            self.__current_state = self.__states["tired"]
        else:
            self.__current_state = self.__states["happy"]

    def increase(self, target, amount):
        self.nums[target] = self.nums[target] + amount \
            if (self.nums[target] + amount) <= MAX_NUMS[target] else MAX_NUMS[target]

    def decrease(self, target, amount):
        self.nums[target] = self.nums[target] - amount \
            if self.nums[target] > amount else 0

    def is_healthy(self):
        return self.nums["health"] > 0
