import pickle
import validators

model = pickle.load(open("final_model.pkl", "rb"))

def encode_link(link): 
    len_link = len(link)
    contain_subscribe = 1 if "subscribe" in link else 0
    contain_hash = 1 if "#" in link else 0
    is_https = 1 if "https" in link else 0
    contain_question = 1 if "?" in link else 0
    numb_digit = sum ([1 for s in link if s.isdigit()]) 
    return [[len_link,contain_subscribe,contain_hash,is_https,contain_question,numb_digit]]

def predict_result(link): 
    if not validators.url(link):
        return -1

    encoded_link = encode_link(link)
    return model.predict(encoded_link)[0]