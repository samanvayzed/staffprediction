#!/bin/bash

curl -d ' [{"m":1 ,"y":2019},{"m":2, "y":2019},{"m":4, "y":2019}]' -H "Content-Type: application/json" -X POST http://localhost:12345/predict 
