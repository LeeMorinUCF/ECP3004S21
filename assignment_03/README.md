# Tips for Assignment 3

## Exercise 1:

For the function ```quad_roots_1()```, 
assume that the user will only ask you for roots of a function
such that the real roots exist.
You will make a more robust version of the function in Exercise 2. 

### Tip for finding test cases

For Exercises 1 and 2, there are a few ways developing test cases:
- choose roots ```x_1``` and ```x_2``` first 
and multiply the terms in ```(x - x_1)*(x - x_2)``` (on paper) 
to get the coefficients for your test case.  
- plug the roots into the quadratic equation to make sure the output is close to zero. 


## Testing the examples in your docstring

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



## New Files for Solutions and Grading

I ran your programs and those from the suggested solutions 
and these programs output the results you see above. 

- The file ```my_A3_functions.py``` is your submission. 
When I run it, it produces the output ```my_A3_functions_out.txt```. 
This shows the results of evaluating your examples. 
Ideally, you see all of your examples printed out. 
If not, it must have failed somewhere. 


- The file ```my_A3_functions_soln.py``` is the suggested solutions. 
When I run it, it produces the output ```my_A3_functions_soln_out.txt```. 
This produces the output of ```doctest``` and the suggested examples as test cases.


- The file ```my_A3_functions_soln_test.py``` is a script that runs examples 
to test the suggested solutions ```my_A3_functions_soln.py```. 
When I run it, it produces the output ```my_A3_functions_soln_test_out.txt```. 
It produces the same output as above, twice, because it reads the script, 
producing all the output in ```my_A3_functions_soln_out.txt``` 
and then runs ```doctest``` and the suggested examples again.
The second version has extra commands so it will still work after some kinds of errors. 


For testing your script, I split these tests into two parts.


- The file ```my_A3_functions_doctest.py``` is a script that runs 
the examples in your docstrings to test your submission ```my_A3_functions.py```. 
When I run it, it produces the output ```my_A3_functions_doctest_out.txt```. 

- The file ```my_A3_functions_examples.py``` is a script that runs 
examples to test your submission ```my_A3_functions.py```. 
When I run it, it produces the output ```my_A3_functions_examples_out.txt```. 
These tests have extra commands so that it will continue after an error
in the individual functions. 
If there is a failure in your script, it only defines the functions
before the failure, so all later test cases will fail. 


