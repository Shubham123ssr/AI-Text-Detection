from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import torch
from transformers import BertTokenizer, BertConfig, BertForSequenceClassification
from edit_distance import Edit_distance

# Initialize FastAPI
app = FastAPI()

# CORS middleware to allow the React frontend to make requests to FastAPI
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request body model
class TextRequest(BaseModel):
    text: str

# Load model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
config = BertConfig.from_pretrained('bert-base-uncased')
BertModel = BertForSequenceClassification(config)
model = BertModel.from_pretrained("yadagiriannepaka/BERT_MODELGYANDEEP.pth")
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

class TextDetector:
    def get_score(self, text):
        inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs)
            probabilities = torch.softmax(outputs.logits, dim=-1)

        return probabilities[0, 1].item()

detector = TextDetector()

def CalculateScore(text):
    score = detector.get_score(text)

    edit_distance = Edit_distance(text)

    final_score = score * 0.75 + 0.25 * edit_distance  # Adjust as per your logic

    return final_score


@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI detection API"}

@app.post("/predict")
async def predict_score(text_request: TextRequest):
    try:
        score = CalculateScore(text_request.text)
        print(score)    
        return {"score": score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# predict_score({"text": "Welcome to the AI detection API"}