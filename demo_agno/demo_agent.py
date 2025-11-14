from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAILike
from agno.utils.pprint import pprint_run_response
db = SqliteDb(db_file="agno.db")

agent = Agent(
    model=OpenAILike(
        id="deepseek-v3",
        api_key="your-api-key",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.3,
        max_tokens=16384,
        top_p=0.9,
    ),
    db=db,
    num_history_runs=3,
    read_chat_history=True,
    add_history_to_context=True,
    markdown=True,
)
# agent.num_history_runs=3
# agent.read_chat_history=True
# agent.add_memories_to_context=True
agent.session_id="b74b1b47-53b9-43fb-a2ea-af18011db661"
agent.id="21de66f8-3c9d-4e47-8f2a-7449ad14771b"
agent.system_message = """
你是个有用的AI助手，你将凭借自己所掌握的知识礼貌地进行回答。
以下是一些重要要求：在回答问题时，你可以依据已知道相关结果作为参考。请以全面、丰富的内容进行回答。
理解问题要求:
    仔细阅读并理解用户提出的问题。
回答问题要求：
    上下文本出现人名时，必须使用真实姓名，不能使用昵称或其他形式的称呼。
    若是没有参考上下文，绝不可以伪造数据
    答案必须准确、专业，语气公平。
    如果历史消息和当前问题无关，请按照当前的问题回答，务必不要参考历史回答。
    仅提供与问题直接相关的信息，避免无关内容或重复。
    无需在答案末尾添加参考词，如：“以上内容来自”或“更多信息请参考词”。
"""

# agent.print_response(input="my name is matt", stream=True, stream_intermediate_steps=True, show_message=True)
# print()
# agent.print_response("what is my first query", stream=True, stream_intermediate_steps=True, show_message=True)

while True:
    # 获取用户的输入
    user_input = input("User: ")

    response = agent.run(input=user_input, stream=True)
    # response = agent.run(input=user_input, stream=True, stream_intermediate_steps=True)
    # pprint_run_response(response, markdown=True)
    # agent.print_response(input=user_input, stream=True, show_message=True, stream_intermediate_steps=True)
    for event in response:
        if event.event == "RunContent":
            print(f"Content: {event.content}")
        elif event.event == "ToolCallStarted":
            print(f"Tool call started: {event.tool}")
        elif event.event == "ReasoningStep":
            print(f"Reasoning step: {event.content}")
    print()

#
# pprint_run_response(response, markdown=True)
# print()
# response = agent.run(input="what are you?", stream=True)
#
# pprint_run_response(response, markdown=True)
# print()
# response = agent.run(input="what can you do?", stream=True)
#
# pprint_run_response(response, markdown=True)
# print()
# response = agent.run(input="what is my name?", stream=True)
#
# pprint_run_response(response, markdown=True)
# print()
# agent.print_response(input="hello", stream=True, stream_intermediate_steps=True, show_message=True)
# agent.print_response("Summarize the top 5 stories on hackernews", stream=True)
