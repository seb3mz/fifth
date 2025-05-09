import os
from openai import OpenAI

client = OpenAI(
    #base_url='https://api.openai-proxy.org/v1',
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    #api_key=os.environ.get("OPENAI_API_KEY"),
    api_key=os.environ.get("DASHSCOPE_API_KEY")
)

stream = client.chat.completions.create(
    model="deepseek-r1",
    messages=[{"role": "user", "content": "讲一个关于人工智能的故事"}],
    #stream=True,
)

# for chunk in stream:
#     if chunk.choices:
#         print(chunk.choices[0].delta.content or "", end="")
# print("\n")

# 通过reasoning_content字段打印思考过程
print("思考过程：")
print(stream.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("最终答案：")
print(stream.choices[0].message.content)