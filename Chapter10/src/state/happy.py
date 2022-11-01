from state.base_state import BaseState


class Happy(BaseState):
    def __init__(self, person):
        super().__init__(person)

    def work(self):
        super().work()

    def discuss(self):
        super().discuss()

    def eat_food(self):
        super().eat_food()

    def drink_coffee(self):
        super().drink_coffee()

    def go_home(self):
        print('  "아직 집 못 가 ㅜㅜ"')

    def how_are_you(self):
        print('  "좋아"')
