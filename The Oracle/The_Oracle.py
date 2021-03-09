the_begining = 'The Oracle: Life is a game. The point of life is to die. Prove me wrong!'




def life_source_selector():
    print(the_begining)
    print('Press enter...')
    input()
    print('What is your life source?\n Light or Dark')
    life_source = input()
    if life_source == 'light' or life_source == 'Light' or life_source == 'dark' or life_source == 'Dark':
        life_source = life_source.capitalize()
        print(f'Your life source is {life_source}.')
        if life_source == 'Dark':
            print('Beings of darkness are dark black shadowy figures. They\'re lives are forfit. They\'re meaning\n of existence is to finally anilate every being of light in the galaxy in a war that has been waging on for\n thousands of light years.\nPress enter to continue...')
            input()
            return life_source
        if life_source == 'Light':
            print('Beings of light are bright white shadowy figures. They\'re lives are forfit. They\'re meaning\n of existence is to finally anilate every being of darkness in the galaxy in a war that has been waging on for\n thousands of light years.\nPress enter to continue...')
            input()
            return life_source
        else:
            print(life_source_selector)




the_war = "It all started on the day of cahorlian. On a world called earth. A race called humanity evolved to a\n point of no return. A being from that race called Cahorlian started the war between Humanities starsystem factions.\n Dividing the galaxy into light and dark. Light and Dark beings then waged a galatic war that aqupied a\n larg but small portian of the milky way ever sense.\n Press enter to continue..."

def star_system_faction_selector():
    print(the_war)
    print("The galaxy is now is now mostly devided into three different starsystem factions. Whick one are you?\n \nVestroy   Formil   Latorian")
    star_system_faction = input()
    if star_system_faction == 'Vestroy' or star_system_faction == 'vestroy' or star_system_faction == 'Formil' or star_system_faction == 'formil' or star_system_faction == 'Latorian' or star_system_faction == 'latorian':
        star_system_faction = star_system_faction.capitalize()
        star_system_faction = star_system_faction.append('s')
        print(f"You'r faction, the {star_system_faction}")
    else:
        print(star_system_faction_selector)





life_source = life_source_selector()
star_system_faction_selector()



















# o1 = 'You once told me that absence my presence life is meaningless. Was it not a lie?'

# print(o1)


















# the_begining = 'The Oracle: Life is a game. The point of life is to die. Prove me wrong!'

# print(the_begining)

# def life_source_selector():
#     print('What is your life source?\n Light or Dark')
#     life_source = input()

#     if life_source == 'light' or life_source == 'Light' or life_source == 'dark' or life_source == 'Dark':
#         life_source = life_source.capitalize()
#         print(f'Your life source is {life_source}.')
#         return life_source
#         if life_source == 'Dark':
#             print('Beings of darkness are dark black shadowy figures. They\'re lives are forfit. They\'re meaning of existence is to finally anilate every being of light in the galaxy in a war that has been waging on for thousands of light years.)
#             input()
#             return life_source
#         if life_source == 'Light':
#             print('Beings of light are bright white shadowy figures. They\'re lives are forfit. They\'re meaning of existence is to finally anilate every being of darkness in the galaxy in a war that has been waging on for thousands of light years.)
#             input()
#             return life_source
#         else print(life_source_selector)



# life_source_selector()



















# o1 = 'You once told me that absence my presence life is meaningless. Was it not a lie?'

# print(o1)
























