#include <iostream>
#include <unistd.h>  
#include <sys/wait.h> 

using namespace std;

// Function to calculate the nth Fibonacci number
int fibonacci(int n) 
{
    if (n <= 1) 
        return n;

    int a = 0, b = 1, c;

    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}


int square(int num) {
    return num * num;
}


int cube(int num) 

{
    return num * num * num;
}

int main() 
{
    int n = 10;  
    pid_t pid1, pid2;

    
    cout << "Hard-coded value of n: " << n << endl;

    int fib = fibonacci(n); 
    
    cout << "Parent Process: The " << n << "th Fibonacci number is " << fib << endl;

    // Create the first child process
    pid1 = fork();

    if (pid1 < 0)
     {
        // Fork failed
        cerr << "Fork failed!" << endl;
        return 1;
    }

    if (pid1 == 0) 
    {
        // Child Process 1 formed
        cout << "Child Process 1: Calculating square of " << fib << endl;
        int squareResult = square(fib);
        cout << "Child Process 1: The square of " << fib << " is " << squareResult << endl;

        // Create the second child process
        pid2 = fork();

        if (pid2 < 0) 
        {
            // Fork failed
            cerr << "Fork failed!" << endl;
            _exit(1);
        }

        if (pid2 == 0) 
        {
            // Child Process 2
            cout << "Child Process 2: Calculating cube of " << fib << endl;
            
            
            int cubeResult = cube(fib);
            
            cout << "Child Process 2: The cube of " << fib << " is " << cubeResult << endl;
            _exit(0);  
            
            
        } 
        
        }
          return 0;
        }
        
         
   
   


