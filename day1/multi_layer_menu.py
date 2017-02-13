data = {
    'name' : 'alex',
    'age' : 18,
    'job' : 'CEO'
}

del data['job']
print data['name']
print data['age']
print data

if data.has_key('info'):
    print data['info']

print data.get('name')

for key in data:
    print key,data[key]
