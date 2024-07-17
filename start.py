import json

# Wczytaj dane z pliku JSON
with open('./filmy.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Funkcja do generowania komend Redis dla każdego filmu
def generate_redis_commands(films):
    commands = []
    for i, film in enumerate(films, start=1):
        film_id = f"film:{i}"
        commands.append(f"HSET {film_id} name \"{film['name']}\"")
        commands.append(f"HSET {film_id} year \"{film['year']}\"")
        commands.append(f"HSET {film_id} description \"{film['description']}\"")
        genres = ", ".join(film['genres'])
        commands.append(f"HSET {film_id} genres \"{genres}\"")
        commands.append(f"HSET {film_id} poster_url \"{film['poster_url']}\"")
    return commands

# Generowanie komend Redis
redis_commands = generate_redis_commands(data)

# Zapisz komendy do pliku tekstowego
with open('./filmy_redis.txt', 'w', encoding='utf-8') as file:
    for command in redis_commands:
        file.write(command + '\n')

print("Konwersja zakończona. Komendy Redis zapisane w 'filmy_redis.txt'.")
