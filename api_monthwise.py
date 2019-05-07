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
import calendar
import time
from dateutil import relativedelta
###############

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if clfstaff:
        try:
            json_ = request.json
            #print("JHBGVCVGBHJKMJNBV BHJKMJNHBVBGHJKMNHBV")
            #print(json_[0]['userid'])
            #print("JHJJHBGHJIKJHBGHJKJHBGHJKI")

            length = len(json_)
            print(length)
            

            inp_arr = np.array([[0,0,0,0,0,0]])
            month_name_arr = np.array([[0]])
            month_arr = np.array([[0,0,0,0]])


            for i in range(length):
                print(i)
                year = json_[i]['y']
                month = json_[i]['m']
                #day = json_[i]['day']
                #year = str(year)
                #month = str(month)
                #day = str(day)
                #print("Day:" + day)

                #print("LLLLLLLLLLLLLLLL")
                #print("Month:" + month)
                #print("Year:" + year)
                #print("MMMMMMMMMMMMMMM")

                num_days = calendar.monthrange(year, month)[1]
                days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
                #print("UUUUUUUUUUUUUU") 
                #print(days)
                #print("IIIIIIIIIIIIIII")

                user1_arr = np.array([[0,0,0,0,0,0]])


                for day in days: 
                    unix_time = time.mktime(day.timetuple())
                    #print("LLLLLLLLLLLLL")
                    #print("EpochTime:" + str(unix_time)) 
                    #print("LLLLLLLLLLLLL")
                    user1_arr = np.append(user1_arr, [[unix_time,1,0,0,0,0]], axis = 0) 
               
                user1_arr = np.delete(user1_arr, (0), axis=0) 


                print("OOOOO") 
                print(user1_arr)
                print("KKKKK")

                test1_res = clfstaff.predict(user1_arr)

                print("OOOOO") 
                print(test1_res)
                print("KKKKK")

                month_sum1 = np.sum(test1_res)

                print("OOOOO") 
                print(month_sum1)
                print("KKKKK")


                user2_arr = np.array([[0,0,0,0,0,0]])


                for day in days: 
                    unix_time = time.mktime(day.timetuple())
                    #print("LLLLLLLLLLLLL")
                    #print("EpochTime:" + str(unix_time)) 
                    #print("LLLLLLLLLLLLL")
                    user2_arr = np.append(user2_arr, [[unix_time,0,1,0,0,0]], axis = 0)  

                user2_arr = np.delete(user1_arr, (0), axis=0) 


                print("OOOOO") 
                print(user2_arr)
                print("KKKKK")

                test2_res = clfstaff.predict(user2_arr)
                #test_res = np.reshape(test_res, (length,4))

                print("OOOOO") 
                print(test2_res)
                print("KKKKK")

                month_sum2 = np.sum(test2_res)


                user3_arr = np.array([[0,0,0,0,0,0]])


                for day in days:
                    unix_time = time.mktime(day.timetuple())
                    #print("LLLLLLLLLLLLL")
                    #print("EpochTime:" + str(unix_time)) 
                    #print("LLLLLLLLLLLLL")
                    user3_arr = np.append(user3_arr, [[unix_time,0,0,1,0,0]], axis = 0) 

                user3_arr = np.delete(user3_arr, (0), axis=0)


                print("OOOOO")
                print(user3_arr)
                print("KKKKK")

                test3_res = clfstaff.predict(user3_arr)
                #test_res = np.reshape(test_res, (length,4))

                print("OOOOO")
                print(test3_res)
                print("KKKKK")

                month_sum3 = np.sum(test3_res)

                user4_arr = np.array([[0,0,0,0,0,0]])


                for day in days:
                    unix_time = time.mktime(day.timetuple())
                    #print("LLLLLLLLLLLLL")
                    #print("EpochTime:" + str(unix_time)) 
                    #print("LLLLLLLLLLLLL")
                    user4_arr = np.append(user4_arr, [[unix_time,0,0,0,1,0]], axis = 0) 

                user4_arr = np.delete(user4_arr, (0), axis=0)


                print("OOOOO")
                print(user4_arr)
                print("KKKKK")

                test4_res = clfstaff.predict(user4_arr)
                #test_res = np.reshape(test_res, (length,4))

                print("OOOOO")
                print(test4_res)
                print("KKKKK")

                month_sum4 = np.sum(test4_res)

                print("AHHAHAHAHAHAHAHHA")
                print(month_sum1)
                print(month_sum2)
                print(month_sum3)
                print(month_sum4)
                print("AHAHAHAHAHAHHAHAH")

                month_arr = np.append(month_arr, [[month_sum1,month_sum2,month_sum3,month_sum4]], axis = 0)


                #date_time_str = year + "-" + month + "-"+ day  
                #date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

                month_name = day.strftime('%b')
                month_name_arr = np.append(month_name_arr, [[month_name]], axis = 0)

                
                #unix_time = time.mktime(date_time_obj.timetuple())
                #print("EpochTime:" + str(unix_time)) 
                
                #inp_arr = np.append(inp_arr, [[unix_time,1,0,0,0,0]], axis = 0)
                #inp_arr = np.append(inp_arr, [[unix_time,0,1,0,0,0]], axis = 0)
                #inp_arr = np.append(inp_arr, [[unix_time,0,0,1,0,0]], axis = 0)
                #inp_arr = np.append(inp_arr, [[unix_time,0,0,0,1,0]], axis = 0)
 
            month_name_arr = np.delete(month_name_arr, (0), axis=0)
            month_arr = np.delete(month_arr, (0), axis=0)
            print("YYYYYYYYYYY")
            print(month_name_arr)
            print(month_arr)
            print("ZZZZZZZZZZZ")


            #test_res = regressor.predict(inp_arr)
            #test_res = np.reshape(test_res, (length,4)) 


            out = np.concatenate((month_name_arr, month_arr), axis=1)  
            out_list = out.tolist()
            out_json_string = json.dumps(out_list)          

            print("PPPPPPPPPPPPPPPPPPP")
            #print(test_res)
            #print(day_arr)
            print(out_json_string)
            print("KKKKKKKKKKKKKKKKKKK")

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
