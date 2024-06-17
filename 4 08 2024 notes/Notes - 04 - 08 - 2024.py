#####################
## Dalton Murray    #
## 04/08/2024       #
## Notes            #
#####################
import sys # Required for system functions

import openai
from openai import OpenAI

# Defines the __main__ function
def __main__():

    ###
    # client = OpenAI(api_key = "")

    # prompt = "The quick brown fox jumps over the lazy"

    # response = client.completions.create(
    #     prompt = prompt,
    #     model = "gpt-3.5-turbo-instruct",
    #     top_p = 0.1,
    #     max_tokens = 2,
    #     frequency_penalty = 0,
    #     presence_penalty = 0,
    #     stream = True
    # )

    # for part in response:
    #     print(part.choices[0].text or "")
    ###

    ###
    client = OpenAI(api_key = "")

    prompt = "Write a poem about the sea"

    response = client.completions.create(
        prompt = prompt,
        model = "davinci-002",
        temperature = 0.7,
        max_tokens = 100,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    for part in response:
        print(part.choices[0].text or "")
    ###

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
