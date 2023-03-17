import openai

# retrieve and set the api key
api_key_file = open("apikey.txt", "r")
api_key = api_key_file.readline()
api_key_file.close()
openai.api_key = api_key

# the initial context of the chat, you can change it to tune the personality of the assistant.
chat_messages = [{ "role" : "system", "content" : "You are a helpful assistant."}]

# generate response based on the current chat messages
# it starts with the initial context and gets expanded by user inputs and generated responses
# see https://platform.openai.com/docs/api-reference/chat/create
def generate_response(chat_messages):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",    # used model
        messages = chat_messages,   # the array of messages
        max_tokens = 1000,          # max value of gpt-3.5-turbo is 4096
        temperature = 0.5,          # 0.0 = correct, 1.0 = creative
        n = 1                       # number of choices generated for each input message
    )
    # the generated json is trimmed to include the content of the message only
    return completion.choices[0].message.content    

# the actual conversation starts here
print("You speak to a ChatBot powered by GPT-3.5-Turbo, enter ABORT to terminate.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "abort":
        print("Chat terminated.")
        break
    chat_messages.append({ "role" : "user", "content" : user_input})
    response = generate_response(chat_messages)
    chat_messages.append({ "role" : "assistant", "content" : response})
    print("ChatBot: " + response)