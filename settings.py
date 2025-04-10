from dotenv import load_dotenv
import os

load_dotenv('.env.sample')

api_key = os.getenv('OPENAI_TOKEN')
base_url = os.getenv('BASE_URL')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
prompts = {'basic': 'You are a helpful assistant',
           'main': "Please analyze the following text and identify the task's meaning, deadlines, and category according to GTD principles. If you need more information, please ask a clarifying question.",
           'main_v1': "Please analyze the following text and determine the meaning of "
                      "the task, the time frame for its completion and the category in accordance with "
                      "the principles of GTD. "
                      "Answer in special format: "
                      "Task:"
                      "Deadline:"
                      "Category:"
                      "If Username is present in the following text, use it as a Category. Finally make a json with keys Task, Deadline, Category, Username. if you don't have enough data, request it from the user."
                      "If you need more information, please ask a clarifying question.",
           'main_v2': "Please analyze the following text and identify the task's meaning, deadlines,"
                      " and category according to GTD principles. Finally make a json with keys Task, Deadline, Category, Username. if you don't have enough data, request it from the user."
           }

if __name__ == "__main__":
    print(f'OPENAI_API_KEY:{api_key}')
    print(f'telegram bot token:{telegram_bot_token}')
    print(f'base_url: {base_url}')
