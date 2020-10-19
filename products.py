import os # operating system

# 讀取檔案
products = []
if os.path.isfile('products.csv'):
    print('yeah！找到檔案了')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 像玩遊戲pass這一輪一樣，直接跳到下一個line繼續loop
            name, price = line.strip().split(',') # 把換行符號去掉＋看到逗點就切成另一塊
            products.append([name, price])
    print(products)
else:
    print('找不到檔案')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q': 
        break
    price = input('請輸入商品價格：')
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products: # 一個一個拿出大清單的物件：就是拿出小清單（name+price組合）
    print(p) # 表示印出小清單

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n') # 當有不同屬性的東西要一起存的時候會用csv檔，像很多政府表格中央氣象局等的資料
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # 逗點有分格的作用
# 不同資料型別不能做加或乘，所以如果把price = int(price)了，下面的字串相加部分就要改成str(p[1])