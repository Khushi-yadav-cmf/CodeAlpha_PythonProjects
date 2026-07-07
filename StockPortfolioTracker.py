
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

total_investment = 0
result = []

print("📈 Stock Investment Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    result.append(f"{stock} - Quantity: {quantity}, Price: ${stock_prices[stock]}, Total: ${investment}")

print("\n----- Investment Summary -----")
for item in result:
    print(item)

print(f"\n💰 Total Investment Value: ${total_investment}")


with open("investment_summary.txt", "w") as file:
    file.write("Investment Summary\n")
    file.write("----------------------\n")

    for item in result:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n✅ Summary saved to 'investment_summary.txt'")