import pymongo
import pandas as pd 
import json
from micepe.config import mongo_client

DATA_FILE_PATH = "/config/workspace/Data_Cortex_Nuclear.xls"
DATABASE_NAME = "mice"
COLLECTION_NAME = "protein_exp"

if __name__=="__main__":
    df = pd.read_excel(DATA_FILE_PATH,index_col = "MouseID")
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json to dump records into mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
