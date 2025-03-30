from dotenv import load_dotenv
import os

load_dotenv('.env')

api_key = os.getenv('OPENAI_TOKEN')
base_url = os.getenv('BASE_URL')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
prompts = {'basic': 'You are a helpful assistant',
           'main': "Please analyze the following text and identify the task's meaning, deadlines, and category according to GTD principles. If you need more information, please ask a clarifying question."}

if __name__ == "__main__":
    print(f'OPENAI_API_KEY:{api_key}')
    print(f'telegram bot token:{telegram_bot_token}')
    print(f'base_url: {base_url}')
