shop_list = {
    "piekarnia": ["chleb", "bułki", "pączek", "bagetka"],
    "warzywniak": ["marchew", "seler", "rukola", "ogórek"]
}
sum = 0
for name, product_list in shop_list.items():
    print(f"Idę na zakupy do: {name.capitalize()}, i kupuję tam następujące produkty: {[product.capitalize() for product in product_list]}")
    sum += len(product_list)
print(f"W sumię kupuję {sum} produktów")

print("Maciek to jest gość ale nieźle daje w kość")
