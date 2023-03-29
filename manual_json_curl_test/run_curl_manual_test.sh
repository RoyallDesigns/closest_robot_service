#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d @test_json_for_curl.json http://localhost:5000/api/robots/closest
