from graphics import *
from myGraph import *

# Create a window
win = GraphWin("Histogram", 400, 300)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Welcome Text
print("Hi, Welcome to 'The Progression Outcome program'.")    
print()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////   
# validation function
def validation():
    global pass_credits
    global defer_credits
    global fail_credits

    while True:
#-------------------------------------
# Prompt if it's not an integer.
            try:
                pass_credits = int(input("Enter your total PASS credits: "))

            except ValueError:
                print("Integer required")
                continue

#Pass credit - Out of Range indication
            if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue
            else:
                pass
#-------------------------------------
# Prompt if it's not an integer.
            try:
                defer_credits = int(input("Enter your total DEFER credits: "))

            except ValueError:
                print("Integer required")
                continue

# Defer credit - Out of Range indication
            if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue
            else:
                pass
#-------------------------------------
# Prompt if it's not an integer.
            try:
                fail_credits = int(input("Enter your total FAIL credits: "))
            except:
                print("Integer required")
                continue

# Fail credit - Out of Range indication
            if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue
            else:
                pass
#-------------------------------------

# Total incorrect indication
            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits > 120:
                print("Total incorrect")
            else:
                return
            
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
def prompt_credits(pass_cred, defer_cred, fail_cred):
    if pass_cred == 120:
        print("Progress")
        print("---------------------------------")
        return

    elif (pass_cred + defer_cred) > 100:
        print('''Progress (module trailer)''')
        print("---------------------------------")
        return
    
    elif (pass_cred + defer_cred) >60:
        print('''Do not Progress – module retriever''')
        print("---------------------------------")
        return
    
    else:
        print("Exclude")
        print("---------------------------------")
        return
    print("Would you like to enter another set of data?")
    print("Enter 'y' for yes or 'q' to quit and view results: ")
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
            
#Run the "validation" function.
# Decide program exit or continue
while True:
        exit_continue = input('''press "y" to continue. press "q" to exit : ''')
        exit_continue = exit_continue.lower()
        
        if exit_continue == "q":
            print("Have a Nice Day...")
            break
        elif exit_continue =="y":
            print("Continuing the program...")
            validation()
            prompt_credits(pass_credits, defer_credits, fail_credits)
        else:
            print("Incorrect Choice. Try again.")
            continue
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
