import os
import openai
import google.generativeai as palm


def main():
    #result = CallChatGPT("Make python helloworld program")
    #result = CallPalm2("Make python helloworld program")
    Call("Make python helloworld program", "ChatGPT")


def Call(projectDescription, LLMName="ChatGPT"):
    if LLMName == "ChatGPT":
        return CallChatGPT(projectDescription)
    elif LLMName == "Palm2":
        return CallPalm2(projectDescription)


def CallChatGPT( projectDescription):
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=projectDescription,
    temperature=0.6,
    max_tokens=3000,
    )
    print(response.choices[0].text.strip())
    return response

def CallPalm2( projectDescription):
    
    palm.configure(api_key=os.getenv("Palm2APIKey"))

    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.7,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 4024,
        'stop_sequences': [],
        'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
        }
    prompt = f"""{projectDescription}"""

    response = palm.generate_text(
    **defaults,
    prompt=prompt
    )
    print(response.result)
    return response


if __name__ == "__main__":
    main()

