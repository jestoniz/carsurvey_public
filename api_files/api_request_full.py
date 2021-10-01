import http.client
import json
import urllib
import os

def request_api(args):
    client_API_key = os.environ.get('CLIENT_API_KEY')
    #conn = http.client.HTTPConnection("localhost:8000")
    conn = http.client.HTTPSConnection("carsurvey.ph")
    request_url = "/api/?"+args+'&api-key='+client_API_key
    request_url = request_url.replace(' ','+')
    print('=======URL Request===================')
    print('https://carsurvey.ph'+request_url)
    print('=======END: URL Reque================')
    print()

    conn.request("GET", request_url)
    res = conn.getresponse()
    data = res.read()
    json_object = json.loads(data.decode("utf-8"))
    json_formatted_str = json.dumps(json_object, indent=2)
    print('=======JSON Response Data=============')
    print(json_formatted_str)
    print('====END:JSON Response Data=============')
    print()

    return json_object


run_program = True

while (run_program):

    json_object = request_api('')
    
    #//----------------------------------------------------------
    #selecting the Maker
    #//----------------------------------------------------------
    
    i = 0
    print("Select the number of chosen Maker")
    for make in json_object["makers"]:
        print(str(i)+": "+str(make))
        i = i + 1
    input_maker = json_object["makers"][int(input())]
    
    
    #//----------------------------------------------------------
    #END: selecting the Maker
    #//----------------------------------------------------------
    
    #//----------------------------------------------------------
    #Selecting the Model
    #//----------------------------------------------------------
    
    #sending the request to get the models
    json_object = request_api("maker="+input_maker)
    
    i = 0
    print("Select the number of chosen Model")
    for model in json_object["models"]:
        print(str(i)+": "+str(model))
        i = i + 1
    input_model = json_object["models"][int(input())]
    
    
    print("Select the number of chosen Transmission")
    i = 0
    for trans_option in json_object["transmission"]:
        print(str(i)+": "+str(trans_option))
        i = i + 1
    input_transmission = json_object["transmission"][int(input())]
    
    print("Input the year")
    input_year = input()

    print("Input the mileage")
    input_mileage = input()

    print("Do you want to include repossessed cars in your FMV computation? [Y/N]")
    response = input()
    if response.lower() == 'y':
        input_repo = 'true'
    else:
        input_repo = 'false'
    #//----------------------------------------------------------
    #END: Selecting the Model
    #//----------------------------------------------------------
    
    
    #//----------------------------------------------------------
    # Selecting the Variant
    #//----------------------------------------------------------
    json_object = request_api("maker="+input_maker+"&model="+input_model+"&year="+input_year+"&transmission="+input_transmission+"&mileage="+input_mileage+"&repo="+input_repo)
    
    print("Select the number of chosen Variant")
    print("*** Indicates the current variant with 2021 model")
    i = 0
    for var_option in json_object["variant"]:
        print(str(i)+": "+str(var_option))
        i = i + 1
    input_variant = json_object["variant"][int(input())]
    
    #//----------------------------------------------------------
    #END:  Selecting the Variant
    #//----------------------------------------------------------
    
    #get the final value
    json_object = request_api("maker="+input_maker+"&model="+input_model+"&year="+input_year+"&transmission="+input_transmission+"&variant_words="+input_variant+"&mileage="+input_mileage+"&repo="+input_repo)

    print("Select the number of the next step you want to do:")
    print("[0] Exit Program")
    print("[1] Select another car")
    user_action = input()
    
    run_program = user_action != '0'
