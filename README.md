# Python & ML - Module 00
***GOAL***: This project aims to you to learn basic stuffs about **Python** with 11 questions.

## Instructions
- **Version**
  - Recommended python version is 3.7.
  - You can check the version of python with `python -V` command.
- **Norm** that no one likes
  - Ok. here, you can see that the NORM that made all of us painful before is back.
  - It is recommended to follow the [**`PEP 8 standards`**](https://peps.python.org/pep-0008/).
  - Check is your code with [`pycodestyle`](https://pypi.org/project/pycodestyle/). 
- function `eval` is never allowed.
- The exercies are ordered from the easiest to the hardest, please keep the order.
- Best manual or the colleague is **Google**(or chatGPT, whatever *`<;`* ).
- You can ask questions in [42AI](https://app.slack.com/client/T3T7KSKE3)/[42born2code](https://app.slack.com/client/T039P7U66)'s `#bootcamps` channel.
- Any mistakes or issues? Please report 'em in [42AI's Github Channel Issue](https://github.com/42-AI/bootcamp_python/issues).
- The project encourage you to create test programs just like old-push-swap. This means you will not be graded with the test program exists or not.

## Exercise 00
|**link**|[ex00](ex00)|
|----|----|
- ***`The first thing you need to do is install Python.`***

|Required File|
|----|
|`answer.txt`, `requirements.txt`|

Recently, most of Unix-based system has already installed python. But, they could be the lower/higher version compare to our goal. Using python2.x as legacy is also common.
```shell
$> python -v
$> python3 -v
```
To handle such a problem, we use conda. You can manage python's package and various environments.
> :warning:
> `Project requires you to use 3.7.X version.`
> `You are free to use a different program/utilities to achieve this goal.`

The main things that must be written in answer.txt
- Output a list of installed packages and their versions.
- Show the package metadata of numpy.
- Remove the package numpy.
- (Re)install the package numpy.
- Freeze your python packages and their versions in a requirements.txt file you have to turn-in.

## Exercise 01
|**link**|[ex01](ex01)|
|----|----|

|Required File|
|----|
|`exec.py`|

Make a program that takes a string.
Reverse and swap it's letter case and print them.
- If argument is more that one, merge them.
- If there's no arguments, don't print something.

> :bulb: Examples
> ```shell
> $> python3 exec.py 'Hello World!' | cat -e
> !DLROw OLLEh$
> $> python3 exec.py 'Hello' 'my Friend' | cat -e
> DNEIRf YM OLLEh$
> $> python3 exec.py
> $>
> ```

## Exercise 02
|**link**|[ex02](ex02)|
|----|----|

|Required File|
|----|
|`whois.py`|

Make a program that takes only a number.
Print wheter the number is odd, even, zero, or somethign wrong.
- If argument is more that one or not integer, print error message.
- If there's no arguments, don't print something.

> :bulb: Examples
> ```shell
> $> python3 whois.py 12
> I'm Even.
> $>
> $> python3 whois.py 3
> I'm Odd.
> $>
> $> python3 whois.py
> $>
> $> python3 whois.py 0
> I'm Zero.
> $>
> $> python3 whois.py Hello
> AssertionError: argument is not an integer
> $>
> $> python3 whois.py 12 3
> AssertionError: more than one argument are provided
> $>
> ```