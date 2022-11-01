from constant.constant import MAX_NUMS


class BaseState:
    def __init__(self, person):
        self._milky = person

    def work(self):
        print('  "일하기 싫어~~~"')
        self._milky.decrease("health", 1)
        self._milky.decrease("hunger", 2)
        self._milky.decrease("sleep", 1)
        self._milky.set_next_state()

    def discuss(self):
        print('  "회의 가기 귀찮아~~~"')
        self._milky.decrease("health", 1)
        self._milky.decrease("hunger", 1)
        self._milky.decrease("sleep", 2)
        self._milky.set_next_state()

    def eat_food(self):
        if self._milky.nums["hunger"] >= MAX_NUMS["hunger"]:
            print('  "배불러"')
        else:
            print('  "밥~~~"')
            self._milky.increase("hunger", 2)
        self._milky.set_next_state()

    def drink_coffee(self):
        if self._milky.nums["sleep"] >= MAX_NUMS["sleep"]:
            print('  "커피 이미 있어"')
        else:
            print('  "커피~~~"')
            self._milky.increase("sleep", 2)
        self._milky.set_next_state()

    def go_home(self):
        print('  "퇴근조아~~~"')
        self._milky.decrease("health", 3)
        self._milky.decrease("hunger", 2)
        self._milky.decrease("sleep", 2)
        self._milky.set_next_state()

    def how_are_you(self):
        pass
