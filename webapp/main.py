from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from transformers import T5ForConditionalGeneration, T5Tokenizer
from os.path import dirname
import os

model = T5ForConditionalGeneration.from_pretrained('../model/French_model')

import numpy as np
import pandas as pd

tokenizer = T5Tokenizer.from_pretrained('../model/French_model')

def correct_trained(sentence): 
    input_ids = tokenizer(f"gec: {sentence}", return_tensors="pt").input_ids

    preds = model.generate(input_ids)
    corrected = []
    for pred in preds:  
        corrected.append(tokenizer.decode(pred, skip_special_tokens=True).strip())
    return "".join(corrected)

class Sentence(BaseModel):
    sentence: str

@app.post("/")
def read_root(sentence: Sentence):
    return correct_trained(sentence)
