import dashscope

messages = [
    {
        "role": "system",
        "content": [
            # 此处用于配置定制化识别的Context
            {"text": ""},
        ]
    },
    {
        "role": "user",
        "content": [
            {"audio": "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3"},
        ]
    }
]
class ASR:

    __client = None

    @classmethod
    def client(cls):
        if cls.__client is None:
            cls.__client = dashscope.MultiModalConversation
        return cls.__client

#
# response = ASR.client().call(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
#     api_key="sk-xxxx",
#     model="qwen3-asr-flash",
#     messages=messages,
#     result_format="message",
#     asr_options={
#         # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
#         "enable_lid":True,
#         "enable_itn":False
#     }
# )
# print(response)



response = ASR.client().call(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
    api_key="sk-xxxx",
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        # "language": "zh", # 可选，若已知音频的语种，可通过该参数指定待识别语种，以提升识别准确率
        "enable_lid":True,
        "enable_itn":False
    }
)
print(response.output.choices[0].message.content[0].get("text"))
print(response.output.choices[0].message.annotations[0].get("language"))