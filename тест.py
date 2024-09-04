def make_profit(number):
  profit = number * 3
  if profit == 21:
    print("Broke even")
  elif profit > 21:
    print("Profit")
  else:
    print("Loss")

if __name__ == "__main__":
  make_profit(7)