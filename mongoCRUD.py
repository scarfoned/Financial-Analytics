#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:55:11 2020

@author: drewscarfone
"""

import requests
import json
import pandas as pd
import urllib.request as ur
from bs4 import BeautifulSoup
from pymongo import MongoClient
from random import randint

db_name = 'masterDB'
collections = 'companies'
connection_string = "mongodb+srv://dscarf:Rowmingroger2@masterdb-gcmec.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(connection_string)
database = client[db_name]
collection_list = database.list_collection_names()

index = 'MSFT'
inst = 'Income Statement'
bs = 'Balance Sheet'
cf = 'Cash Flow'

def find_collection(col_name):
    if col_name in collection_list:
        print('It is in List!')
        return(True)
    else:
        print(collection_list)
        find_collection(input('Enter Collection Name Again: '))

#find_collection(input('Enter Collection Name: '))

def income_statement(index, statement):
    if statement == 'Income Statement':
        temp = 'income-statement'
    if statement == 'Balance Sheet':
        temp = 'balance-sheet-statement'
    if statement == 'Cash Flow':
        temp = 'cash-flow-statement'
    
    data = requests.get(f"https://financialmodelingprep.com/api/v3/financials/" + temp + "/" + index)
    data = data.json()
    data = data['financials']
    
    df = pd.DataFrame(data)
    dataset = dict()
    dict_items = []
    
    dataset = df.T.to_dict()
    
    for i in df:
        dict_items.append(i)
    #print(dataset[0])
    
    
income_statement(index, inst)












