import json

# Məlumatı fayldan yüklə
try:
    with open('birthdays.json', 'r') as file:
        birthdays = json.load(file)
except FileNotFoundError:
    birthdays = {}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

    # Hər dəfə yeni məlumat əlavə ediləndə faylı yenilə
    with open('birthdays.json', 'w') as file:
        json.dump(birthdays, file, indent=4)

print('All birthdays saved. Bye!')
