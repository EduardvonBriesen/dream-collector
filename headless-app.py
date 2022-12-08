import os
import openai
import speech_recognition as sr

r = sr.Recognizer()

openai.api_key = os.getenv("OPENAI_API_KEY")

dream_list = []
prompt_list = []


def add_dream(dream):
    dream_list.append(dream)
    print("Adding dream: " + dream)
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(),
        temperature=1,
        max_tokens=100,
    )
    print("New prompt:" + response.choices[0].text)
    prompt_list.append(response.choices[0].text)


def generate_prompt():
    print("Generating prompt")
    # open text file in read mode
    text_file = open("example_prompts.txt", "r")
    text_file.close()

    return """Generate a new prompt with the phrases {}""".format(
        example_prompts,
        dream_list
    )


# def get_image(prompt):
#     base_url = "https://api.newnative.ai/stable-diffusion?prompt="

#     response = requests.request("GET", base_url + prompt)
#     data = response.json()
#     print(data["image_url"])


print("Starting")
while True:
    input_text = ""
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        
        try:
            # using google speech recognition
            input_text = r.recognize_google(audio_text)
            print("Text: "+input_text)
        except:
            print("Sorry, I did not get that")

    add_dream(input_text)