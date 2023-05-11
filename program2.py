# 硬貨リスト
coins = {500:8,
         100:5,
         50:1,
         10:4,
         1:9}

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
   for coin, value in coins.items():
      if money >= coin:
         num = int(money / coin)
         if num > value:
            num = value
         result = result + num
         money = money - coin * num
   if money > 0:
      error_message = "硬貨が不足しています。【不足分の金額：{:,}円】".format(money)
      print(error_message)
   else:
      return result

money = input_money()
if money is not None:
   result_coins = count_coins(money)
   if result_coins is not None:
      message = "金額：{:,}円, 硬貨の最小枚数：{:,}枚".format(money, result_coins)
      print(message)