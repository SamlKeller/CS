'''
accumulator = ""
text = ""
while text != "quit":
print("So far, this is everything you've typed:", accumulator)
text = input("Please type anything ('quit' will exit): ")
accumulator = accumulator + text

This idea is important for this assignment; make sure this makes sense to you as well!

Coding Task
Your goal is to write a function c_sub that takes a single argument – a string that has already been encoded with a
substitution cipher you don’t know.
Inside c_sub, you should have a while loop that repeats until the user types 'quit', just as shown above. Inside the while
loop, your code must do these things in this order:
• Print the encoded text, in its current state.
• Print each letter in the alphabet, and how many times it occurs in the text (either upper or lowercase).
• Print a reminder for the user that the most common letters in English are usually ETAOINSHRDLU, in that order.
• Ask the user to either swap two letters or quit, using the following prompt in an input statement:
Type a pair of letters to swap, for example AB would swap A and B, or type 'quit':
• If the user typed a two-letter input, then your code should swap each occurrence of each of those two letters
with the other. For instance, the user might notice that the letter X appears most often in the ciphertext, and
type 'XE'. Then, every single X in the ciphertext should become an E; every single E should become an X. Also,
every x should become an e and every e should become an x. And next time through the loop, it should report
that E is now the most common letter in the ciphertext.
• If the user typed 'quit', then the while statement at the top of the loop should notice and stop the loop.
Just like the Better Substitution Ciphers assignment, this function should be able to handle strings that contain
lowercase letters, spaces, and grammatical markers; it isn’t ever trying to change *every* character in the string, only
the *specific* letters the user chooses. As such, the non-letter characters will be ignored. This will make it easier to
decode some of the messages later in the assignment, where I’ve left the spaces in!

'''

def c_sub (string):
    alph = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    accumulator = ""
    text = ""
    while text != "quit":
        print(string)
        for x in range(0, 26):
            print(alph[x], ":", (string.count(alph[x]) + string.count(alph.lower()[x])))
        text = input("Type two letters to switch in lowercase ab format or type 'quit' to exit: ")
        accumulator = accumulator + text
        if (len(text) == 2 and text.isalpha()):
            string = string.replace(text[1], '^`^`')
            string = string.replace(text[0], text[1])
            string = string.replace('^`^`', text[0])

            string = string.replace(text[1].upper(), '^`^`')
            string = string.replace(text[0].upper(), text[1].upper())
            string = string.replace('^`^`', text[0].upper())
        else:
            print("Invalid input, restarting iteration")
            continue


strInput = '''Rqvrkq hadmj zvlrbhqwo ndkk jqqr haql pwvl lsjdmg ldohsjqo. Haqf'wq nwvmg. Ndha zvlrbhqwo
fvb lsjq ldohsjqo psohqw. -Sxsl Vouvwmq, dmiqmhqw vp haq pdwoh rvwhsukq zvlrbhqw'''


print(c_sub(strInput))

'''ETAOINSHRDLU'''


'''
1. Computers are incredibly fast, accurate, and stupid. Human beings are incredibly slow,
inaccurate, and brilliant. Together they are powerful beyond imagination. -Albert
Einstein, physicist

2. Humans are allergic to change. They love to say, 'We've always done it this way.' I try to
fight that. That's why I have a clock on my wall that runs counterclockwise. -Grace
Hobber, combuter scientist and military admiral

3. Before software should be reusable, it should be usable. -Ralph Johnson, computer
scientist

4. Code breaks and then it falls apart, and it often takes many, many tries until that magical
moment when what you're trying to build comes to life. -Reshma Sauvani, founder of Girls
Who Code

5. People think computers will keep them from making mistakes. They're wrong. With computers
you make mistakes faster. -Adam Osborne, inventer of the first portable computer
'''