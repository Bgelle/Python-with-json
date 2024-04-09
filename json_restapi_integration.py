import argparse
import requests
import json
def read_data_json(filename):
    with open(filename,"r") as read:
        data=json.load(read)
        print(data)
def write_data_json(filename):
    data = {"product_name":"toy",'product_id': 78, 'manufactured': 'india',"cost":200}
    with open(filename,"w") as file:
        json.dump(data,file)
def update_data_json(filename):
    with open(filename,"r") as read:
        data=json.load(read)
    data["product_name"]="dairy"
    data["product_id"]=90
    print(data)
def delete_data_json(filename):
    with open(filename,"r") as read:
        data=json.load(read)
    del data["product_id"]
    print(data)
def conditional_update_json(filename):
    with open(filename,"r") as read:
        data=json.load(read)
    if data["product_name"]=="choclate":
        data["product_name"]="dairy"
    else:
        print("No product found!!")
    print(data)
def conditional_deletedata_json(filename):
    with open(filename,"r") as read:
        data=json.load(read)
    if data["product_cost"]==45:
        del data["mfd"]
    print(data)




parser = argparse.ArgumentParser()#//to get the parser object
parser.add_argument('-fn','--file_name',required=True, help="Please pass the file name to read")
args = parser.parse_args()
read_data_json(args.file_name)
update_data_json(args.file_name)
delete_data_json(args.file_name)
conditional_update_json(args.file_name)
conditional_deletedata_json(args.file_name)
write_data_json(args.file_name)