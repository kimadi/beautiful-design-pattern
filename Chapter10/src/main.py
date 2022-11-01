from context.milky import Milky

if __name__ == '__main__':
    milky = Milky()

    print("========== [오전] ==========")
    milky.how_are_you()
    milky.work()
    milky.how_are_you()
    milky.work()
    milky.go_home()

    print("\n========== [점심] ==========")
    milky.eat_food()

    print("\n========== [오후] ==========")
    milky.how_are_you()
    milky.discuss()
    milky.how_are_you()
    milky.work()
    milky.go_home()
    milky.drink_coffee()
    milky.how_are_you()
    milky.work()

    print("\n========== [저녁] ==========")
    milky.how_are_you()
    milky.work()
    milky.discuss()
    milky.eat_food()
    milky.drink_coffee()
    milky.go_home()
