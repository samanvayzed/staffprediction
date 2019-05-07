#!/bin/bash

curl -d ' [{"userid":102,"year":2019 ,"month":5 ,"day":25},{"userid":102,"year":2019 ,"month":5 ,"day":26},{"userid":102,"year":2019 ,"month":5 ,"day":27}]' -H "Content-Type: application/json" -X POST http://localhost:12345/predict 


