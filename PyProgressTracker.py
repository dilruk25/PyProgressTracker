from graphics import *
from myGraph import *

print("""***STUDENT PROGRESSION SYSTEM*** Developed by Dilruk""")
print()

# To ask selection of choice. (Continue or move to Histogram.)
selection1 = 0

progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
global progress_outcome_list
progress_outcome_list = []


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# validate inputs
def validation():
    global pass_credits
    global defer_credits
    global fail_credits

    # -------------------------------------
    # Prompt if it's not an integer.
    while True:
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

<<<<<<< HEAD
        # Total incorrect indication
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits > 120:
            print("Total incorrect")
            pass
        else:
            return pass_credits, defer_credits, fail_credits


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
def prompt_credits(pass_cred, defer_cred, fail_cred):
    global credit_result
    if pass_cred == 120:
        credit_result = "Progress"
=======
def prompt_credits(pass_credit, defer_credit, fail_credit):
    if pass_credit == 120:
        print("Progress")
>>>>>>> SGS
        global progress_count
        progress_count += 1
        print(credit_result)
        print("---------------------------------")


    elif (pass_cred + defer_cred) > 100:
        credit_result = "Progress (module trailer)"
        global trailer_count
        trailer_count += 1
        print(credit_result)
        print("---------------------------------")
        

    elif (pass_cred + defer_cred) > 60:
        credit_result = "Do not Progress – module retriever"
        global retriever_count
        retriever_count += 1
        print(credit_result)
        print("---------------------------------")
        

    else:
        credit_result = "Exclude"
        global excluded_count
        excluded_count += 1
        print(credit_result)
        print("---------------------------------")
    
    return progress_count, trailer_count, retriever_count, excluded_count, credit_result

def store_progress():
    global progress_list   
    progress_list = [credit_result, pass_credits, defer_credits, fail_credits]

    progress_outcome_list.append(progress_list)

    credit_list = [progress_count, trailer_count, retriever_count, excluded_count]
<<<<<<< HEAD
    return progress_count, trailer_count, retriever_count, excluded_count, progress_outcome_list

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
def histogram_graph(
    progress_count, trailer_count, retriever_count, excluded_count, height_scale=25
):
    # Create a GraphWin window
=======
    return histogram_graph(credit_list)

# didn't touch anything inside this function
def histogram_graph(credit_list, height_scale = 25):
>>>>>>> SGS
    win = GraphWin("Histogram", 715, 550)

    title = Text(Point(170, 30), "Histogram Results")
    title.setSize(20),title.setStyle("bold")
    title.draw(win)

    total_credits = sum(credit_list)
    # Rectangles for each credits
<<<<<<< HEAD
    progress_rect = Rectangle(
        Point(70, 440), Point(190, 440 - progress_count * height_scale)
    )
    progress_rect.setFill("green")
    progress_rect.draw(win)

    trailer_rect = Rectangle(
        Point(200, 440), Point(320, 440 - trailer_count * height_scale)
    )
    trailer_rect.setFill("light green")
    trailer_rect.draw(win)

    retriever_rect = Rectangle(
        Point(330, 440), Point(450, 440 - retriever_count * height_scale)
    )
    retriever_rect.setFill("orange")
    retriever_rect.draw(win)

    excluded_rect = Rectangle(
        Point(460, 440), Point(580, 440 - excluded_count * height_scale)
    )
=======
    progress_rect = Rectangle(Point(70, 440), Point(190, 440 - credit_list[0] * height_scale))
    progress_rect.setFill("green")
    progress_rect.draw(win)

    trailer_rect = Rectangle(Point(200, 440), Point(320, 440 - credit_list[1] * height_scale))
    trailer_rect.setFill("light green")
    trailer_rect.draw(win)

    retriever_rect = Rectangle(Point(330, 440), Point(450, 440 - credit_list[2] * height_scale))
    retriever_rect.setFill("orange")
    retriever_rect.draw(win)

    excluded_rect = Rectangle(Point(460, 440), Point(580, 440 - credit_list[3] * height_scale))
