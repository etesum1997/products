# 那大清單可以直接products = [[name, price]]嗎？不行（原因如下）
# 存成二維清單才可以方便分組
products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q': 
        break
    price = input('請輸入商品價格：')
    products.append([name, price])
print(products)
# 本來要先在loop裡建立一個小清單p
# 再把name跟price分別加入p：p.append(name), p.append(price)
# 再把p加入products：products.append(p)
# 但可以直接：p = [name, price]
# 或甚至可以：products.append([name, price])
# 但不可以直接寫：products = [[name, price]]，因為這樣會變成只顯示最後一筆，會被while loop洗掉，沒辦法累積進本來的大清單讓它變長