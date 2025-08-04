#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

 
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.ok:
        data = response.json()
        meaning = data[0]['meanings'][0]
        definition = meaning['definitions'][0]['definition']
        return f"{word.capitalize()} ({meaning['partOfSpeech']}): {definition}"
    else:
        return f"Sorry, I couldn't find the meaning of '{word}'."

 
def chat():
    print("📖 DictionaryBot: Ask me for word meanings! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'bye':
            print("📖 DictionaryBot: Goodbye!")
            break

         
        if user_input.startswith("define "):
            word = user_input[7:]   
            print("📖 DictionaryBot:", get_definition(word))
        else:
            print("📖 DictionaryBot: Try asking me like 'define happiness'.")

 
if __name__ == "__main__":
    chat()


# In[ ]:





# In[ ]:




