from state.base_state import BaseState


class Hungry(BaseState):
    def __init__(self, person):
        super().__init__(person)

    def work(self):
        print('  "배고파!!!"')

    def discuss(self):
        print('  "배고파!!!"')

    def eat_food(self):
        super().eat_food()

    def drink_coffee(self):
        super().drink_coffee()

    def go_home(self):
        print('  "배고파... 근데 아직 집 못 가 ㅜㅜ"')

    def how_are_you(self):
        print('  "배고파"')
