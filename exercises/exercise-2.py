# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
phrase = input(' Please enter a word or phrase:').lower()
# 2. Print the following message:
while phrase != "quit":
    if phrase != "quit":
        print(f'What you entered is {len(phrase)} characters long')
        phrase = input(' Please enter a word or phrase:').lower()
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

