import requests

def Client():
    token_h="Token de556ac4748fe17888049f4719cf3f16968900e5"
    # credentials={
    #     "username":"amir",
    #     "password":"rumi"

    # }

    # response=requests.post("http://192.168.43.212:8000/api/rest-auth/login/",data=credentials)

    
    headers= {"Authorization": token_h}

    response=requests.get("http://127.0.0.1:8000/TrafficReport/report/",
                             headers=headers)

    print("Status Code",response.status_code)

    response_data=response.json()
    print(response_data)

if __name__== "__main__":
    Client()