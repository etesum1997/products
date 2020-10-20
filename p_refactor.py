import os 

# 讀取檔案
def read_file(filename): # 檔名建議改成參數，這樣就可以投入不同檔案
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 像玩遊戲pass這一輪一樣，直接跳到下一個line繼續loop
            name, price = line.strip().split(',') # 把換行符號去掉＋看到逗點就切成另一塊
            products.append([name, price])
    return products # 因為有加東西進products，所以要回傳出來
# 讓使用者輸入
def user_input(products): # 因為def的每段程式是獨立的，又下面這段程式沒有定義products，所以要設定參數，不然他不知道那是啥
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q': 
            break
        price = input('請輸入商品價格：')
        products.append([name, price])
    print(products)
    return products # 因為有加東西進products，所以要回傳

# 印出所有購買紀錄
def print_products(products):
    for p in products: 
        print(p) 

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n') 
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') 

# 分別使用4個function
def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在，這個只執行一次，不會重複執行，所以可以直接寫在下面就好
        print('yeah！找到檔案了')
        products = read_file(filename) # 有return，function的執行結果就可以存下來
    else:
        print('找不到檔案')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)
main()

# function的中心思想是只做一件事！