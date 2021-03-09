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
            print('Beings of darkness are dark black shadowy figures. They\'re lives are forfit. They\'re meaning of existence is to finally anilate every being of light in the galaxy in a war that has been waging on for thousands of light years.')
            input()
            return life_source
        if life_source == 'Light':
            print('Beings of light are bright white shadowy figures. They\'re lives are forfit. They\'re meaning of existence is to finally anilate every being of darkness in the galaxy in a war that has been waging on for thousands of light years.')
            input()
            return life_source
        else:
            print(life_source_selector)




























life_source = life_source_selector()
gender = gender_selector()




# o1 = 'You once told me that absence my presence life is meaningless. Was it not a lie?'

# print(o1)
























