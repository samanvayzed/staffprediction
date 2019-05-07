#!/bin/bash

curl -d ' [{"w":1 ,"y":2019},{"w":2, "y":2019},{"w":4, "y":2019}]' -H "Content-Type: application/json" -X POST http://localhost:12345/predict 
