
from methods import load_file, save_file


products = load_file("data/products.json")
print(products)

data = load_file("data/user.json")
data.append({"name": "Test"})
save_file("data/user.json", data)