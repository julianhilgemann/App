##### imports

# For the API CAll
import requests
# Basic calculations
import numpy as np
# JSON Handling
import json
# dataframe management
import pandas as pd
# OS
import os

#DB

from models import TimeSeriesData, Session

def extract_api_call(sample_key):
    # Split key by "."
    key_list = sample_key.split(".")
    # Extract FlowRef
    flowRef = key_list[0]
    # Extract key 
    key = sample_key[len(key_list[0])+1:]
    # Build call string
    # API Part of URL
    api_part_generic = "https://api.statistiken.bundesbank.de/rest/data/"
    api_part_specific = flowRef+"/"+key
    api_call = api_part_generic + api_part_specific
    return api_call

##### Function that takes in the api-call and performs a request and stores the data in a response_json

def auto_response_saver(api_call):
    #Define the header
    headers = {'accept': 'application/vnd.sdmx.data+json;version=1.0.0',}
    # Define parameters
    params = {'detail': 'full',}
    # Define full-sub
    full_response = '?detail=full'
    # Create full call
    full_call = api_call + full_response
    # Get the actual response
    response = requests.get(full_call, params=params, headers=headers,)
    # As json
    response_list = response.json()
    return(response_list)

##### Take Response and return DF

def extract_response(Response, ColName):
    Response_Numbers = []
    VarKey = list(Response["data"]["dataSets"][0]["series"].keys())[0]

    for key in Response["data"]["dataSets"][0]["series"][VarKey]["observations"]:
        Response_Numbers.append(Response["data"]["dataSets"][0]["series"][VarKey]["observations"][key][0])

    Response_Numbers_PD = pd.DataFrame(Response_Numbers, columns = [ColName])    

    # General Timestamp ["data"]["structure"]["dimensions"]["observation"][0]["values"]
    Response_Timestamp = []

    for element in Response["data"]["structure"]["dimensions"]["observation"][0]["values"]:
        Response_Timestamp.append(element["id"])

    Response_Timestamp_PD = pd.DataFrame(Response_Timestamp, columns = ["time"])

    Response_DF = pd.concat([Response_Timestamp_PD,Response_Numbers_PD],axis=1).set_index("time")
    
    return Response_DF

##### Function, that takes in a KEY and a "Name" that then 
##### builds the api call, fetches the data, extracts the data from the response and returns dataframes separately

def BBK2PD(KEY, ColName):
    Output = extract_response(auto_response_saver(extract_api_call(KEY)), ColName)
    return Output


#####Variable Declaration

Keys_All = {  
"HVPI" :"BBDP1.M.DE.N.HVPI.C.A00000.I15.A",
}

##### Create separate varables from dict

for key, value in Keys_All.items():
    exec(f"{key} = '{value}'")
    
##### Loop through the Dict and save Variables in dataframes
for key, value in Keys_All.items():
     exec(f"{key} = BBK2PD(value, key)")
        
# Create an empty list to store the values and loop through the dictionary and extract the values 
values = []
for key in Keys_All:
    values.append(globals()[key])
#Concat all variables and join the by common index.
DTF = pd.concat(values,axis=1,join="inner")
del values

##### Write Dataframe into DB

session = Session()

for index, row in DTF.iterrows():
    data = TimeSeriesData(
        name=row['name'],
        timestamp=row['timestamp'],
        value=row['value']
    )
    session.add(data)

session.commit()
session.close()

##### For future query

from models import TimeSeriesData, Session

session = Session()

# Query data from the database
results = session.query(TimeSeriesData).filter(TimeSeriesData.name == 'inflation_rate').all()

for result in results:
    print(result.name, result.timestamp, result.value)

session.close()