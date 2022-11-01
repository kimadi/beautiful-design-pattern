from state.base_state import BaseState


class Tired(BaseState):
    def __init__(self, person):
        super().__init__(person)

    def work(self):
        print('  "졸려!!!"')

    def discuss(self):
        print('  "졸려!!!"')

    def eat_food(self):
        super().eat_food()

    def drink_coffee(self):
        super().drink_coffee()

    def go_home(self):
        print('  "졸려... 근데 아직 집 못 가 ㅜㅜ"')

    def how_are_you(self):
        print('  "졸려"')

