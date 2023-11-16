Multi-Class Planned Design Recipe
1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.


To record my experiences I want to keep a regular diary.
To reflect on my experiences want to read my past entries.
On a busy day, I want to select diary entries to read based on how much time I have and my reading speed.
To keep track of tasks, keep a todo list along with my diary
To keep track of my contacts, I want to see a list of all of the mobile phone numbers in all my diary entries


2. Design the Class System
Design the interfaces of each of your classes and how they will work together to achieve the job of the program. You can use diagrams to visualise the relationships between classes.

Consider pulling out the key verbs and nouns in the problem description to help you figure out which classes and methods to have.

Steps 3, 4, and 5 then operate as a cycle.

Nouns:
diary
diary entry
tasks
todo list
contacs
phone number

Verbs:
keep
read
read for time
see list of tasks
see list of phone numbers


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

Encode one of these as a test and move to step 4.

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

Encode one of these as a test and move to step 5.

5. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.