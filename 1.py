import json

#l = '{"userid": 102, "year": 2019, "month": 5, "day": 25}, {"userid": 102, "year": 2019, "month": 5, "day": 26}, {"userid": 102, "year": 2019, "month": 5, "day": 27}'

#print("xxxxx" + l + "yyyyy")


list = [{'userid': 102, 'year': 2019, 'month': 5, 'day': 25}, {'userid': 102, 'year': 2019, 'month': 5, 'day': 26}, {'userid': 102, 'year': 2019, 'month': 5, 'day': 27}]
print(list[1]['year'])
#print(type(list[1]))

#my_dict = json.loads(list[1])

#print("YYYYYYYYYYY")
#print(my_dict)
#print("ZZZZZZZZZZZ")
#print(my_dict['year'])
