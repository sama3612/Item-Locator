# Item-Locator
ETAbot Team questionnaire item locator

# Design Choices
As soon as I read the problem statement, the first thing that crossed my mind was a Hashtable. Since the ETAbot team is seeking backend developers fluent in python, I decided that a python dictionary is the data structure of choice. Hash functions are very powerful and optimized to handle storing information that is in the format of key-value pairs. In our case, the item is the key and the location is the value of that key. There can be no duplicate keys, which makes sense because you cannot place the same item in two different places. There are allowed to be duplicate values however because a fridge, for instance, can store multiple different items.

I was initially planning on writing unit tests using the python library unittest, however, they were fairly straightforward so I wrote out some test cases as I applied TDD and wrote the code to ensure the test cases were passing. Additional functionality such as getting rid of items can also be added if necessary.
