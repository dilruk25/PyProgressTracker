def main():
  print("Hello from GitHub Actions!")

if __name__ == '__main__':
  main()

from graphics import *
import sys

# //////////////////////////////////////////  Main Menu  /////////////////////////////////////////////////
def main_menu():
    global verify
    print('''Select the mode you want to continue
          1. Student Mode
          2. Staff Member Mode
          3.. Exit\n''')
    verify = input("Select (1/2/3): ").lower()

# ////////////////////////////////////////////  Exit  ////////////////////////////////////////////////////
def exit():
    print("Have a Nice Day...")
    sys.exit(0)

# ///////////////////////////////////////  validate inputs  //////////////////////////////////////////////
def validation():
    global pass_credits, defer_credits, fail_credits

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

        try:
            defer_credits = int(input("Enter your total DEFER credits: "))

        except ValueError:
            print("Integer required")
            continue

        if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range.")
            continue
        else:
            pass
        # -------------------------------------

        try:
            fail_credits = int(input("Enter your total FAIL credits: "))
        except:
            print("Integer required")
            continue

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

# ///////////////////////////////  Prompt the progression outcome  ///////////////////////////////////////
progress_count, trailer_count, retriever_count, excluded_count = 0,0,0,0

def prompt_credits(pass_credits, defer_credits, fail_credits):
    global credit_result, progress_count, trailer_count, excluded_count, retriever_count

    if pass_credits == 120:
        credit_result = "Progress"
        progress_count += 1
        print(credit_result)

    elif pass_credits == 100:
        credit_result = "Progress (module trailer)"
        trailer_count += 1
        print(credit_result)

    elif fail_credits >= 80:
        credit_result = "Exclude"
        excluded_count += 1
        print(credit_result)

    else:
        credit_result = "Do not Progress – module retriever"
        retriever_count += 1
        print(credit_result)

    print("---------------------------------")
    return progress_count, trailer_count, retriever_count, excluded_count, credit_result

# ///////////////////////////////////  Store the progressions  ///////////////////////////////////////////
progress_outcomes_list = []

def store_progress():
    global progress_list
    temp_progress_list = [credit_result, pass_credits, defer_credits, fail_credits]
    progress_outcomes_list.append(temp_progress_list)

    # Only use in histogram
    credit_list = [progress_count, trailer_count, retriever_count, excluded_count]

    return progress_count, trailer_count, retriever_count, excluded_count, progress_outcomes_list

# //////////////////////////////////////  Display Histogram  /////////////////////////////////////////////
def histogram_graph(progress_count, trailer_count, retriever_count, excluded_count, height_scale=25):

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
    start_point = Point(70, 441)
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

# //////////////////////////////////////  Selection Choice  //////////////////////////////////////////////
def selection_choice():
    global selection1, progress_count, trailer_count, retriever_count, excluded_count
    while True:
        selection1 = input("""Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: """)

        if selection1 == "y":
            print("---------------------------------")
            validation()
            prompt_credits(pass_credits, defer_credits, fail_credits)
            store_progress()

        elif selection1 == "q":
            print("---------------------------------")
            progression_report()
            histogram_graph(progress_count, trailer_count, retriever_count, excluded_count)

            # Reset Histogram & Progress Outcomes list
            progress_count, trailer_count, retriever_count, excluded_count = 0, 0, 0, 0
            progress_outcomes_list = []
            break

        else:
            print("Incorrect selection")
            continue

# /////////////////////////////////////  Progression Report  /////////////////////////////////////////////
def progression_report():
    print("======  Part 2: Displaying All Progress Outcomes  ======")
    for outcome in progress_outcomes_list:
        print("---------------------------------")
        print(f"{outcome[0]} - {outcome[1]}, {outcome[2]}, {outcome[3]}")
    print("---------------------------------")

# /////////////////////////////////////////  Staff Mode  /////////////////////////////////////////////////
def staff_mode():
    print("---------------------------------  Staff Member Mode  ---------------------------------")

    while True:
        validation()
        prompt_credits(pass_credits, defer_credits, fail_credits)
        store_progress()
        selection_choice()
        selection2 = input("Do you want to Try Again (y) or Exit (n)? (y/n) ").lower()
        
        if selection2 == "y":
            print("---------------------------------")
            continue
        elif selection2 == "n":
            print("---------------------------------")
            print("Have a Nice Day...")
            sys.exit(0)
        else:
            print("Incorrect selection")
            continue
# ////////////////////////////////////////  Student Mode  ////////////////////////////////////////////////
def student():
    print("---------------------------------  Student Mode  ---------------------------------\n")
    while True:
        validation()
        prompt_credits(pass_credits, defer_credits, fail_credits)
        store_progress()
        selection2 = input("Do you want to Try Again (y) or Exit (n)? (y/n) ").lower()

        if selection2 == "y":
            print("---------------------------------")
            continue
        elif selection2 == "n":
            print("---------------------------------\nIn Student Mode, No histogram available for multiple progression.")
            exit()
        else:
            print("Incorrect selection")
            continue

# /////////////////////////////////////////  Start code  /////////////////////////////////////////////////
print("---STUDENT PROGRESSION SYSTEM--- Developed by Dilruk\n")

while True:
    main_menu()

    # For 1 Student
    if verify == "1":
        student()

    # For a Staff Member
    elif verify == "2":
        staff_mode()

    # For Exit
    elif verify == "3":
        exit()
    else:
        print("Incorrect selection. Try again\n---------------------------------")
        continue
