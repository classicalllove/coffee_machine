class CoffeeMachine():
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.disp_cups = 9

    def coffee_action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit): ')
            action = input()
            if action == 'buy':
                self.buy()
            elif action == 'remaining':
                self.remaining()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'exit':
                break

    def buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choose_action = input()
        if choose_action == 'back':
            pass
        elif choose_action == '1':
            if self.water < 250:
                print('Sorry, not enough water!\n')
            elif self.coffee < 16:
                print('Sorry, not enough coffee!\n')
            elif self.disp_cups == 0:
                print('Sorry, not enough cups!\n')
            else:
                print('I have enough resources, making you a coffee!\n')
                self.money += 4
                self.water -= 250
                self.coffee -= 16
                self.disp_cups -= 1

        elif choose_action == '2':
            if self.water < 350:
                print('Sorry, not enough water!\n')
            elif self.milk < 75:
                print('Sorry, not enough milk!\n')
            elif self.coffee < 20:
                print('Sorry, not enough coffee!\n')
            elif self.disp_cups == 0:
                print('Sorry, not enough cups!\n')
            else:
                print('I have enough resources, making you a coffee!\n')
                self.money += 7
                self.water -= 350
                self.coffee -= 20
                self.milk -= 75
                self.disp_cups -= 1

        elif choose_action == '3':
            if self.water < 200:
                print('Sorry, not enough water!\n')
            elif self.milk < 100:
                print('Sorry, not enough milk!\n')
            elif self.coffee < 12:
                print('Sorry, not enough coffee!\n')
            elif self.disp_cups == 0:
                print('Sorry, not enough cups!\n')
            else:
                print('I have enough resources, making you a coffee!\n')
                self.money += 6
                self.water -= 200
                self.coffee -= 12
                self.milk -= 100
                self.disp_cups -= 1

    def fill(self):
        print('\nWrite how many ml of water you want to add: ')
        water_fill = int(input())
        print('Write how many ml of milk you want to add: ')
        milk_fill = int(input())
        print('Write how many grams of coffee beans you want to add: ')
        coffee_fill = int(input())
        print('Write how many disposable cups you want to add: ')
        cups_fill = int(input())
        print()
        self.water += water_fill
        self.milk += milk_fill
        self.coffee += coffee_fill
        self.disp_cups += cups_fill

    def take(self):
        print(f'\nI gave you ${self.money}\n')
        self.money -= self.money

    def remaining(self):
        print(
            f"""\nThe coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk\n{self.coffee} g of coffee beans\n{self.disp_cups} disposable cups\n${self.money} of money\n""")


make_coffee = CoffeeMachine()
make_coffee.coffee_action()
