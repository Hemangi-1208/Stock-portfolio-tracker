# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0
portfolio = []

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        portfolio.append([stock, quantity, price, investment])

        print("Stock added successfully!")
        print("Investment for", stock, "=", investment)

    else:
        print("Stock not available. Please choose from the available stocks.")

# Display portfolio
print("\n===== PORTFOLIO SUMMARY =====")

for item in portfolio:
    print(
        "Stock:", item[0],
        "| Quantity:", item[1],
        "| Price:", item[2],
        "| Value:", item[3]
    )

print("\nTotal Investment Value =", total_investment)

# Save result in a text file
with open("portfolio.txt", "w") as file:
    file.write("===== STOCK PORTFOLIO =====\n\n")

    for item in portfolio:
        file.write(
            f"Stock: {item[0]} | Quantity: {item[1]} "
            f"| Price: {item[2]} | Value: {item[3]}\n"
        )

    file.write("\nTotal Investment Value = " + str(total_investment))

print("\nPortfolio saved successfully in portfolio.txt")