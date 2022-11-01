from state.base_state import BaseState


class Unhappy(BaseState):
    def __init__(self, person):
        super().__init__(person)

    def work(self):
        print('  "일하기 싫어!!!"')

    def discuss(self):
        print('  "회의 가기 싫어!!!"')

    def eat_food(self):
        if self._milky.is_healthy():
            super().eat_food()
            self._milky.set_next_state()
        else:
            print('  "회사밥 싫어! 집 보내줘!!!"')

    def drink_coffee(self):
        if self._milky.is_healthy():
            super().drink_coffee()
            self._milky.set_next_state()
        else:
            print('  "커피 싫어! 집 보내줘!!!"')

    def go_home(self):
        super().go_home()

    def how_are_you(self):
        print('  "집에 보내줘!!!"')
