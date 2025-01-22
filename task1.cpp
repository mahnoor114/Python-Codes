#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int reverseNumber(int num) 
{
    int reversed = 0;
    while (num > 0) 
    {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }
    return reversed;
}

int isPalindrome(int num) 
{
    return num == reverseNumber(num);
}

int main() 
{
    int num;
    pid_t pid;

    cout<<"\n enter a number";
    
    cin>>num;

    pid = fork();  // Create child process

    if (pid < 0)
     {
    
        cout<<"\n fork has failed!";
        return 1;
        
    } 
    
    else if (pid == 0) 
    
    
    {  
    
    // Child process
        
        
        int reversed = reverseNumber(num);
        cout<<"\n reversed of number is"<<reversed<<endl;
    } 
    else 
    {  // Parent process
    
        wait(NULL);  // Wait for child process to finish
        
        
        if (isPalindrome(num)) 
        {
            cout<<"it is palindrome";
            
        } 
        
        else 
        
        {
            cout<<"\n not palidrome";
        }
    }

    return 0;
}

