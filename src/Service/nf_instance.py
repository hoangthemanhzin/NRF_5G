#from Services import environment
from ..Database.database import free5gc_db
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Test nfprofile_collection
nfprofile_collection = free5gc_db.NfProfile;
#nfprofile_collection = client.free5gc.NfProfile;
# Function get nf instance

def get_nf_instance(nfInstanceId):
    try:
        nf_profile = nfprofile_collection.find_one({"nfInstanceId": nfInstanceId})
        return nf_profile
    except:
        return None
    
# Function delete nf instance 

def delete_nf_instance(nfInstanceId):
    if get_nf_instance(nfInstanceId= nfInstanceId) == None:
        print("NF does not exist")
        return 400
    try:
        nfprofile_collection.delete_one({"nfInstanceId": nfInstanceId})
        print("Deleted: " + str(nfInstanceId))
        return 200
    except:
        print("Cannot delete: " + str(nfInstanceId))
        return 400

#Function create nf 

def create_nf_instance(nfInstanceId, nf_profile):
    if get_nf_instance(nfInstanceId= nfInstanceId) != None:
        print("NF has already registered")
        return 400
    try:
        nfprofile_collection.insert_one(nf_profile)
        print("Register NF")
        return 200
    except:
        print("Cannot insert to nfProfile collection")
        return 400