# Exemplo básico de introduzir dicionários em listas

# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yellow", "points": 10}
# alien_2 = {"color": "red", "points": 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


# Exemplo básico de como criar muitos aliens
aliens = []

# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Exibe os primeiros 5 alienígenas
for alien in aliens[:5]:
    print(alien)

print("...")

# Exibe quantos alienígenas foram criados
print(f"Total de aliens criados: {len(aliens)}.")

# Mudando a cor dos alienígenas
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)

print("...")

