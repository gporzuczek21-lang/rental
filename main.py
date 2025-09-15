from datetime import date
from faker import Faker
fake=Faker()
import random

class Movis:
    def __init__(self, title, yers, genre):
        self.title = title
        self.yers = yers
        self.genre = genre
        self.plays = 0

    def __str__(self):
        return f"{self.title} {self.yers}"
    
    def play(self):
       self.plays += 1
    
class Series(Movis):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"
        
def creator_library(how_many):
    library = []
    genres = ["komedia", "dramat", "horror", "science fiction", "akcja", "thriller", "western"]
    for i in range(0,how_many):
        i = Movis(title=fake.word().title(), yers=random.randint(1895, 2025), genre = random.choice(genres))
        library.append(i)
        i = Series(title=fake.word().title(), yers=random.randint(1895, 2025), genre = random.choice(genres), season = random.randint(1,15), episode = random.randint(1,24))
        library.append(i)    
    return library

def get_movies(rental):
    filmy = [s for s in rental if not isinstance(s,Series)]
    filmy.sort(key = lambda Movies:Movies.title)
    return filmy            
    
def get_series(rental):
    seriale = [s for s in rental if isinstance(s, Series)]   
    seriale.sort(key = lambda Series:Series.title)
    return seriale
    
def generate_views(rental):
    lotto = random.choice(rental)
    los = random.randint(1, 100)
    lotto.plays += los
    
def generate_views10(rental):
    for i in range(10):
        generate_views(rental)   

def top_titles(rental):
    how = int(input("Podaj ile tytułów mam wyświetlić: "))
    top = sorted(rental, key=lambda ren:ren.plays, reverse=True)
    najj = (top[:how])
    return najj

def search(rental):
    element = input("podaj szykany tytuł: ")
    szukana = (obj for obj in rental if obj.title == element)
    return szukana 

if __name__=='__main__':
    today = date.today()
    print("Biblioteka Filmów:")
    rental = creator_library(5)
    for r in rental:
        print(r)

    generate_views10(rental)
   
    print(f"Najpopularniejsze filmy i seriale dnia {today.day}.{today.month}.{today.year}")
    toop=top_titles(rental)
    for t in toop:
        print(t)

   
    szuk =search(rental)
    for s in szuk:
        print(s)

