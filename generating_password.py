#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
import string

def gen_pass(length, digits, special_characters):
    characters = string.ascii_lowercase
    
    if digits:
        characters += string.digits
        
    if special_characters:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected.")
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        length = int(input("Please enter the length of your password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        digits = input("Do you want digits in your password? (yes/no): ").strip().lower() == 'yes'
        special_characters = input("Do you want special characters in your password? (yes/no): ").strip().lower() == 'yes'
        
        password = gen_pass(length, digits, special_characters)
        print(f"Password is: {password}")
    
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()


# In[8]:





# In[5]:





# In[ ]:




