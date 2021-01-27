# nBASIC: a really, really basic BASIC interpreter

*Not to be confused with [uBASIC](http://dunkels.com/adam/ubasic/). (i guess)*

This BASIC is even more basic then it already is.

I made this as a challenge to myself that didn't know how to code an interpreter the traditional way. Also, this is non-interactable.
## Syntax:
```(N)``` means any number.
```(O)``` means any operations.
```(C)``` means any character.
| Syntax | Description |
| --- | --- |
| ```GOTO(N)``` | go to line ```(N)``` |
| ```IF(O)THEN(N)``` | if ```(O)``` is true, go to line ```(N)``` |
| ```PRINT(O)``` | print ```(O)``` |
| ```INPUT(C)``` | input string |
| ```INT(C)``` | cast variable ```(C)``` to integer |
| ```REM``` | Comment |
| ```(C)=(O)``` | Variable assigment |
## Operation
The operators in nBASIC are addition (+), subtraction (-), multiplication (\*), and division (/).
There is no order of operation, so operations are operated from left to right.

This means ```2+3*5``` equals ```25``` instead of ```17```.
## Variable types
Since the "interpreter" is coded in Python, you don't need to assign a type. Instead, just put the name if the variable:
```
INPUT A
PRINT A
```
## Running the program
To run the program, use this command:
```
$ python3 nbasic.py file.bas
```
