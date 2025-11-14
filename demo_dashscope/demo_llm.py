import os
from openai import OpenAI


client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-7813347557f943adab65c5bb64820e36",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {"role": "system", "content": """<instruction> 根据提供的上下文内容和模型自身的知识，生成最符合用户问题的答案。在回答时，请识别并展示与问题相关联的图片，格式为：![img](a img url)。请确保输出中不包含任何 XML 标签。 步骤说明： 1. 读取输入中的上下文内容。 2. 识别上下文中所有以 `<!-- [some description] --> ![img](a img url)` 形式出现的图片描述。 3. 分析用户的问题，判断是否与这些图片描述相关。 4. 如果相关，则在答案中插入对应的图片链接：![img](a img url)。 5. 确保输出仅包含自然语言回答，不包含任何 XML 标签或结构。 6. 优先使用参考信息中的内容，若无相关信息或信息不足可从你自身的知识中参考回答。 </instruction> <example> context: "这里是一段上下文内容。<!-- 这是一张显示系统架构的图片 --> ![img](https://example.com/arch.png)" query: "系统架构是怎样的？" answer: "系统的架构如下所示：![img](https://example.com/arch.png)" </example> <example> context: "" query: "系统架构是怎样的？" answer: "系统架构是描述系统各组件、组件间关系及运行规则的整体框架，不同类型系统（如软件、硬件、物联网）的架构设计差异极大，核心是为了实现高可用、可扩展、易维护的目标。" </example> <example> context: "以下是一个关于天气的描述。<!-- 这是一张显示晴天的图片 --> ![img](https://example.com/sunny.png)" query: "今天天气怎么样？" answer: "今天天气晴朗，如图所示：![img](https://example.com/sunny.png)" </example>"""},
        {"role": "user", "content": "sam的主要抗辩点是什么"},
        {"role": "system", "content": "根据提供的上下文内容，没有提到与“sam的主要抗辩点”相关的信息。因此无法提供具体的答案。如果您有更多相关信息，欢迎补充。"},
        {"role": "user", "content": """<input> context: # 当被问及OpenAI微薄的收入时，Sam Altman失去了冷静 —— “够了。” 公众号: F8AI 2025年11月4日 12:11 OpenAI 计划投入巨资建设人工智能基础设施，因为它正试图通过庞大的计算规模来实现通用人工智能。尽管微软的收入远远落后于其巨额支出，但最近公布的微软收益显示，由萨姆·奥特曼领导的这家公司上个季度亏损高达 115 亿美元。就连其重磅人工智能聊天机器人 ChatGPT（该公司的大部分收入都来自 ChatGPT）似乎也面临着新用户增长停滞的困境。OpenAI难以说服其 8 亿活跃 ChatGPT 用户中超过 5% 的人付费订阅。在最近接受播客主持人兼 OpenAI 投资者 Brad Gerstner 的采访时，当 Altman 被直接问及这一切是如何运作的，他顿时失去了冷静。“一家年收入130亿美元的公司，怎么可能做出1.4万亿美元的支出承诺？”格斯特纳问他。“萨姆，你听到了这些批评。”“如果你想卖掉你的股份，我会帮你找到买家，”奥特曼吃惊地简短回答道。“够了。”面对这场冲突，格斯特纳大笑起来。“我认为很多人对我们的计算技术或其他方面表现出极大的热情，他们很乐意购买我们的股票，”奥特曼坚持己见。“我们可以很快地把你的股票或者其他任何人的股票卖给那些在推特上对此大肆炒作的人。”这段在社交媒体上疯传的激烈争论，凸显了人们对人工智能泡沫日益增长的担忧，各公司越来越难以向投资者保证他们的投资会有回报。甚至奥特曼本人也在8 月份接受记者采访时承认，我们正处于“投资者整体对人工智能过度兴奋的阶段”，这可能会导致“某人”损失“巨额资金”。事关重大。尽管OpenAI亏损数十亿美元，但它目前被认为是全球最有价值的私营公司。伯恩斯坦研究公司分析师斯泰西·拉斯贡在最近一份致投资者的报告中指出，奥特曼“有能力让全球经济崩溃十年，或者带领我们走向成功”。奥特曼的简短回答也凸显出他似乎已经厌倦了为OpenAI的巨额支出辩解。尽管格斯特纳提出的问题或许合情合理，而且很可能也是无数投资者心中的疑问。OpenAI首席执行官对格斯特纳对公司营收的估算提出异议，但除了声称“营收正在快速增长”以及OpenAI“公开押注公司将继续增长”之外，并未提供具体数字。由于OpenAI并非上市公司，因此从技术上讲，该公司没有义务公开这些数据——尽管这种情况可能很快就会改变。路透社上周报道称，OpenAI正在“为首次公开募股（IPO）做准备，IPO后公司的估值可能高达1万亿美元”。奥特曼似乎也认同这种可能性，他开玩笑说，如果公司上市，他很乐意看到做空者“吃亏”。futurism.com query: sam是指奥特曼或者alterman </input>"""},
    ],
    # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
    # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
    # extra_body={"enable_thinking": False},
)
print(completion.model_dump_json())