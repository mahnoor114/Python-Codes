#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[10]:


class Quiz:
    def __init__(self):
        
        self.questions
        [
            {"question 1":"Who is the developer of python language?","answer":"Guido van Rossum"},
            {"question 2":"what is the capital of Italy?","answer":"Rome"},
            {"Question 3":"who was the first major Gen. of Pakistan?","answer":" Quaid-e-Azam Muhammad Ali Jinnah"}  
        ]
        
    self.score=0.0
        
    def questions(self,question,ans):
        user_ans=input(question +" ")
        if user_ans.strip().lower()==answer.lower():
            self.score+=1
            print(f"CORRECT!")
            
        else:
            print(f"sorry! wrong answer =<")
            print(f"correct answer is {answer}")
            
    def start_quiz(self):
        print(f"HI! WELCOME =>")
        print(f"please answer the following questions")
        
        for q in self.questions:
            self.question(q["question"], q["answer"])
            
            
            
        print(f"\nQuiz Over! Your score is: {self.score} out of {len(self.questions)}")
        
        
if __name__ == "__main__":
    quiz_app = QuizApplication()
    quiz_app.start_quiz()
        
        
        


# In[ ]:




