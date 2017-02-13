import pickle

dic1={'name':'billy','age':'18','job':'IT'}

f = file('test.pkl','w')

pickle.dump(dic1,f)

f.close()