from passlib.hash import pbkdf2_sha256
import uuid
import pymongo

username = "Allocative"
password = "DeepReinorcementLearningProject"

srv = "mongodb+srv://{}:{}@supplychain-u6nhl.mongodb.net/test?retryWrites=true&w=majority".format(
    username, password)
client = pymongo.MongoClient(srv)

db = client['Allocative']

LoginCollection = db['Auth']


def Register(email,name,password):
    q1 = {"email":email}

    result1 = LoginCollection.find(q1)
    check = False

    for  i in  result1:
        if  email == i['email']:
            check = True
            break
    
    if check:
        print("Email Address already exist in database.")
        return False
    else:
        password = pbkdf2_sha256.hash(password)
        q2 = {"name": name, "email": email,
              "password": password,"Id":str(uuid.uuid4())}
        
        LoginCollection.insert_one(q2)
        return True

def Login(email,password):
    l1 = {"email": email}
    res = LoginCollection.find(l1)

    data = {}
    data['check'] = False
    for i in res:
        if pbkdf2_sha256.verify(password, i['password']):
            data['name'] = i['name']
            data['check'] = True
    print(data)
    return data

#Register("anmolgoyal@gmail.com","Anmol Goyal","allocative")

# Allocative
# DeepReinorcementLearningProject