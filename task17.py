a = input('some text: ')
if a == 'Hello':
    b = {1: 'google_kazahstan.txt',
    2: 'google_paris.txt',
    3: 'google_uar.txt',
    4: 'google_kyrgyzstan.txt',
    5: 'google_san-francisco.txt',
    6: 'google_germany.txt',
    7: 'google_moscow.txt',
    8: 'google_sweden.txt'
    }
    print(b)

s = int(input('choose one file: '))
text = input('This text will printed in file: ')
if s == 1:
    with open('google_kazahstan.txt', 'w') as file_object:
        file_object.write(text)
elif s == 2:
    with open('google_paris.txt', 'w') as file_object:
        file_object.write(text)
elif s == 3:
    with open('google_uar.txt', 'w') as file_object:
        file_object.write(text)
elif s == 4:
    with open('google_kyrgyzstan', 'w') as file_object:
        file_object.write(text)
elif s == 5:
    with open('google_san-francisco.txt', 'w') as file_object:
        file_object.write(text)
elif s == 6:
    with open('google_germany', 'w') as file_object:
        file_object.write(text)
elif s == 7:
    with open('google_moscow', 'w') as file_object:
        file_object.write(text)
elif s == 8:
    with open('google_sweeden', 'w') as file_object:
        file_object.write(text)
    print(text)