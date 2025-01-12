from openai import OpenAI

class ChatBot:
    def __init__(self, model='gpt-3.5-turbo'):
        self.client=OpenAI(api_key='********************************')
        self.messages = []
        self.model = model

    def add_message(self,role,content):
        if role in ['user', 'assistant']:
            self.messages.append(
                {'role': role, 'content': content}
            )
        else:
            raise ValueError('Role must be either "user" or "assistant"')

    def get_response(self,user_message):
        self.add_message("user",user_message)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            # temperature=0.7,
            # max_tokens=100,
            # n=1,
            # stop=None
        )

        print(response)
        model_message = response.choices[0].message.content
        self.add_message("assistant",model_message)
        return model_message

bot = ChatBot()

if __name__ == '__main__':
    print("Welcome")
    print(bot.get_response("Kto jest prezydentem Polski"))

    # Welcome

    # Obecnie
    # prezydentem
    # Polski
    # jest
    # Andrzej
    # Duda.Jego
    # kadencja
    # rozpoczęła
    # się
    # w
    # 2015
    # roku, a
    # został
    # ponownie
    # wybrany
    # na
    # drugą
    # kadencję
    # w
    # 2020
    # roku.
