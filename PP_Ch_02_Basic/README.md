# PP_Ch_2_Basic



```python 
>>> 4 + 13
17

``` 

```python 
>>> 15 - 3
12
>>> 4 * 7
28

``` 

```python 
>>> degrees_celsius = 26.0

``` 

```python 
>>> degrees_celsius = 26.0 + 5
>>> degrees_celsius
31.0

``` 

```python 
>>> degrees_celsius = 15.5
>>> difference = 100 - degrees_celsius
>>> difference
84.5
``` 

```python 
>>> degrees_celsius = 26.0
>>> 9 / 5 * degrees_celsius + 32
78.80000000000001
>>> degrees_celsius = 0.0
>>> 9 / 5 * degrees_celsius + 32
32.0

``` 

```python 
>>> degrees_celsius = 26.0
>>> degrees_celsius
26.0
>>> 9 / 5 * degrees_celsius + 32
78.80000000000001
>>> degrees_celsius / degrees_celsius
1.0

``` 

```python 
>>> 10000000000 + 0.00000000001
10000000000.0

``` 

```python 
>>> # Python ignores this sentence because of the # symbol.

``` 

```python 
>>> (212 - 32) * 5 / 9 # Convert 212 degrees Fahrenheit to Celsius.
100.0

``` 

```python 
>>> 5 / 2
2.5

``` 

```python 
>>> 4 / 2
2.0

``` 

```python 
>>> 17 // 10
1

``` 

```python 
>>> 17.0 - 10
7.0
>>> 17 - 10.0
7.0

``` 

```python 
>>> 17 - 10.
7.0
>>> 17. - 10
7.0

``` 

```python 
>>> 17.0 - 10.0
7.0

``` 

```python 
>>> 3.3 // 1
3.0
>>> 3 // 1.0
3.0
>>> 3 // 1.1
2.0
>>> 3.5 // 1.1
3.0
>>> 3.5 // 1.3
2.0

``` 

```python 
>>> 53 // 24
2

``` 

```python 
>>> 53 % 24
5

``` 

```python 
>>> room_temperature_c = 20
>>> cooking_temperature_f = 350
>>> oven_heating_rate_c = 20
>>> oven_heating_time = (
... ((cooking_temperature_f - 32) * 5 / 9) - room_temperature_c) / \
... oven_heating_rate_c
>>> oven_heating_time
7.833333333333333

``` 

```python 
>>> oven_heating_time = (
...     ((cooking_temperature_f - 32) * 5 / 9) - room_temperature_c) / \
...     oven_heating_rate_c

``` 

```python 
>>> oven_heating_time = (
...     ((cooking_temperature_f - 32) * 5 / 9) -
...      room_temperature_c) / \
...     oven_heating_rate_c

``` 

```python 
>>> room_temperature_c = 20
>>> cooking_temperature_f = 350
>>> cooking_temperature_c = (cooking_temperature_f - 32) * 5 / 9
>>> oven_heating_rate_c = 20
>>> oven_heating_time = (cooking_temperature_c - room_temperature_c) / \
...     oven_heating_rate_c
>>> oven_heating_time
7.833333333333333

``` 

```python 
>>> -5
-5
>>> --5
5
>>> ---5
-5

``` 

```python 
>>> -17 // 10
-2
``` 

```python 
>>> -17 % 10
3
>>> 17 % -10
-3
``` 

```python 
>>> 12 = x
  File "<stdin>", line 1
SyntaxError: can't assign to literal

``` 

```python 
>>> 3 ** 6
729

``` 

```python 
>>> 212 - 32 * 5 / 9
194.22222222222223

``` 

```python 
>>> -2 ** 4
-16
>>> -(2 ** 4)
-16
>>> (-2) ** 4
16

``` 

```python 
>>> (212 - 32) * 5 / 9
100.0
``` 

```python 
>>> 2 / 3
0.6666666666666666
>>> 5 / 3
1.6666666666666667

``` 

```python 
>>> 2 / 3 + 1
1.6666666666666665
>>> 5 / 3
1.6666666666666667

``` 

```python 
>>> score = 50
>>> score
50
>>> score = score + 20
>>> score
70

``` 

```python 
>>> score = 50
>>> score
50
>>> score += 20
>>> score
70

``` 

```python 
>>> (2 +
... 3)
5
>>> 2 + \
... 3
5

``` 

```python 
>>> 2 +
  File "<stdin>", line 1
    2 +
      ^
SyntaxError: invalid syntax

``` 

```python 
>>> 3 + moogah
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'moogah' is not defined

``` 

```python 
>>> difference = 20
>>> double = 2 * difference
>>> double
40
>>> difference = 5
>>> double
40

``` 

```python 
>>> number = 3
>>> number
3
>>> number = 2 * number
>>> number
6
>>> number = number * number
>>> number
36

``` 

```python 
>>> d = 2
>>> d *= 3 + 4
>>> d
14

``` 

```python 
>>> number = 10
>>> number *= number
>>> number
100

``` 

```python 
>>> number = 10
>>> number = number * number
>>> number
100

``` 

