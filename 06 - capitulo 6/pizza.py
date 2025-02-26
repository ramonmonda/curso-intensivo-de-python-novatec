# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    "borda": "espessa",
    "coberturas": [ "cogumelos", "queijo extra"],
}

# Resume o pedido
print(f"Você pediu uma pizza de borda {pizza['borda']}, " 
      "com as seguintes coberturas:")

for cobertura in pizza["coberturas"]:
    print(f"{cobertura}")

