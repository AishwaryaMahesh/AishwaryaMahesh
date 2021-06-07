# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:14:08 2021

@author: 10641168
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())