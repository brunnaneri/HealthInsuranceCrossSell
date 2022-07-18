import pickle
import pandas as pd
from flask                           import Flask, request, Response
from health_insurance.HealthInsurance import HealthInsurance

#loading model
model = pickle.load(open('/home/brunnaneri/repos/p004-hics/health_insurance_cross_sell/model/model_health_insurance.pkl','rb'))

#inicialize API
app = Flask(__name__)
@app.route('/predict', methods=['POST'])


def health_insurance_predict():
    json = request.get_json()
    
    if json: #there is data
        if isinstance(json,dict):
            df_raw = pd.DataFrame(json, index=[0])
        
        else: 
            df_raw = pd.DataFrame(json, columns=json[0].keys())
        
        #Instantiate Health Insurance Class
        pipeline = HealthInsurance()
        
        #Data Cleaning
        df1 = pipeline.data_cleaning(df_raw)

        #Feature Engineering
        df2 = pipeline.feature_engineering(df1)
        
        #Data Preparation
        df3 = pipeline.data_preparation(df2)
        
        #Prediction
        
        df_response = pipeline.get_prediction(model,df_raw,df3)
        
        return df_response
    
    else:
        return Response('{}',status=200, minetype='application/json')
                        
if __name__ == "__main__":
    app.run('0.0.0.0')
