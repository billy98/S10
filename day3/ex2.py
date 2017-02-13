def run():
    for i in range(100):
        print i
        yield i

task = run()

task.next()
print '-----do sth else-----'
task.next()
print '-----do sth else-----'
task.next()
print '-----do sth else-----'
task.next()
print '-----do sth else-----'


print [i for i in range(10) if i<5]