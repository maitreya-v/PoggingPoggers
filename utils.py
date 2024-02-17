import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, FunctionDeclaration, Tool, Content
import pandas as pd
from typing import List, Dict

def suggest_items(item_list: str):
    df = pd.read_csv("item_list2.csv")
    items = []
    for index, item in df.iterrows():
        if item["Names"] in item_list:
            items.append({
                "Name":item["Names"],
                "Price":item["Prices"],
                "Image": item["Image Source"]
            })
        if len(items) == 3:
            break

    return {"text": item_list, "items": items}


def menu(items=None) -> Dict[str, List[str]]:
    df = pd.read_csv("item_list2.csv")
    return {"Menu": df["Names"].to_list()}

# Specify a function declaration and parameters for an API request


def add_to_cart(items: List[str]) -> Dict[str, str]:
        return {"Status": "Success"}


def instantiate_tools() -> List[Tool]:
    get_current_products_func = FunctionDeclaration(
        name="get_product_list",
        description="Get the complete menu of the cafe to be able to suggest items. Call this function always when no other function is called.",
        # Function parameters are specified in OpenAPI JSON schema format
        parameters={
            "type": "object",
            "properties": {"items": {"type": "string"}},
        },
    )

    add_to_cart_func = FunctionDeclaration(
        name="add_to_cart",
        description="Add a list of items to cart.",
        parameters={
            "type": "object",
            "properties": {"items": {"type": "array", "items": {"type": "string"}}}
        }
    )

    # suggest_items_func = FunctionDeclaration(
    #     name="suggest_items",
    #     description="Send user suggestions. Input must be a string having atleast 3 menu items. Use this function to send user final suggestions.",
    #     parameters={
    #         "type": "object",
    #         "properties": {"item_list": {"type": "string"}}
    #     }
    # )

    # Define a tool that includes the above get_current_weather_func
    cafe_tool = Tool(
        function_declarations=[add_to_cart_func,get_current_products_func ],
    )


    return [cafe_tool]


def send_message_no(prompt:str)->str:
    intro_prompt = """
    You are an AI assistant.
    You are hired by 'Ettara Cafe' to guide users on the website and help them recommend products of their preference.
    Be empathetic and ask for their preferences and use the tools given to you to suggest them items. 
    """
    vertexai.init(project="level-elevator-413808", location="us-central1")
    model = GenerativeModel("gemini-pro")
    tools = instantiate_tools()

    func_dict = {
        "get_product_list": menu,
        "add_to_cart": add_to_cart
    }

    # prompt = "I want to something with nuts. What do you suggest?"
    chat_model = model.start_chat()
    for i in range(3):
        prompt = input()
        response = chat_model.send_message(prompt, tools=tools)
        model_function = response.candidates[0].content.parts[0].function_call.name
        print(model_function)
        params = {}
        if response.candidates[0].content.parts[0].function_call.args:
            for key, value in response.candidates[0].content.parts[0].function_call.args.items():
                params[key] = value

        output = func_dict[model_function](**params)
        final_response = chat_model.send_message(
            Part.from_function_response(
                name=model_function,
                response={
                    "content": output,
                }
            ),
            tools=tools
        )
        text_output = final_response.candidates[0].content.parts[0].text
        print(text_output)
        return text_output