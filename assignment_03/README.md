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


