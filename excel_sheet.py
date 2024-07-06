import pandas as pd

data = {
    "Item ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    "Item Name": ["T-Shirt", "Jeans", "Jacket", "Skirt", "Dress", "Blouse", "Sweater", "Shorts", "Coat", "Polo Shirt", "Trousers", "Cardigan", "Hoodie", "Tank Top", "Vest", "Blazer", "Socks", "Scarf", "Gloves", "Hat", "Cap", "Shoes", "Sandals", "Boots", "Sneakers", "Belt", "Tie", "Swimsuit", "Raincoat", "Suit", "Pajamas", "Leggings", "Tunic", "Overalls", "Poncho", "Kimono", "Sarong", "Shawl", "Culottes", "Joggers"],
    "Category": ["Tops", "Bottoms", "Outerwear", "Bottoms", "Dresses", "Tops", "Tops", "Bottoms", "Outerwear", "Tops", "Bottoms", "Outerwear", "Outerwear", "Tops", "Tops", "Outerwear", "Accessories", "Accessories", "Accessories", "Accessories", "Accessories", "Footwear", "Footwear", "Footwear", "Footwear", "Accessories", "Accessories", "Swimwear", "Outerwear", "Outerwear", "Sleepwear", "Bottoms", "Tops", "Outerwear", "Outerwear", "Outerwear", "Accessories", "Accessories", "Bottoms", "Bottoms"],
    "Quantity": [50, 30, 20, 40, 25, 35, 15, 60, 10, 55, 25, 20, 18, 45, 22, 12, 100, 70, 80, 30, 40, 25, 20, 15, 50, 75, 65, 28, 10, 12, 40, 38, 35, 18, 22, 15, 25, 28, 40, 30],
    "Price per Unit": [10, 25, 50, 20, 40, 15, 30, 20, 60, 15, 25, 35, 40, 10, 8, 55, 5, 12, 10, 15, 12, 40, 20, 50, 60, 10, 8, 25, 80, 100, 15, 20, 30, 40, 35, 55, 10, 20, 30, 25],
    "Total Sales": [500, 750, 1000, 800, 1000, 525, 450, 1200, 600, 825, 625, 700, 720, 450, 176, 660, 500, 840, 800, 450, 480, 1000, 400, 750, 3000, 750, 520, 700, 800, 1200, 600, 760, 1050, 720, 770, 825, 250, 560, 1200, 750]
}


df = pd.DataFrame(data)

print(df)

total_sales_per_category = df.groupby("Category")["Total Sales"].sum()
print("\nTotal sales per category:")
print(total_sales_per_category)

avg_price_per_category = df.groupby("Category")["Price per Unit"].mean()
print("\nAverage price per unit per category:")
print(avg_price_per_category)

high_sales_items = df[df["Total Sales"] > 1000]
print("\nItems with sales greater than $1000:")
print(high_sales_items)
