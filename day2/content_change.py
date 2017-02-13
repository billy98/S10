#_*_ coding:utf-8 _*_
import sys
if '-r' in sys.argv:
    rep_pos = sys.argv.index('-r')
    #-r 的位置
    old_str = sys.argv[rep_pos +1]
    #被替换内容的位置
    new_str = sys.argv[rep_pos +2]
    #替换后内容的位置

f = file('passwd','r+')
#以读写打开文件passwd
while True:
    line = f.readline()
    if old_str in line:
        last_pos = f.tell() - len(line)
        #找到包含old_str变量内容的行的行头位置
        f.seek(last_pos)
        #切换到该行头位置
        new_line = line.replace(old_str,new_str)
        #将new_str的内容替换old_str，并赋给new_line
        f.write(new_line)
        #写入文件
        break
f.close()
#关闭文件
