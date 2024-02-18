from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import vertexai
from vertexai.preview.generative_models import GenerativeModel
from utils import *
import pandas as pd
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import nest_asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("item_list3.csv")


vertexai.init(project="level-elevator-413808", location="us-central1")
model = GenerativeModel("gemini-pro")
tools = instantiate_tools()

intro_prompt = """
    You are an AI assistant.
    You are hired by 'Ettara Cafe' to guide users on the website and help them recommend products of their preference.
    Be empathetic and ask for their preferences and use the tools given to you to suggest them items. 
    
    <Important>
    If a user gives a vague message and is not related to the cafe, suggest 3 items from the menu. Call the menu function to get the list of products.
    Each suggestion must include strictly 3 items, No more and No less. If there are less items for some request add additional items that may complement other items.
    </Important>
    """

func_dict = {
    "get_product_list": menu,
    "add_to_cart": add_to_cart,
    "get_user_history": get_user_history,

}

# prompt = "I want to something with nuts. What do you suggest?"
chat_model = model.start_chat()
print(chat_model)

class MessageRequest(BaseModel):
    message:str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/message")
async def send_message(message: MessageRequest):
    print("Hello")
    # global chat_model, func_dict
    prompt = message.message
    response = chat_model.send_message(prompt, tools=tools)
    model_function = response.candidates[0].content.parts[0].function_call.name
    print(model_function)
    if model_function == "":
        model_function = "get_product_list"
    params = {}
    if response.candidates[0].content.parts[0].function_call.args:
        for key, value in response.candidates[0].content.parts[0].function_call.args.items():
            params[key] = value

    output = func_dict[model_function](**params)
    try:
        final_response = chat_model.send_message(
            Part.from_function_response(
                name=model_function,
                response={
                    "content": output,
                }
            ),
            tools=tools
        )
        answer = final_response.candidates[0].content.parts[0].text

        items = []
        for index, item in df.iterrows():
            if item["Names"] in answer:
                items.append({
                    "Name": item["Names"],
                    "Price": item["Prices"],
                    "Image": item["Image Source"]
                })
            if len(items) == 3:
                break
        if len(answer) < 200:
            answer += (200-len(answer))*' '
        if items:
            return {"message": answer, "items": items}
        else:
            return {"message": answer}
    except Exception as e:
        print(e)
        return {"message": "Some Error Occurred. Please Try Again."}



# uvicorn.run("backend:app", host="0.0.0.0", port=port, reload=True)
if __name__=="__main__":
    port = 8000
    ngrok_tunnel = ngrok.connect(port)
    print('Public URL:', ngrok_tunnel.public_url)
    nest_asyncio.apply()
    uvicorn.run(app,port=port)