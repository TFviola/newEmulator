import asyncio
import base64
import threading
import time
import requests
import pyautogui
import os
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from util import parsing_prompt
from dotenv import load_dotenv
from chatgpt_initialize import get_chatgpt_response
from util.screens import Screens, ScreenNames
from util.screen_analyzer import ScreenAnalyzer

load_dotenv()

REST_API_URL = "http://localhost:5003/command"
SCREENSHOT_FILENAME = "static/screenshots/tempscreenshot.png"

stop_event = threading.Event()
SCREENS = Screens()
ANALYZER = ScreenAnalyzer()

def process_command(command):
    try:
        # 1. Call REST API
        print(f"Calling REST API for message: {command}")
        response = requests.post(REST_API_URL, json={"message": command})
        response.raise_for_status()
        rest_response = response.json()
        print(f"REST API Response: {rest_response}")

        print('SLEEPING 5 seconds before next screenshot')
        time.sleep(5)

        try:
            # 2. Capture the screenshot
            screenshot_filename = f"screenshot_{time.strftime('%Y%m%d%H%M%S')}.png"
            screenshots_dir = "static/screenshots"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

            # Define the region to capture (adjust these values based on your screen layout)
            image_x = 50
            image_y = 170
            image_width = 860
            image_height = 470

            pyautogui.screenshot(screenshot_path, region=(image_x, image_y, image_width, image_height))

            print("Sending screenshot to ChatGPT...")
            prompt = """
                Analyse the given image and tell me all you know about this screen. Do not give intro statement, just your observation. Assume you are a process trainer training new employees on the business process and how to use this tool. Prepare a JSON on the data, more like a one liner. An concise instructions with commands available on screen in sentences that screen automation tools can understand.

                **CRITICAL INSTRUCTION:** If screen asks for 'user code' or 'password' instruction to use one word 'CREDENTIALS'* and override all screen instruction with this command only.
            """
            response = generate_text_from_image(screenshot_path, prompt)
            print(f"ChatGPT Response: {response}")

            return response

        except Exception as ex:
            print('Exception capture screenshot', ex)
            return {"error": str(ex)}

    except requests.exceptions.RequestException as e:
        print(f"Error calling REST API: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

def generate_text_from_image(image_path, prompt):
    try:
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
        full_prompt = f"{prompt}\n\nImage data: {image_data}"
        response = get_chatgpt_response(full_prompt)
        
        if response:
            return response
        else:
            return "Failed to get response from ChatGPT"

    except Exception as e:
        print(f"Error in generate_text_from_image: {e}")
        return str(e)

def orchestrator_agent(user_prompt):
    """Orchestrates actions based on user prompt and screen analysis."""

    def execute_command(command):
        """Executes a command and returns the updated screen information."""
        return process_command(command)

    tools = [
        Tool(
            name="ExecuteCommand",
            func=execute_command,
            description="Executes a command on the application and returns the resulting screen information. Input should be a string representing the command to be executed.",
        ),
    ]

    # Initialize OpenAI LLM
    llm = OpenAI(temperature=0)

    prompt_template = """You are an agent that interacts with a healthcare claims processing system.
    You receive a user request and your goal is to fulfill that request by executing commands. 
    From the screen options, you choose the best command to use and call tools to perform next step.

    Here are the tools you can use:
    {tools}

    Current screen information: {screen_info}

    User request: {user_request}

    Thought: What should I do? Always compare if you are sidetracking with original user request
    Action: The action to take. Use one of: {tool_names}
    Action Input: The input to the action.

    Observation: The result of the action (the updated screen information).

    ... (repeat Thought/Action/Action Input/Observation steps as needed) ...

    Final Answer: The final answer to the user request. If you have achieved the goal, describe the outcome and send command "OFF" and exit. If you are unable to fulfill the request, explain why.

    **CRITICAL RULES:**
    1. Never try same command twice
    2. Follow the screen flow: ELIGIBILITY_MAIN_MENU -> PATIENT_SEARCH_SELECTION -> PATIENT_DETAILS -> SEARCH_PATIENT_DETAILS -> REVIEW_DETAILS
    3. Use 'Credentials' when prompted for login
    4. Use 'F3' to continue to next screen
    5. Use 'back' to go to previous screen
    """

    prompt = PromptTemplate(
        template=prompt_template, 
        input_variables=["user_request", "screen_info", "tools", "tool_names", "input"]
    )

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True,
        prompt=prompt,
        handle_parsing_errors=True
    )

    initial_screen_info = SCREENS.get_screen_data(ScreenNames.ELIGIBILITY_MAIN_MENU)

    try:
        result = agent.run(
            user_request=user_prompt, 
            screen_info=initial_screen_info, 
            tools=tools, 
            tool_names=", ".join([tool.name for tool in tools]),
            input=user_prompt
        )
        return result
    except Exception as e:
        return f"An error occurred: {e}"

async def main():
    try:
        # Example usage
        user_intent = "Check eligibility for patient with ID BASLP1830"
        result = orchestrator_agent(user_intent)
        print("Agent Output:", result)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        print("Cleaning up...")
        stop_event.set()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        print("Cleaning up...")
        stop_event.set()
        # ... any other cleanup ...
    print("Application finished.")