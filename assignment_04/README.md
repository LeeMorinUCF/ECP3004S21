# Tips for Assignment 4


## Question 2: Testing the examples in your docstring

If you have entered your examples in the proper format within your function docstrings, 
you can test them automatically with the ```doctest``` module. 

```python
import doctest

doctest.testmod()
```

It should print out tests of the examples in your docstring, 
including a message about whether the tests passed or failed. 

Don't worry about test cases that fail in the smaller decimal points.
It is fine as long as your answer is accurate to several decimals. 


## Finding Good Test Cases

Good test cases have two main characteristics:
- They are easy to calculate.
- They detect potential errors.

These are some tips to choose simple examples that find errors: 
- A list of length three or four might be enough
- Choose values that evaluate to integers. 
For example, with your ```ssr``` functions, 
choose numbers such that ```y - beta_0 - x*beta_1``` are all integers. 
- For linear regression, choose one example that is perfectly linear. 
That is, choose any ```beta_0```, ```beta_1``` and ```x``` 
and calculate ```y = beta_0 + x*beta_1``` so that the linear equation holds exactly.
- Make sure to choose other examples that do not fit exactly on a line. 
An easy type of error is symmetric has four elements ```error = [1, -1, -1, 1]```.
Use it to calculate an example with ```y``` 
using ```y = beta_0 + x*beta_1 + error```.
- For functions that involve the log or exponential, choose values of 
```beta_0```, ```beta_1``` and ```x``` such that they add up to ```math.log(z)``` for some number ```z``` because ```math.exp(math.log(z)) = z```. 
Search online for exponentials and logarithms for a review. 
- Find some other way of calculating the function, such as with a calculator or a spreadsheet. Your python version will scale to much larger datasets but should work if it calculates correctly for even a pair of small lists. 


## Test Your Full Script

- After you finish a function, test it with your examples. 
- After you finish all the functions, test them all together with ```doctest```. 
- When they are all finished, run the entire script from top to bottom. 
Press ```F5``` or the green "Play" button with the green triangle.
- If there are any errors, find where they are by running small sections until you isolate the error. 
- The error message gives clues about the problem and ```^``` points to the location of the error. Online help becomes more useful as you gain experience. 
- Shut down Spyder and reopen it to test your full script one more time, 
starting fresh with nothing else in memory. 
Sometimes previous calculations make your functions work temporarily 
but the script fails when run from an empty workspace. 

It's important that your script runs without errors because it stops running once it hits the first error and all the rest of the functions will not be defined
and the examples will fail. 



