import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple','mango','bannana','chikku']

f = open(shoplistfile, 'wb')
#dump object to the file
pickle.dump(shoplist, f)
f.close()
#destroy shoplist variable
del shoplist
#read back from the storage
f = open(shoplistfile, 'rb')
#load object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()
