from fastapi import FastAPI, Query, Path, HTTPException
import json

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

app = FastAPI()

# @app.route("/", method=["GET"])
# name = request.args.get("name")

@app.get("/")
def hello():
    return {"message":"Hello from App"}

@app.get("/about")
def about(name: str = Query("Stranger", description="Add name as query parameter")):
    return {"message":"This app is build in collabaration with {name}"}


@app.get("/view")
def view():
    return load_data()

@app.get('/view/{id}')
def view_specific(id: str = Path(description="This will take you to the specific patient", examples=["P001", "P001"])):
    data = load_data()
    return data[id]

@app.get("/sort")
def sort(pram: str = Query(..., description=""),
         type: str = Query("desc", description="")):
    data = load_data()
    reverse = False
    reverse = True if type == "desc" else False
    checks = ["height", "weight", "age", "bmi"]

    if pram in checks:
        sort_data = sorted(data.items(),key = lambda X:X[1].get(pram), reverse=reverse)
    else:
        raise HTTPException(status_code=404, detail="This parameter doest exist")
    return sort_data