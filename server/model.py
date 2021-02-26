from functools import lru_cache
import pickle
import os

model_path = os.getenv("MODEL_PATH")

@lru_cache(maxsize=1)
def load_model():
    # Loading model to compare the results
    model = pickle.load(open(model_path,'rb'))
    return model