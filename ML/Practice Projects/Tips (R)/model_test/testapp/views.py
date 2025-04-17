from django.shortcuts import render
from testapp.models import Tips
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
import joblib

# Create your views here.

model_path = '/home/suhas/Desktop/office/Data Science/Notes/Data Analysis/2024-Nov/ML/Practice Projects/Tips/model_test/testapp/svm.pkl'
piepline = joblib.load(model_path)

class TipsPrediction(APIView):
    def post(self,request):
        try:
            #get the data from the request body
            data  = request.data

            #Extract individual values from the request data
            total_bill = data.get('total_bill')
            sex = data.get('sex')
            smoker = data.get('smoker')
            day = data.get('day')
            time = data.get('time')
            size = data.get('size')

            # create a dictionary for the input data
            raw_data = {
                "total_bill": total_bill,
                "sex": sex,
                "smoker": smoker,
                "day": day,
                "time": time,
                "size": size
            }

            # creata a dataframe for the new data
            new_data = pd.DataFrame([raw_data])

            prediction = piepline.predict(new_data)

            #save the new record in the database
            new_tip = Tips(
                total_bill = total_bill,
                sex = sex,
                smoker = smoker,
                day = day,
                time = time,
                size = size,
                tip = str(prediction[0])
            )
            new_tip.save()

            # Return the response in the
            return Response({
                "Predicted_tip": prediction[0],
                "message": "Prediction saved sucessfull"
            },status=status.HTTP_201_CREATED)
    
    
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    


