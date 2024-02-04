from pymongo import MongoClient
import pandas as pd 
from logger import logging
from exception import CustomException


def Data_collection():
    try:
        logging.info("Data Collaction from mongoDB Database Started")
        claster = MongoClient("mongodb+srv://arup92327:Arup0070@cluster0.e9r83iz.mongodb.net/?retryWrites=true&w=majority")
        db=claster["Movie_DataBase"]
        coll=db["Movie_data"]
        li=[]
        for i in coll.find({},{"_id":0}):
                li.append(i)
        df=pd.DataFrame(li)
        df.to_csv("Data\Movies.csv")
    except Exception as e:
        logging.info("Error in Data Collection From MongoDB")
        raise CustomException(e,sys)

if __name__=="__main__":
    df= Data_collection()
