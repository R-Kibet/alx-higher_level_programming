#!/bin/bash
# return status code
curl -o /dev/null -s -w "%{http_code}" $1
