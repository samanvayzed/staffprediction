# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:55:43 2019

@author: hp
"""



# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
import sys
import json

################
import datetime
import time
from dateutil import relativedelta
###############

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def staff_day():
    if clfstaff:
        try:
            json_ = request.json
            print("JHBGVCVGBHJKMJNBV BHJKMJNHBVBGHJKMNHBV")
            print(json_[0]['y'])
            print("JHJJHBGHJIKJHBGHJKJHBGHJKI")

            length = len(json_)
            print(length)
            
            #m = str(json_).strip('[]')
            #print(m) 
            #n = '"' + m + '"'  
            #print(n)
            #y = str(n).replace("'", '"')
            #print("HHHHHHH") 
            #print(y)
            #print("IIIIII")
            #z = y[1:-1]
            #a = "'" + z + "'"
            #print("xxxxx" + z + "yyyyy")
            #my_dict = json.loads(z)
            #print("YYYYYYYYYYY")
            #print(my_dict)
            #print("ZZZZZZZZZZZ")
            #print(my_dict['year'])
            

            inp_arr = np.array([[0,0,0,0,0,0]])
            #day_list = []
            day_arr = np.array([[0]])


            for i in range(length):
                print(i)
                year = json_[i]['y']
                month = json_[i]['m']
                day = json_[i]['d']
                year = str(year)
                month = str(month)
                day = str(day)
                print("Day:" + day)
                print("Month:" + month)
                print("Year:" + year)
                date_time_str = year + "-" + month + "-"+ day  
                date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

                week_day = date_time_obj.strftime('%a')
                #day_list.append(week_day)
                day_arr = np.append(day_arr, [[week_day]], axis = 0)

                
                unix_time = time.mktime(date_time_obj.timetuple())
                print("EpochTime:" + str(unix_time)) 
                
                #inp_arr = np.array([[0,1,0,0]])
                #inp_arr = np.empty([4, 1])
                inp_arr = np.append(inp_arr, [[unix_time,1,0,0,0,0]], axis = 0)
                inp_arr = np.append(inp_arr, [[unix_time,0,1,0,0,0]], axis = 0)
                inp_arr = np.append(inp_arr, [[unix_time,0,0,1,0,0]], axis = 0)
                inp_arr = np.append(inp_arr, [[unix_time,0,0,0,1,0]], axis = 0)
 
            day_arr = np.delete(day_arr, (0), axis=0)
            inp_arr = np.delete(inp_arr, (0), axis=0)
            print("YYYYYYYYYYY")
            print(inp_arr)
            print("ZZZZZZZZZZZ")


            test_res = clfstaff.predict(inp_arr)
            test_res = np.reshape(test_res, (length,4)) 


            out = np.concatenate((day_arr, test_res), axis=1)  
            out_list = out.tolist()
            out_json_string = json.dumps(out_list)          

            print("PPPPPPPPPPPPPPPPPPP")
            #print(test_res)
            #print(day_arr)
            print(out_json_string)
            print("KKKKKKKKKKKKKKKKKKK")
            
            ''' 
            next = []
            
            for x in range(0,8):
                next.append(date_time_obj + datetime.timedelta(days=x))

            print("YYYYYYYYYYY")

            for i in range(0,8):
                #print(next[i])
                dto_string = str(next[i])
                pattern = "%Y-%m-%d %H:%M:%S"
                epoch = int(time.mktime(time.strptime(dto_string, pattern))) 
                #print(epoch)
                inp_arr = np.append(inp_arr, [[epoch,1,0,0]], axis = 0)

            inp_arr = np.delete(inp_arr, (0), axis=0)

            print("YYYYYYYYYYY")
            print(inp_arr) 
            print("ZZZZZZZZZZZ")

            #dto_string = str(date_time_obj)
            
            #pattern = "%Y-%m-%d %H:%M:%S"
            #epoch = int(time.mktime(time.strptime(dto_string, pattern)))
            #print("HELLO") 
            #print(epoch)
            #print("HELLO")

            ############################################## 
            # QUICKLY TEST QUERY HERE
            ##############################################
            pred_test=np.array([[epoch,1,0,0]])
            test_res=regressor.predict(inp_arr)

            print("CCCCCCCCCCCCCCCC")
            print(test_res)
            print("CCCCCCCCCCCCCCCC")
   
            ################################################
            #regressor.predict(query)

            #pred_features1=np.array([[102,2019,5,25]])

            

            userid = np.int64(userid)
            year = np.int64(year)
            month = np.int64(month)
            day = np.int64(day)

         

            pred_features0=np.array([[userid,year,month,day]])
            pred_features1=np.array([[userid,next_seven_days[1].year,next_seven_days[1].month,next_seven_days[1].day]])
            pred_features2=np.array([[userid,next_seven_days[2].year,next_seven_days[2].month,next_seven_days[2].day]])
            pred_features3=np.array([[userid,next_seven_days[3].year,next_seven_days[3].month,next_seven_days[3].day]])
            pred_features4=np.array([[userid,next_seven_days[4].year,next_seven_days[4].month,next_seven_days[4].day]])
            pred_features5=np.array([[userid,next_seven_days[5].year,next_seven_days[5].month,next_seven_days[5].day]])
            pred_features6=np.array([[userid,next_seven_days[6].year,next_seven_days[6].month,next_seven_days[6].day]])
            pred_features7=np.array([[userid,next_seven_days[7].year,next_seven_days[7].month,next_seven_days[7].day]])

 
            pred_result0=regressor.predict(pred_features0).astype('int64')
            pred_result1=regressor.predict(pred_features1).astype('int64')
            pred_result2=regressor.predict(pred_features2).astype('int64')
            pred_result3=regressor.predict(pred_features3).astype('int64')
            pred_result4=regressor.predict(pred_features4).astype('int64')
            pred_result5=regressor.predict(pred_features5).astype('int64')
            pred_result6=regressor.predict(pred_features6).astype('int64')
            pred_result7=regressor.predict(pred_features7).astype('int64')
 
            pred_result0 = int(pred_result0)
            pred_result1 = int(pred_result1)
            pred_result2 = int(pred_result2)
            pred_result3 = int(pred_result3)
            pred_result4 = int(pred_result4)
            pred_result5 = int(pred_result5)
            pred_result6 = int(pred_result6)
            pred_result7 = int(pred_result7)
            
            #print(type(pred_result0))
            #print(type(pred_result1))
            #print(pred_result2)
            #print(pred_result3)
            #print(pred_result4)
            #print(pred_result5)
            #print(pred_result6)
            #print(pred_result7)

            
            dict_0 = {}
            dict_0['x']=next_seven_days[0].strftime("%a")
            dict_0['value']=pred_result0


            dict_1 = {}
            dict_1['x']=next_seven_days[1].strftime("%a")
            dict_1['value']=pred_result1

            dict_2 = {}
            dict_2['x']=next_seven_days[2].strftime("%a")
            dict_0['value']=pred_result2

            dict_3 = {}
            dict_3['x']=next_seven_days[3].strftime("%a")
            dict_3['value']=pred_result3

            dict_4 = {}
            dict_4['x']=next_seven_days[4].strftime("%a")
            dict_4['value']=pred_result4


            dict_5 = {}
            dict_5['x']=next_seven_days[5].strftime("%a")
            dict_5['value']=pred_result5

            dict_6 = {}
            dict_6['x']=next_seven_days[6].strftime("%a")
            dict_6['value']=pred_result6

            dict_7 = {}
            dict_7['x']=next_seven_days[7].strftime("%a")
            dict_7['value']=pred_result7

            '''

            #list_of_dicts = [dict_0,dict_1,dict_2,dict_3,dict_4,dict_5,dict_6,dict_7]
            #list_of_dicts = [dict_0,dict_1]


            # convert into JSON:
            #json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            #print(json_dict)
 


        
            #list = [pred_result0, pred_result1,pred_result2, pred_result3, pred_result4, pred_result5, pred_result6, pred_result7] 

            #query = pd.get_dummies(pd.DataFrame(json_))
            #print(query) 
            #query = query.reindex(columns=model_columns, fill_value=0)

            #print(query)

            #prediction = list(regressor.predict(query))
            #print(prediction)
            
            #return jsonify({'prediction': str(list)})
            #return jsonify({'prediction': str(prediction)})
            a = "cheese"
            return out_json_string 
 

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    clfstaff = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')
    print(model_columns)



    app.run(port=port, debug=True)
