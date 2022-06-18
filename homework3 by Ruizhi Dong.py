#Task-1 Q1
'''
raining = input('Is it raining? y/n')
if raining == 'y' :
    print('Take an umbrella')
elif raining == 'n' :
    print("You don't need an umbrella")
'''

#Task-1 Q2 It should be changed as
'''
my_money = input('How much money do you have? ')
boat_cost = 20 + 5

if int(my_money) >= boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')
'''

#Task-1 Q3
'''
Year_of_book = input('Which year was it published?')
century = int(Year_of_book) // 100
decade_1 = int(Year_of_book) // 10
decade = decade_1 % 10
if century == 18:
    century_of_book = 'Nineteenth Century'
elif century == 19:
    century_of_book = 'Twentieth Century'

if decade == 0:
    decade_of_book = '00s'
elif decade == 1:
    decade_of_book = '10s'
elif decade == 2:
    decade_of_book = 'twenties'
elif decade == 3:
    decade_of_book = 'thirties'
elif decade == 4:
    decade_of_book = 'fourties'
elif decade == 5:
    decade_of_book = 'fifties'
elif decade == 6:
    decade_of_book = 'sixties'
elif decade == 7:
    decade_of_book = 'seventies'
elif decade == 8:
    decade_of_book = 'eighties'
elif decade == 9:
    decade_of_book = 'nineties'

print(century_of_book , ',' , decade_of_book)
'''

#Task-2 Q1
#The reason is that the items in a list was ordered from 0, so if you want to output the first one in your shopping list, you should set as 0 when you print.
'''
shopping_list = ["oranges", "cat food", "sponge cake", "long-grain rice", "cheese board"]
print(shopping_list[0])
'''

#Task-2 Q2
'''
chocolates = {

	'white': 1.50,

	'milk': 1.20,

	'dark': 1.80,

	'vegan': 2.00,

}

customer_wants = input('which kind of chocolates do you want?')
print (chocolates[customer_wants])
'''

#Task-2 Q3
'''
import random
count = 0
numbers_1 = [random.randint(0,10) for x in range(7)]
numbers_2 = [random.randint(0,10) for x in range(7)]
print(numbers_1, numbers_2)
for i in range(len(numbers_1)) :
    for j in range(len(numbers_2)) :
        if numbers_1[i] == numbers_2[j]:
            count = count +1
if count == 3:
    print('£20')
elif count == 4:
    print('£30')
elif count == 5:
    print('£40')
elif count == 6:
    print('£50')
elif count == 7:
    print('£60')
'''

#Task-3 Q1
'''
Pip is a package management system used to install and manage software packages written in Python.we need to install pip itself first, which would allow us to install new packages in Python in the future.
A package contains all the files you need for a module.Modules are Python code libraries you can include in your project.
One major advantage of pip is the ease of its command-line interface, which makes installing Python software packages as easy as issuing a command.
'''

#Task-3 Q2
#The mistake is about the difference between 'r' and 'w'. 'r' means 'read', 'w' means 'write'. So in this program, we should use 'w' rather than 'r'.
'''
poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)
'''

#Task-3 Q3
'''
Song = " You could never know what it \'s like \n Your blood like winter freezes just like ice \n And there\'s a cold lonely light that shines from you \n You\'ll wind up like the wreck you hide behind that mask you use \n \n And did you think this fool could never win? \n Well look at me, I\'m coming back again \n I got a taste of love in a simple way\n And if you need to know while I\'m still standing, you just fade away\n \n Don't you know I\'m still standing better than I ever did\n Looking like a true survivor, feeling like a little kid\n I\'m still standing after all this time\n Picking up the pieces of my life without you on my mind \n \n I\'m still standing (Yeah, yeah, yeah)\n I\'m still standing (Yeah, yeah, yeah)"
with open('Song.txt', 'w') as Song_file:
    Song_file.write(Song)
with open('Song.txt', 'r') as Song_file:
    lines = Song_file.readlines()
    stripped_lines = [line.strip() for line in lines]

    for item in stripped_lines:
        if 'still' in item:
            print(item)
'''

#Task-4 Q1
import requests
list_pokemon = []
list_name = []
for i in range(6) :
    pokemon_number = input("What is the Pokemon's ID? ")
    list_pokemon.append(pokemon_number)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    list_name.append(pokemon['name'])
    moves = pokemon['moves']
    with open('pokemon.txt', 'a+') as pokemon_file:
        pokemon_file.write('\n'+pokemon['name']+'\n')
    for move in moves:
        with open('pokemon.txt', 'a+') as pokemon_file:
            pokemon_file.write(move['move']['name'])
print(list_pokemon, list_name)
