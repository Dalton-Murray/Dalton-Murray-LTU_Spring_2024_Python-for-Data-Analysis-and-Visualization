#####################
## Dalton Murray    #
## OpenAI           #
#####################
import sys
import csv

import openai
from openai import OpenAI

###! This uses openAI library 1.16.2/latest

# Defines the __main__ function
def __main__():
    client = OpenAI(api_key = "")

    SEED = 1

    ### Image recognition, healthcare
    # response = client.chat.completions.create(
    #     model = "gpt-4-1106-vision-preview",
    #     seed = SEED,
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": [
    #             {"type": "text", "text": "What’s in this image?"},
    #             {
    #             "type": "image_url",
    #             "image_url": {
    #                 "url": "https://media.istockphoto.com/id/152499925/photo/broken-leg-x-ray.jpg?s=612x612&w=0&k=20&c=ks0mRUknz4zJGbJWQQbYYL7FeolQsAtmFUxqCU0zECw=",
    #             },
    #             },
    #         ],
    #         }
    #     ],
    #     max_tokens=300,
    # )

    # response_message = response.choices[0].message.content
    # print(response_message)
    ###

    ### RegEx generation
    # response = client.chat.completions.create(
    #     model = "gpt-4-0125-preview",
    #     seed = SEED,
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": [
    #             {"type": "text", "text": "I want you to act as a RegEx generator. Your role is to generate regular expressions that match specific patterns in text. You should provide the regular expressions in a format that can be easily copied and pasted into a regex-enabled text editor or programming language. Generate a regular expression that matches an email address."},
    #         ],
    #         }
    #     ],
    #     max_tokens=300,
    # )

    # response_message = response.choices[0].message.content
    # print(response_message)
    ###

    ### Personal information finder
    # file = open("./1-MB-Test.csv")
    # file_contents = csv.reader(file)
    # header = []
    # header = next(file_contents)
    # rows = []
    # for row in file_contents:
    #     rows.append(row)

    # response = client.chat.completions.create(
    #     model = "gpt-4-0125-preview",
    #     seed = SEED,
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": [
    #             {"type": "text", "text": f"You are a Cybersecurity expert. Does this contain any personally identifiable information, PII? Only respond with yes or no {header}, {rows}"},
    #         ],
    #         }
    #     ],
    #     max_tokens=300,
    # )

    # response_message = response.choices[0].message.content
    # print(response_message)
    ###

    ### Malware detector
    # with open("./example_keylogger.py") as file:
    #     lines = file.readlines()

    # response = client.chat.completions.create(
    #     model = "gpt-4-0125-preview",
    #     seed = SEED,
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": [
    #             {"type": "text", "text": f"You are a Cybersecurity expert. Does this file contain anything that looks like malware? {lines}"},
    #         ],
    #         }
    #     ],
    #     max_tokens=300,
    # )

    # response_message = response.choices[0].message.content
    # print(response_message)
    ###

    ### Image recognition, automation, captcha
    # response = client.chat.completions.create(
    #     model = "gpt-4-1106-vision-preview",
    #     seed = SEED,
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": [
    #             {"type": "text", "text": "Could you identify what images in this image contains trees?"},
    #             {
    #             "type": "image_url",
    #             "image_url": {
    #                 "url": "https://10web.io/wp-content/uploads/2022/05/reCaptcha-example.jpg",
    #             },
    #             },
    #         ],
    #         }
    #     ],
    #     max_tokens=300,
    # )

    # response_message = response.choices[0].message.content
    # print(response_message)
    ###

    ### Image generation
    # response = client.images.generate(
    #     model = "dall-e-3",
    #     prompt = "A sleek, modern, professional icon/logo. Black and white. Line art focus.",
    #     size = "1024x1024",
    #     quality="standard",
    #     n = 1,
    # )

    # image_url = response.data[0].url
    # print(image_url)
    ###



# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
