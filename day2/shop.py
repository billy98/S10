products = [
    ['iphone',5800],
    ['ipad',4000],
    ['tesla',800000],
    ['coffee',35],
    ['clothes',500],
    ['shoes',800]
]

salary = 9000
shop_list = []
while True:
    for index,p in enumerate(products):
        print index,p[0],p[1]
    choice = raw_input('Choose sth to buy:').strip()
    if choice.isdigit():
        choice = int(choice)
        print products[choice]
        p_price = products[choice][1]
        if p_price < salary:
            shop_list.append(products[choice])
            salary -= p_price
            print 'Has added \033[31;1m%s\033[0m into shop list,your current balance is \033[31;1m%s\033[0m' %(products[choice][0],salary)
        else:
            print '\033[31;1m Money is not enough,get the fuck out \033[0m'

    elif choice == 'quit':
        print '---------shpping list---------'
        for k,v in enumerate(shop_list):
            print k,v
        print 'Your current balance is \033[31;1m%s\033[0m' % salary
        print '---------------end-------------'
        break