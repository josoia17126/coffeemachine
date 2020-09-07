#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:40:36 2020

@author: apple
"""
water1 = 400
milk1 = 540
coffee_beans1 = 120
disposable_cups1 = 9
money1 = 550
list1 = ['water', 'milk', 'coffee beans', 'disposable cups']
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - to main menu:')
        b = input()
        if b == '1':
            if water1 >= 250 and coffee_beans1 >= 16 and disposable_cups1 >= 1:
                print('I have enough resources, making you a coffee!')
                water1 = water1 - 250
                coffee_beans1 = coffee_beans1 - 16
                disposable_cups1 = disposable_cups1 - 1
                money1 = money1 + 4
                
            else:
                list_ = [water1 < 250, False, coffee_beans1 < 16, disposable_cups1 < 1]
                for i in range(4):
                    if list_[i] == True:
                        print('Sorry, not enough ' + list1[i] + '!')
                        
        elif b == '2':
            if water1 >= 350 and milk1 >= 75 and coffee_beans1 >= 20 and disposable_cups1 >= 1:
                print('I have enough resources, making you a coffee!')
                water1 = water1 - 350
                milk1 = milk1 - 75
                coffee_beans1 = coffee_beans1 - 20
                disposable_cups1 = disposable_cups1 - 1
                money1 = money1 + 7
                
            else:
                list_ = [water1 < 350, milk1 < 75, coffee_beans1 < 20, disposable_cups1 < 1]
                for i in range(4):
                    if list_[i] == True:
                        print('Sorry, not enough ' + list1[i] + '!')
                        
        elif b == '3':
            if water1 >= 200 and milk1 > 100 and coffee_beans1 >= 12 and disposable_cups1 >= 1:
                print('I have enough resources, making you a coffee!')
                water1 = water1 - 200
                milk1 = milk1 - 100
                coffee_beans1 = coffee_beans1 - 12
                disposable_cups1 = disposable_cups1 - 1
                money1 = money1 + 6
                
            else:
                list_ = [water1 < 200, milk1 < 100, coffee_beans1 < 12, disposable_cups1 < 1]
                for i in range(4):
                    if list_[i] == True:
                        print('Sorry, not enough ' + list1[i] + '!')
                        
        else:
            continue
    elif action == 'fill':
        print('Write how many ml of water do you want to add:')
        c = int(input())
        print('Write how many ml of milk do you want to add:')
        d = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        e = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        f = int(input())
        water1 = c + water1
        milk1 = d + milk1
        coffee_beans1 = e + coffee_beans1
        disposable_cups1 = f + disposable_cups1
        
    elif action == 'take':
        print('I gave you $' + str(money1))
        money1 = 0
    elif action == 'remaining':
        print('The coffee machine has:')
        print(str(water1) + ' of water')
        print(str(milk1) + ' of milk')
        print(str(coffee_beans1) + ' of coffee beans')
        print(str(disposable_cups1) + ' of disposable cups')
        print('$' + str(money1) + ' of money')
        
    else:
        exit()
                    