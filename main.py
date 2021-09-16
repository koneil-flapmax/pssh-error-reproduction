# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 02:41:11 2021

@author: piyush
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pssh.clients import SSHClient


app = FastAPI()

logger = logging.getLogger('gunicorn.error')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



