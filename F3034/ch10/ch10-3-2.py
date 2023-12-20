import openai

openai.api_key = "<API-KEY>"
reply_msg = "客戶你好..."

while True:
    input_msg = input("你: ")
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",      
      messages = [
            {"role": "system", "content": "你是客服機器人"},
            {"role": "assistant", "content": reply_msg},
            {"role": "user", "content": input_msg}
                 ]
    )
    reply_msg = response.choices[0].message.content
    print(reply_msg)