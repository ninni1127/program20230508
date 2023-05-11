# 硬貨リスト
coins = [500, 100, 50, 10, 5, 1]

# 金額の入力
def input_money():
   i = 0
   while True:
      inputMoney = input("金額を入力してください：")
      if inputMoney.isdigit():
        intMoney = int(inputMoney)
        return intMoney
        break
      print("整数値を入力してください。")
      i = i + 1
      if i >= 5:
         print('入力回数の上限をオーバーしたため、終了します。')
         break

# 最小枚数の算出
def count_coins(money):
   result = 0
   for coin in coins:
      if money >= coin:
         num = int(money / coin)
         result = result + num
         money = money - coin * num
   return result

money = input_money()
if money is not None:
   message = "金額：{:,}円, 硬貨の最小枚数：{:,}枚".format(money, count_coins(money))
   print(message)