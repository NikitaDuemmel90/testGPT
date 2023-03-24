import hvac   
import openai

##############################################################
#   HashiCorp Vault Initialization and retrieval of API keys 
##############################################################
class Keychain:
    def __init__(self):
        client = hvac.Client(
            url='https://vault-int.app.corpintra.net/',
            namespace='HCV-test'
        )
        approle_file = open("approle.txt", "r")
        approle_secret_id = approle_file.readline()
        approle_file.close()
        client.auth.approle.login(
            role_id='8c9d6f48-f20e-93b6-aff4-b9e1e15b4e78',
            secret_id=approle_secret_id
        )
        read_response = client.secrets.kv.read_secret_version(path='chatbot', mount_point='kv')        
        self.google_search_api_key = read_response['data']['data']['google_search_api_key']
        self.openai_api_key = read_response['data']['data']['openai_api_key']

    def get_google_search_api_key(self):
        return self.google_search_api_key
    
    def get_openai_api_key(self):
        return self.openai_api_key
        

##############################################################
#   ChatBot
##############################################################
class ChatBot:
    def __init__(self):
        # the initial context of the chat, you can change it to tune the personality of the assistant.
        self.chat_messages = [{ "role" : "system", "content" : "You are a helpful assistant."}]

    # generate response based on the current chat messages
    # it starts with the initial context and gets expanded by user inputs and generated responses
    # see https://platform.openai.com/docs/api-reference/chat/create
    def __generate_response(self):
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",        # used model
            messages = self.chat_messages,  # the array of messages
            max_tokens = 1000,              # max value of gpt-3.5-turbo is 4096
            temperature = 0.5,              # 0.0 = correct, 1.0 = creative
            n = 1                           # number of choices generated for each input message
        )
        # the generated json is trimmed to include the content of the message only
        return completion.choices[0].message.content    

    def startConversation(self):
        # the actual conversation starts here
        print("You speak to a ChatBot powered by GPT-3.5-Turbo, enter ABORT to terminate.")
        while True:
            user_input = input("\nUser: ")
            if user_input.lower() == "abort":
                print("Chat terminated.")
                break
            self.chat_messages.append({ "role" : "user", "content" : user_input})
            response = self.__generate_response()
            self.chat_messages.append({ "role" : "assistant", "content" : response})
            print("\nChatBot: " + response)

def main():
    keychain = Keychain()
    openai.api_key = keychain.get_openai_api_key()
    chatbot = ChatBot()
    chatbot.startConversation()

if __name__ == "__main__":
    main()