from http import HTTPStatus
from dashscope.audio.asr import Transcription
import json

# 若没有将API Key配置到环境变量中，需将下面这行代码注释放开，并将apiKey替换为自己的API Key
import dashscope
dashscope.api_key="sk-xxx",

transcribe_response = Transcription.async_call(
    model='paraformer-v2',
    file_urls=['https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3'],
    language_hints=['zh', 'en']  # “language_hints”只支持paraformer-v2模型
)

while True:
    if transcribe_response.output.task_status == 'SUCCEEDED' or transcribe_response.output.task_status == 'FAILED':
        break
    transcribe_response = Transcription.fetch(task=transcribe_response.output.task_id)

if transcribe_response.status_code == HTTPStatus.OK:
    print(json.dumps(transcribe_response.output, indent=4, ensure_ascii=False))
    print('transcription done!')