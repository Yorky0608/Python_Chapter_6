favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

poll = ['jen', 'jack', 'paul', 'luke', 'phil']

for name in poll:
    if name in favorite_languages:
        print(f"\n{name.title()}, thank you for taking the poll.")
    else:
        print(f"\n{name.title()}, please take the poll.")