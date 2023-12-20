import pickle

data = {
    "name": "Joe Chen",
    "age": 22,
    "score": 95,
}
with open("dic.dat", "wb") as f:
    pickle.dump(data, f)
with open("dic.dat", "rb") as f:
    new_data = pickle.load(f)
print(new_data)    
