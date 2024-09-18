favorite_languages = {
 'jen': ['python', 'rust'],
 'sarah': ['c'],
 'edward': ['rust', 'go'],
 'phil': ['python', 'haskell'],
 }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}")
    for language in languages:
        print(f"\t{language.title()}")
