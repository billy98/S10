#coding:utf8
#递归练习
#这是一个二分查找脚本

data_list = range(0,10000,2)
def binary_seach(find_num,data):
    mid = len(data)/2
    if mid >0:
        if find_num>data[mid]:
            binary_seach(find_num,data[mid:])
        elif find_num<data[mid]:
            binary_seach(find_num,data[:mid])
        else:
            print 'find the num:%s' % data[mid]
    elif data[0] == find_num:
        print 'find the num:%s' % data[mid]
    else:
        print 'cannot find the num',find_num


if __name__ == '__main__':
    find_n = raw_input('find:').strip()
    if find_n.isdigit():
        find_n = int(find_n)
        binary_seach(find_n,data_list)