>>>>>>> SGS
    excluded_rect.setFill("red")
    excluded_rect.draw(win)

    # Labels at the bottom of each bar
    progress_label = Text(Point(130, 460), "Progress")
    progress_label.setSize(15),progress_label.setStyle("normal")
    progress_label.draw(win)

    trailer_label = Text(Point(260, 460), "Trailer")
    trailer_label.setSize(15),trailer_label.setStyle("normal")
    trailer_label.draw(win)

    retriever_label = Text(Point(390, 460), "Retriever")
    retriever_label.setSize(15),retriever_label.setStyle("normal")
    retriever_label.draw(win)

    excluded_label = Text(Point(520, 460), "Excluded")
    excluded_label.setSize(15),excluded_label.setStyle("normal")
    excluded_label.draw(win)

    # Value labels on the top of each bar
<<<<<<< HEAD
    progress_count_label = Text(
        Point(130, 440 - progress_count * height_scale - 10), f"{progress_count}"
    )
    progress_count_label.setSize(15)
    progress_count_label.setStyle("normal")
    progress_count_label.draw(win)

    trailer_count_label = Text(
        Point(260, 440 - trailer_count * height_scale - 10), f"{trailer_count}"
    )
    trailer_count_label.setSize(15)
    trailer_count_label.setStyle("normal")
    trailer_count_label.draw(win)

    retriever_count_label = Text(
        Point(390, 440 - retriever_count * height_scale - 10), f"{retriever_count}"
    )
    retriever_count_label.setSize(15)
    retriever_count_label.setStyle("normal")
    retriever_count_label.draw(win)

    excluded_count_label = Text(
        Point(520, 440 - excluded_count * height_scale - 10), f"{excluded_count}"
    )
    excluded_count_label.setSize(15)
    excluded_count_label.setStyle("normal")
    excluded_count_label.draw(win)

    # bottom x axis
    start_point = Point(50, 440)
    end_point = Point(600, 440)
    line = Line(start_point, end_point)
    line.setOutline("black")
    line.setWidth(2)
=======
    progress_count_label = Text(Point(130, 440 - credit_list[0] * height_scale - 10), f"{credit_list[0]}")
    progress_count_label.setSize(15),progress_count_label.setStyle("normal")
    progress_count_label.draw(win)

    trailer_count_label = Text(Point(260, 440 - credit_list[1] * height_scale - 10), f"{credit_list[1]}")
    trailer_count_label.setSize(15),trailer_count_label.setStyle("normal")
    trailer_count_label.draw(win)

    retriever_count_label = Text(Point(390, 440 - credit_list[2] * height_scale - 10), f"{credit_list[2]}")
    retriever_count_label.setSize(15),retriever_count_label.setStyle("normal")
    retriever_count_label.draw(win)

    excluded_count_label = Text(Point(520, 440 - credit_list[3] * height_scale - 10), f"{credit_list[3]}")
    excluded_count_label.setSize(15),excluded_count_label.setStyle("normal")
    excluded_count_label.draw(win)

    line = Line(Point(50,440), Point(600,440))
    line.setOutline("black"),line.setWidth(2)
>>>>>>> SGS
    line.draw(win)

    title = Text(Point(190, 510), "{} outcomes in total".format(total_credits))
    title.setSize(20),title.setStyle("bold")
    title.draw(win)
<<<<<<< HEAD

    # Display the Histogram window
    win.getMouse()
    win.close()


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
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
            continue

        else:
            print("Incorrect selection")
            continue

def progression_report():
    print(progress_outcome_list)
    print(credit_result, "-", pass_credits, defer_credits, fail_credits)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
=======
    
    win.getMouse()
    win.close()

>>>>>>> SGS
# Start code
# Part 1

while True:
    print("Part 1:")
    validation()
    prompt_credits(pass_credits, defer_credits, fail_credits)
    store_progress()
    selection_choice()
    