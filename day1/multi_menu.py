
menu = {
    'Beijing':{
        'ChaoYang':{
            'CBD': ['CICC','CCTV'],
            'JinRongJie': ['Momo','ChuiZi']
        },
    'HaiDian': ['Baidu','YouKu']
    },

    'ShangHai':{
        'PuDong':['Ctrip','1 shop'],
        'PuXi':['China Bank','America Bank']
    }
}
#33999
exit_flag = False
while not exit_flag:
    for index,key in enumerate(menu.keys()):
        print index,key
    choice_1 = raw_input('please choose menu to enter:').strip()
    if choice_1.isdigit():
        choice_1 = int(choice_1)
        key_1 = menu.keys()[choice_1]
        while not exit_flag:
            for index,key in enumerate(menu[key_1]):
                print '-->',index,key
            choice_2 = raw_input('please choose menu to enter:').strip()
            if choice_2.isdigit():
                choice_2 = int(choice_2)
                key_2 = menu[key_1].keys()[choice_2]
                while not exit_flag:
                    for index,key in enumerate(menu[key_1][key_2]):
                        print '-->-->',index,key
                    choice_3 = raw_input('please choose menu to enter:').strip()
                    if choice_3.isdigit():
                        print 'this is the last level...'
                    elif choice_3 == 'quit':
                        exit_flag = True
                    elif choice_3 == 'back':
                        break
else:
    print '====going to quit===='
