#coding:utf8
#装饰器练习

#如果有3000个函数，而每个函数都需要加入验证（auth），可以通过装饰器来设置

def auth(func):
    def wrapper(arg):
        user = raw_input('input passwd:').strip()
        if user == 'alex':
            print '---welcome login---'
            return func(arg)
        else:
            print '---wrong passwd access denied!---'
    return wrapper

@auth       # @auth的作用相当于task = auth(task)
def task(name):
    print 'do something...',name
    return name

res = task('task 2222')

print '==>',res