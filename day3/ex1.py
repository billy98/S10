def sayhi(*arg):
    print arg
sayhi('g1','g2','g3')


def sayhi(**kwargs):
    print kwargs
sayhi(name='billy',agr='18',job='IT')


print map(lambda x:x**2,range(10))


dic1 = {3:9,
        5:6,
        'b':'test',
        'g':'sunfo',
        '*':'$'
        }

print sorted(dic1.items(),key=lambda x:x[0])