import json
from sarufi import Sarufi
sarufi = Sarufi(username="kamemia18@yahoo.com", password="cuti3.5miley1")

def create_insuarance_bot():
    response = sarufi.create_bot(
        name="M-jengo Chatbot",
        description="My bot can do a lot",
        intents=json.load(open("data/intents.json")),
        flow=json.load(open("data/flow.json")),
    )

    print(response)


def chat():
    while True:
        message = input("Me : ")
        response = sarufi.chat(project_id=352, chat_id="furaha", message=message)
        print(f"Bot: {response}")


def respond(message, chat_id):
    response = sarufi.chat(bot_id=3, chat_id=chat_id, message=message)
    return response.get("message")


if __name__ == "__main__":
    # create_insuarance_bot()
    chat()