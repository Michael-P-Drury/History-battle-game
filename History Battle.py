from troops_dict import *
import time
import random


def print_shop(all_troops):

    print()
    print('Welcome to the shop what would you like to buy traveler?')
    for troop in all_troops:
        position = str(all_troops.index(troop) + 1)
        print(position + ' : ' + troop['name'] + ': price = ' + str(troop['price']))
    print(str(len(all_troops)+ 1) + ' : leave shop')


def enter_shop(troops, money, all_troops):
    shop_loop = True
    while shop_loop:
        try:
            enter_choice = input('would you like to enter the shop (y)yes or (n)no? ').lower()
            if enter_choice in ['y', 'n', 'yes', 'no']:
                shop_loop = False
            else:
                print('Not valid input')
        except:
            print('Not valid input')

    if enter_choice in ['y', 'yes']:
        print_shop(all_troops)
        leave = False
        while not leave:
            shop_option = int(input())
            if shop_option == 6:
                leave = True
            if shop_option == 1:
                if money >= infantry['price']:
                    troops.append(infantry)
                    money -= infantry['price']
                    print('You have purchased one infantry troop')
                    print('You now have ' + str(money) + ' gold coins')
                else:
                    print('You do not have enough money for this purchase')
            if shop_option == 2:
                if money >= shield['price']:
                    troops.append(shield)
                    money -= shield['price']
                    print('You have purchased one shield troop')
                    print('You now have ' + str(money) + ' gold coins')
                else:
                    print('You do not have enough money for this purchase')
            if shop_option == 3:
                if money >= archer['price']:
                    troops.append(archer)
                    money -= archer['price']
                    print('You have purchased one archer troop')
                    print('You now have ' + str(money) + ' gold coins')
                else:
                    print('You do not have enough money for this purchase')
            if shop_option == 4:
                if money >= cavalry['price']:
                    troops.append(cavalry)
                    money -= cavalry['price']
                    print('You have purchased one cavalry troop')
                    print('You now have ' + str(money) + ' gold coins')
                else:
                    print('You do not have enough money for this purchase')
            if shop_option == 5:
                if money >= ranged_cavalry['price']:
                    troops.append(ranged_cavalry)
                    money -= ranged_cavalry['price']
                    print('You have purchased one ranged cavalry troop')
                    print('You now have ' + str(money) + ' gold coins')
                else:
                    print('You do not have enough money for this purchase')
    else:
        pass

    return troops, money


def battle(troops, number_of_enemies, money):
    origional_enemies = number_of_enemies
    battle_over = False
    archers_under_attack = True
    while not battle_over:
        time.sleep(1)
        print('there are ' + str(number_of_enemies) + ' bandits left')
        time.sleep(1)
        print('Your army currently includes:')
        for print_troop in troops:
            print(print_troop['name'])
        print()
        time.sleep(1)
        if infantry in troops or shield in troops:
            archers_under_attack = False
        for troop in troops:
            troop_alive = True
            enemy = 1
            while enemy <= number_of_enemies and troop_alive:
                troop_under_attack = True
                if troop['damage'] > random.random()*1000:
                    print(troop['name'] + ' killed one of the bandits')
                    time.sleep(1)
                    number_of_enemies -= 1
                if troop['name'] == 'Archer' and archers_under_attack == False:
                    troop_under_attack = False
                if troop_under_attack and number_of_enemies >= 1:
                    if (random.random() * troop['speed']) < 5:
                        if (random.random() * troop['health']) < 5:
                            troop_alive = False
                            troops.remove(troop)
                            print(troop['name'] + ' was killed by one of the bandits')
                            time.sleep(1)
                enemy += 1

        if len(troops) <= 0:
            print('you lost the battle and the bandits have taken half of your gold')
            money = money//2
            battle_over = True
        if number_of_enemies <= 0:
            money_won = origional_enemies * random.randint(10, 100)
            print('you have won the battle and have recieved ' + str(money_won) + ' gold coins')
            money += money_won
            battle_over = True

    return troops, money


def main():

    all_troop_id = ['infantryID', 'shieldID', 'archerID', 'cavalryID', 'rangedcavalryID']
    all_troops = [infantry, shield, archer, cavalry, ranged_cavalry]

    print('Welcome to battle wars')
    print('Would you like to:')
    print('1 : Play a new game')
    print('2 : play save game')
    start_loop = True
    while start_loop:
        try:
            save_input = int(input())

            if save_input == 1:
                troops = []
                money = 1000
                start_loop = False

            elif save_input == 2:
                with open('save.txt') as f:
                    file_in = f.readlines()
                    f.close()
                in_troops = file_in[0]
                money = int(file_in[1])
                in_troops = in_troops.split()
                troops = []
                for troop in in_troops:
                    index = all_troop_id.index(troop)
                    troops.append(all_troops[index])
                start_loop = False
            else:
                print('Not valid input')


        except:
            print('not valid input')


    game_over = False

    while not game_over:

        print()
        print(f'You currently have {money} gold coins and you have the following troops:')
        for troop in troops:
            print(troop['name'])
        print()

        items_bought = enter_shop(troops, money, all_troops)
        troops = items_bought[0]
        money = items_bought[1]

        print()

        number_of_enemies = random.randint(1, 20)

        escaping_chance = 100 - ((number_of_enemies / 21) * 100)


        print(f'You have encountered {number_of_enemies} bandits would you like to:')
        print(f'1 : attempt escaping you have a {escaping_chance:.2f}% chance of escaping')
        print(f'2 : fight')
        fight_or_flee = int(input())

        if fight_or_flee == 1:
            escape_attempt = random.random() * 100
            if escape_attempt > (100 - escaping_chance):
                print('You escaped')
            else:
                print('You were unable to escape')
                fee = random.randint(100, 500)
                fee_choice = input('The bandits are offering a fee of ' + str(fee) + '. are you willing to pay (y if yes) '
                                                                   '(if not you will have to fight) ').lower()
                time.sleep(0.5)
                fight = True
                if int(fee) > int(money):
                    print('You are unable to pay the fee as you dont have enough money')
                else:
                    if fee_choice in ['y', 'yes']:
                        money -= fee
                        fight = False
                        print('You have paid the fee and the bandits have let you pass you now have ' + str(money)+ ' gold coins')

                time.sleep(0.5)
                if fight:
                    battle_results = battle(troops, number_of_enemies, money)
                    troops = battle_results[0]
                    money = battle_results[1]
        else:
            battle_results = battle(troops, number_of_enemies, money)
            troops = battle_results[0]
            money = battle_results[1]

        save_and_quit = input('Would you ike to save and quit (y if yes)? ').lower()
        if save_and_quit:
            f = open("save.txt", "w")
            for troop in troops:
                f.write(troop['id'])
                f.write(' ')
            f.write('\n')
            f.write(str(money))
            f.close()

if __name__ == '__main__':
    main()
