# 那大清單可以直接products = [[name, price]]嗎？不行（原因如下）
# 存成二維清單才可以方便分組
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue # 像玩遊戲pass這一輪一樣，直接跳到下一個line繼續loop
        name, price = line.strip().split(',') # 把換行符號去掉＋看到逗點就切成另一塊
        products.append([name, price])
print(products)
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

with open('products.txt', 'w') as f: # 上面東西執行完後能直接寫出txt/csv檔並產生檔案
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 字串可以相加相乘

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n') # 當有不同屬性的東西要一起存的時候會用csv檔，像很多政府表格中央氣象局等的資料
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 逗點有分格的作用
# 不同資料型別不能做加或乘，所以如果把price = int(price)了，下面的字串相加部分就要改成str(p[1])