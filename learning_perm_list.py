import pickle

#list = [1,2,3,4]

#with open("test.txt","wb") as fp:
#    pickle.dump(list, fp)

with open("test.txt", "rb") as fp:
    b = pickle.load(fp)

print(b)