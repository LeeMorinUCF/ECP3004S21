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


