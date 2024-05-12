import pandas as pd

fruits = pd.DataFrame(columns=['Apples', 'Bananas'])

fruits_data = {
        "Apples" :[35],
        "Bananas" :[21]
}

pd.DataFrame(fruits_data)

fruit_sales = pd.DataFrame({
    "Apples": [35, 41],
    "Bananas": [21,34]},
    index = ["2017 Sales", "2018 Sales"])

print(fruit_sales)

fruit_sales.to_csv("fruit.csv", index=True)
