from App import app
from App.db import CassandraConnector
import pandas as pd
import json

@app.get("/api/getAllInfo")
def getAllInfo():
    cassandra = CassandraConnector()
    query = "SELECT * FROM product_information"
    result = cassandra.query(query)
    cassandra.close()
    
    return {
        "status": True,
        "message": "Get all info successfully",
        "data":json.dumps(result)
    }

@app.get("/api/countCategory")
def countCategory():
    cassandra = CassandraConnector()
    query = "SELECT categories FROM product_information"
    result = cassandra.query(query)
    cassandra.close()
    # Convert result to pandas DataFrame
    df = pd.DataFrame(result)

    # Extract category names
    df['categories'] = df['categories'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
    print(df['categories'])
    # Extract category names
    df['category_name'] = df['categories'].apply(lambda x: x['name'] if x is not None else None)

    # Count category names
    count = df['category_name'].value_counts().to_dict()
    
    
    return {
        "status": True,
        "message": "Count category successfully",
        "data": count 
    }

@app.get("/api/getInfo")
def getCategory(id:str):
    cassandra = CassandraConnector()
    query = f"SELECT * FROM product_information Where id ='{id}'"
    result = cassandra.query(query)
    cassandra.close()
    return {
        "status": True,
        "message": "Get info successfully",
        "data": result 
    }
