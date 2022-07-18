import pickle
import pandas as pd
import numpy as np

class HealthInsurance(object):
    def __init__(self):
        self.path = '/home/brunnaneri/repos/p004-hics/health_insurance_cross_sell/'
        self.annual_premium_scaler = pickle.load(open(self.path+'parameter/annual_premium_scaler.pkl','rb'))
        self.month_premium_scaler = pickle.load(open(self.path+'parameter/month_premium_scaler.pkl','rb'))
        self.age_scaler = pickle.load(open(self.path+'parameter/age_scaler.pkl','rb'))
        self.vintage_scaler = pickle.load(open(self.path+'parameter/vintage_scaler.pkl','rb'))
        self.vintage_month_scaler = pickle.load(open(self.path+'parameter/vintage_month_scaler.pkl','rb'))
        self.vintage_week_scaler = pickle.load(open(self.path+'parameter/vintage_week_scaler.pkl','rb'))
        self.gender_encoder = pickle.load(open(self.path+'parameter/gender_encoder.pkl','rb'))
        
    def data_cleaning(self, df):
        #ensuring that column names will be lowercase
        df.columns = df.columns.str.lower()
        
        return df
    
    def feature_engineering(self, df3):
        # Vehicle Age
        df3['vehicle_age'] = df3['vehicle_age'].apply(lambda x: 'a' if x=='< 1 Year' else 'b' if x=='1-2 Year' else 'c')
        
        # Vehicle Damage
        df3['vehicle_damage'] = df3['vehicle_damage'].apply(lambda x: 1 if x=='Yes' else 0)
        
        #Annual premium to Month premium
        df3['month_premium'] = round(df3['annual_premium']/30,2)
        
        #Vintage (day) to month
        df3['vintage_month'] = round(df3['vintage']/30)
        df3['vintage_month'] = df3['vintage_month'].astype('int64')
        
        #Vintage (day) to week
        df3['vintage_week'] = (df3['vintage']/7)
        df3['vintage_week'] = df3['vintage_week'].astype('int64')
    
        return df3
    
    def data_preparation(self,df5): 
        # Annual Premium
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5[['annual_premium']].values)
        
        # Month Premium
        df5['month_premium'] = self.month_premium_scaler.transform(df5[['month_premium']].values)
        
        #Age
        df5['age'] = self.age_scaler.transform(df5[['age']])
        
        #Vintage
        df5['vintage'] =self.vintage_scaler.transform(df5[['vintage']])
        
        #Vintage Week
        df5['vintage_week'] = self.vintage_week_scaler.transform(df5[['vintage_week']])
        
        #Vintage Month
        df5['vintage_month'] = self.vintage_month_scaler.transform(df5[['vintage_month']])      
        
        # Gender - Target Encoder
        df5['gender'] = self.gender_encoder.transform(df5['gender'])
        
        # Vehicle Age - Ordinal Encoder
        df5 = pd.get_dummies(df5, prefix='vehicle_age',columns=['vehicle_age'])
        
        # Policy Sales Channel - Frequency Encoder
        freq_pol = df5.groupby('policy_sales_channel').size()/len(df5['policy_sales_channel'])
        df5.loc[:,'policy_sales_channel'] = df5['policy_sales_channel'].map(freq_pol)
        
        # Region Code - Frequency Encoder
        freq_region = df5.groupby('region_code').size()/len(df5['region_code'])
        df5.loc[:,'region_code'] = df5['region_code'].map(freq_region)
        
        
        #as vehicle_age is derived in multiple columns (due to pandas get_dummies method) it is necessary to perform a check:
        
        if 'vehicle_age_a' not in df5.columns:
            df5['vehicle_age_a'] = 0
        
        if 'vehicle_age_b' not in df5.columns:
            df5['vehicle_age_b'] = 0
            
        if 'vehicle_age_c' not in df5.columns:
            df5['vehicle_age_c'] = 0
 
        cols_selected = ['gender', 'age', 'region_code', 'policy_sales_channel',
       'driving_license', 'vehicle_damage', 'previously_insured',
       'annual_premium','vehicle_age_a', 'vehicle_age_b', 'vehicle_age_c']
    
        return df5[cols_selected]
    
    def get_prediction(self,model,data_original,data_prepared):
        prediction = model.predict_proba(data_prepared)
        data_original['predict_score'] = prediction[:,1].tolist()
        data_original = data_original.sort_values('predict_score',ascending=False)
        data_original = data_original.reset_index(drop=True)
        return data_original.to_json(orient='records')
