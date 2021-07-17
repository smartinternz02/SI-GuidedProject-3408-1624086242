import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "kwB4ALb2-exUR2mJnILKbrcPr4NOpWrn3Tm5wZitXsUn"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['sad','neutral','happy','step_count','calories_burned','hours_of_sleep','weight_kg']] , "values": [[0,0,1,4435,600,10,65]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5a057f36-51ca-4eac-a353-6ea4721d8b6c/predictions?version=2021-06-25', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
print(predictions)
pred=predictions['predictions'][0]['values'][0][0]

if(pred == 0):
            result = "You are not fit"
else:
            result = "You are fit"
print(result)