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
print(products[0][0])
# 本來要先在loop裡建立一個小清單p
# 再把name跟price分別加入p：p.append(name), p.append(price)
# 再把p加入products：products.append(p)
# 但可以直接：p = [name, price]
# 或甚至可以：products.append([name, price])
# 但不可以直接寫：products = [[name, price]]，因為這樣會變成只顯示最後一筆，會被while loop洗掉，沒辦法累積進本來的大清單讓它變長

# 用for loop搞清楚每個東西代表什麼：
for p in products: # 一個一個拿出大清單的物件：就是拿出小清單（name+price組合）
    print(p) # 表示印出小清單
for p in products:
    print(p[0]) # 表示印出小清單的第一個東西，也就是name
for p in products:
    print(p[0], '的價格是', p[1]) # 商品名稱的價格是商品價格