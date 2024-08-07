Simple Discord Bot
This Discord bot uses user interactions and previous conversations to provide responses based on past interactions.

How to Use the Code:
Copy the files and load them into an interpreter.
Run the program from the main file.
Ask the bot something in chat.
If the question has been asked before, the bot will provide the stored answer. If not, the bot will inform you that it doesn't know the answer and will ask what the answer should be for future reference.
If you prefer not to provide an answer, you can skip the question.

How the Code Works:
The MAIN file primarily handles the messages being sent and received.
The CHECK file is used to compare the user's message with the data already present in the JSON file.
The JSON file contains the previous questions and their corresponding answers.
