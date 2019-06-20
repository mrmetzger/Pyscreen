# prerequisite import
import pyautogui
import time
import winsound

# Ask for filename and store it as string
print('Enter screenshot name:')
name = input()

# Ask how long to wait and store as int
print('How many seconds do you want to wait?')
wait = int(input())

'''
# Prototype: function that would:
# - ask for inputs
# - collect user inputs for both filename (name) and wait time (wait)
# - save as global variables
# - return global variables outside of the function

def user_input(name, wait):
    print('Enter screenshot name:')
    name = input()
    global_name = name
    print('How many seconds do you want to wait?')
    wait = input()
    global_wait = int(wait)

    return global_name
    return global_wait

user_input(name, wait)
'''

#def confirmation(name, wait):
    
# confirm back to user the input and timer
print(name, 'is confirmed')
print('Please wait', wait, 'seconds. Process finished on the chime')

# Wait a number of seconds 
time.sleep(wait)

# take the screenshot
pic = pyautogui.screenshot()

# save the screenshot to the current directory
# whereever the script was run or 
# C:\username\AppData\Local\Programs\Python\Python36-32
# if run inside IDLE directly
pic.save(name + '.png')

# notify when process has completed
winsound.PlaySound('tada.wav', winsound.SND_FILENAME)
# print('Its done bitches')
pyautogui.alert('This displays some text with an OK button.')



# input that creates directory
# enter directory input and/or just saves to new directory
# and puts file there
# 
