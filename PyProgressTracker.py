from graphics import *
import sys

# Variable to ask selection of choice. (Continue or move to Histogram.)
selection1 = 0

progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
global progress_outcome_list

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# validate inputs
def validation():
    global pass_credits
    global defer_credits
    global fail_credits
    
    while True:
        # -------------------------------------
        # Prompt if it's not an integer.
        try:
            pass_credits = int(input("Enter your total PASS credits: "))

        except ValueError:
            print("Integer required")
            continue

        # Pass credit - Out of Range indication
        if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range.")
            continue
        else:
            pass
        # -------------------------------------
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
        # -------------------------------------
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
        # -------------------------------------

        # Total incorrect indication
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect")
            pass
        else:
            return pass_credits, defer_credits, fail_credits

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Prompt the progression outcome
def prompt_credits(pass_credits, defer_credits, fail_credits):
    global credit_result

    if pass_credits == 120:
        credit_result = "Progress"
        global progress_count
        progress_count += 1
        print(credit_result)
        print("---------------------------------")


    elif (pass_credits) >= 100:
        credit_result = "Progress (module trailer)"
        global trailer_count
        trailer_count += 1
        print(credit_result)
        print("---------------------------------")
        

    elif (fail_credits) >= 80:
        credit_result = "Exclude"
        global excluded_count
        excluded_count += 1
        print(credit_result)
        print("---------------------------------")

    else:
        credit_result = "Do not Progress – module retriever"
        global retriever_count
        retriever_count += 1
        print(credit_result)
        print("---------------------------------")

    return progress_count, trailer_count, retriever_count, excluded_count, credit_result

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Store the progressions
progress_outcomes_list = []
def store_progress():
    global progress_list   
    temp_progress_list = [credit_result, pass_credits, defer_credits, fail_credits]
    
    progress_outcomes_list.append(temp_progress_list)

    # Only use in histogram
    credit_list = [progress_count, trailer_count, retriever_count, excluded_count]
    return progress_count, trailer_count, retriever_count, excluded_count, progress_outcomes_list

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Display Histogram
def histogram_graph(progress_count, trailer_count, retriever_count, excluded_count, height_scale = 25):
    # Create a GraphWin window
    win = GraphWin("Histogram", 715, 550)

    # Title of the histogram
    title = Text(Point(170, 30), "Histogram Results")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)

    # Total credits
    total_credits = progress_count + trailer_count + retriever_count + excluded_count

    # Percentage of each credits
    progress_percentage = (progress_count / total_credits) * 100
    trailer_percentage = (trailer_count / total_credits) * 100
    retriever_percentage = (retriever_count / total_credits) * 100
    excluded_percentage = (excluded_count / total_credits) * 100

    # Rectangles for each credits
    progress_rect = Rectangle(Point(100, 440), Point(220, 440 - progress_count * height_scale))
    progress_rect.setFill("green")
    progress_rect.draw(win)

    trailer_rect = Rectangle(Point(230, 440), Point(350, 440 - trailer_count * height_scale))
    trailer_rect.setFill("light green")
    trailer_rect.draw(win)

    retriever_rect = Rectangle(Point(360, 440), Point(480, 440 - retriever_count * height_scale))
    retriever_rect.setFill("orange")
    retriever_rect.draw(win)

    excluded_rect = Rectangle(Point(490, 440), Point(610, 440 - excluded_count * height_scale))
    excluded_rect.setFill("red")
    excluded_rect.draw(win)

    # Labels at the bottom of each bar
    progress_label = Text(Point(160, 460), "Progress")
    progress_label.setSize(15)
    progress_label.setStyle("normal")
    progress_label.draw(win)

    trailer_label = Text(Point(290, 460), "Trailer")
    trailer_label.setSize(15)
    trailer_label.setStyle("normal")
    trailer_label.draw(win)

    retriever_label = Text(Point(420, 460), "Retriever")
    retriever_label.setSize(15)
    retriever_label.setStyle("normal")
    retriever_label.draw(win)

    excluded_label = Text(Point(550, 460), "Excluded")
    excluded_label.setSize(15)
    excluded_label.setStyle("normal")
    excluded_label.draw(win)

    # Value labels on the top of each bar
    progress_count_label = Text(Point(160, 440 - progress_count * height_scale - 15), f"{progress_count}")
    progress_count_label.setSize(15)
    progress_count_label.setStyle("normal")
    progress_count_label.draw(win)

    trailer_count_label = Text(Point(290, 440 - trailer_count * height_scale - 15), f"{trailer_count}")
    trailer_count_label.setSize(15)
    trailer_count_label.setStyle("normal")
    trailer_count_label.draw(win)

    retriever_count_label = Text(Point(420, 440 - retriever_count * height_scale - 15), f"{retriever_count}")
    retriever_count_label.setSize(15)
    retriever_count_label.setStyle("normal")
    retriever_count_label.draw(win)

    excluded_count_label = Text(Point(550, 440 - excluded_count * height_scale - 15), f"{excluded_count}")
    excluded_count_label.setSize(15)
    excluded_count_label.setStyle("normal")
    excluded_count_label.draw(win)

    # bottom x axis
    start_point = Point(70,441)
    end_point = Point(640, 441)
    line = Line(start_point, end_point)
    line.setOutline("black")
    line.setWidth(2)
    line.draw(win)
    

    # Outcomes of the histogram
    title = Text(Point(190, 510), "{} outcomes in total".format(total_credits))
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)
    
    # Display the Histogram window
    win.getMouse()
    win.close()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Selection Choice
def selection_choice():
    global selection1
    while True:
        selection1 = input(
            """Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: """
        )

        if selection1 == "y":
            validation()
            prompt_credits(pass_credits, defer_credits, fail_credits)
            store_progress()

        elif selection1 == "q":
            progression_report()
            histogram_graph(progress_count, trailer_count, retriever_count, excluded_count)
            break

        else:
            print("Incorrect selection")
            continue

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Progression Report
def progression_report():
    print()
    print("Part 2:")
    for outcome in progress_outcomes_list:
        print("---------------------------------")
        print(f"{outcome[0]} - {outcome[1]}, {outcome[2]}, {outcome[3]}")
    print("---------------------------------")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Start code
# Part 1
print("***STUDENT PROGRESSION SYSTEM*** Developed by Dilruk")
print()
print("Select the mode you want to continue")
print("1. Student Mode")
print("2. Staff Member Mode")
print("---------------------------------")
verify = input("Type 1 or 2: ").lower()
while True:
    # For 1 Student
    if verify == "1":
        print("---------------------------------")
        print("Student Mode") 
        while True:  
            validation()
            prompt_credits(pass_credits, defer_credits, fail_credits)
            store_progress()

            selection2 = input("Do you want to Exit (y) or Try Again (n)? (y/n) ").lower()

            if selection2 == "y":
                print("In Student Mode, No histogram available for multiple progression.")
                print("Have a Nice Day...")
                sys.exit(0)
            elif selection2 == "n":
                continue
            else:
                print("Incorrect selection")
                continue

    # For a Staff Member
    elif verify == "2":
        print("---------------------------------")
        print("Staff Member Mode")  
        print("Part 1:")

        while True:
            validation()
            prompt_credits(pass_credits, defer_credits, fail_credits)
            store_progress()
            selection_choice()
            selection2 = input("Do you want to Exit (y) or Try Again (n)? (y/n) ").lower()
            if selection2 == "y":
                print("Have a Nice Day...")
                sys.exit(0)
            elif selection2 == "n":
                continue
            else:
                print("Incorrect selection")
                continue

    else:
        print("Incorrect selection. Try again")
        continue