from litellm import completion
import os
from uv_project.api_key import GEMINI_API_KEY

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hi, my name is Zain. I was born in 2004. Considering the current year is 2025, can you tell me how old I am now?","role": "user"}]
    )

    print(response.choices[0].message.content)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, do you know which powerful GPU NVIDIA is planning to launch next?","role": "user"}]
    )

    print(response.choices[0].message.content)

