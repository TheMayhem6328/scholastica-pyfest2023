"""
Objective:
===============
Take a string
Reverse it


Examples:
=========
"Cat" should be converted to "taC"
"Fatema" should be converted to "ametaF"
"Zahir" should be converted to "rihaZ"


Note:
=======================================
Now, using slice notation, this could
be done with a simple one-liner:

```
your_string[::-1]
```

But that's not how they want us to do it - they
want us to use a while loop to do it

Ok sure - that's doable too
"""

# Initialize a string to mess around with
my_string = "Fatema Jahan Akhter"

# Store the length of the string seperately
my_size = len(my_string) # Evaluates to (4' 11")? :P

# Initialize a blank string to store reversed string in
reversed_string = ""

# Initiate a loop which does not stop
# as long as `my_size` is greater than 0
#
# Honestly, it's been a while since I've used a while loop :D
while my_size > 0:
    # Know that we are starting backwards,
    # and eventually are making our way
    # to the first character to the string,
    # one character at a time
    #
    # Like let's say, "Whirl"
    # We first take the last character ('l' in this case)
    # and add it to a `reversed_string`
    # then we do the same for the previous character
    # (in this case, 'r')
    #
    # So on and so forth, till we ultimately read it in
    # the sequence 'l', 'r', 'i', 'h', and 'W'
    
    # Decrement `my_size`
    # Could also be written as `my_size = my_size - 1`
    my_size -= 1
    
    # Retrieve the character at index `my_size`
    char = my_string[my_size]
    
    # Add that to `reversed_string`
    reversed_string += char

# After the loop is done, we should have a new string
# with the reversed version of the original
#
# Output it because why not
print(reversed_string)
