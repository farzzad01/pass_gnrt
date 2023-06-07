
import random
import string

settings = {     
    'lower':True,
    'upper': True,
    'number':True,
    'symbol':True,
    'space': False,
    'length': 8
}

def get_pass_length(option,default, pw_min=4, pw_max=30):
    while True:
        user_input = input('enter pass length '
                            f'(default is {default} (enter = default)-> ') 
        if user_input == '':
            return default
        if user_input.isdigit():
            user_pass_length = int(user_input)
            if pw_min <= user_pass_length <= pw_max:
                return int(user_input)
            print('please try again.')
            print(f'password length should be between {pw_min} and {pw_max}')
        else:
            print('invalid input you should enter a number')

def get_yes_or_no(option,default):
    while True:
        user_input = input(f'include {option} ? '
                           f'default is {default}  (y : yes , n: no , enter:default ) ')
        if user_input == '':
            return default
        if user_input in ['y','n']:
            return user_input == 'y'
        print('invalid input')

        # if user_input =='y' or user_input == 'n':
        #     if user_input =='y':
        #         return True
        #     else:
        #         return False

        #     print('invalid input')



def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no(option , default)
            settings[option] = user_choice
        else:
            user_pass_length = get_pass_length(option, default)
            settings[option] = user_pass_length    
    


def generate_random_char(choices):
    choice = random.choice(choices)
    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    if choice == 'symbol':
        return random.choice(string.punctuation)
    if choice == 'number':
        return random.choice(string.digits)
    if choice == 'space':
        return ' '


def password_genrator(settings):
    final_pass = ''
    password_length = settings['length']
    
    choices = list(filter(lambda x: settings[x] == True, ['upper', 'lower','symbol','number','space']))
    
    # choices = []
    # for key, value in settings.items():
    #     if value == True and key != 'length':
    #         choices.append(key)

    for i in range(password_length):
        final_pass += generate_random_char(choices)
    return final_pass

get_setting_from_user(settings)
print(password_genrator(settings))


