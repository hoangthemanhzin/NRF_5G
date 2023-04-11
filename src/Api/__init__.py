#from quart import Quart, request, jsonifyfrom 
from quart  import jsonify
from src import app, request
from src.Service import nf_instance

#app = Quart(__name__)
#mk : 123456

#test : 

@app.route('/')
async def hello():
    return "hello"

@app.get("/test")
async def test():
    data = await request.get_json()
    return {"input": data, "extra": True}

#NF Instance ID (Document): register, deregister, read, update : 

@app.put("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_register(nfInstanceId):
    return jsonify(nf_instance.create_nf_instance(nf_profile=await request.get_json(), nfInstanceId=nfInstanceId))

@app.delete("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_deregister(nfInstanceId):
    return jsonify(nf_instance.delete_nf_instance(nfInstanceId=nfInstanceId))

@app.get("/nnrf-nfm/v1/nf-instances/<nfInstanceId>")
async def nf_read(nfInstanceId):
    nf_prf = nf_instance.get_nf_instance(nfInstanceId= nfInstanceId)
    if nf_prf != None:
        nf_prf["_id"] = str(nf_prf["_id"])
        return nf_prf
    return "Khong lay dc du lieu"


#def run() -> None:
#    app.run()