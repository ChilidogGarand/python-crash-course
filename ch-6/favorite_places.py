# exercise 6-9 on p112

favorite_places = {
    'chilidog': ['dinosaur valley state park', 'boston', 'albuquerque',],
    'spaghetti': ['las vegas', 'fresno', 'poland',],
    'john': ["harper's ferry", 'osawatomie', 'conneticuit',]
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")