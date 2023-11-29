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

        # Total incorrect indication
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits > 120:
            print("Total incorrect")
            pass
        else:
            return


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
def prompt_credits(pass_cred, defer_cred, fail_cred):
    if pass_cred == 120:
        credit_result = "Progress"
        global progress_count
        progress_count += 1
        print(credit_result)
        print("---------------------------------")
        return progress_count

    elif (pass_cred + defer_cred) > 100:
        credit_result = "Progress (module trailer)"
        global trailer_count
        trailer_count += 1
        print(credit_result)
        print("---------------------------------")
        return trailer_count

    elif (pass_cred + defer_cred) > 60:
        credit_result = "Do not Progress – module retriever"
        global retriever_count
        retriever_count += 1
        print(credit_result)
        print("---------------------------------")
        return retriever_count

    else:
        credit_result = "Exclude"
        global excluded_count
        excluded_count += 1
        print(credit_result)
        print("---------------------------------")
        return excluded_count


def store_progress():
    credit_list = [progress_count, trailer_count, retriever_count, excluded_count]
    return progress_count
    return trailer_count
    return retriever_count
    return excluded_count


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
def histogram_graph(progress_count, trailer_count, retriever_count, excluded_count, height_scale = 20):
    # Create a GraphWin window
    win = GraphWin("Histogram", 650, 400)

    # Title of the histogram
    title = Text(Point(125, 20), "Histogram Results")
    title.setSize(14)
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
    progress_rect = Rectangle(Point(50, 250), Point(150, 250 - progress_count * height_scale))
    progress_rect.setFill("light green")
    progress_rect.draw(win)

    trailer_rect = Rectangle(Point(200, 250), Point(300, 250 - trailer_count * height_scale))
    trailer_rect.setFill("dark green")
    trailer_rect.draw(win)

    retriever_rect = Rectangle(Point(350, 250), Point(450, 250 - retriever_count * height_scale))
    retriever_rect.setFill("yellow")
    retriever_rect.draw(win)

    excluded_rect = Rectangle(Point(500, 250), Point(600, 250 - excluded_count * height_scale))
    excluded_rect.setFill("purple")
    excluded_rect.draw(win)

    # Labels at the bottom of each bar
    progress_label = Text(Point(100, 270), "Progress")
    progress_label.draw(win)

    trailer_label = Text(Point(250, 270), "Trailer")
    trailer_label.draw(win)

    retriever_label = Text(Point(400, 270), "Retriever")
    retriever_label.draw(win)

    excluded_label = Text(Point(550, 270), "Excluded")
    excluded_label.draw(win)

    # Value labels on the top of each bar
    progress_count_label = Text(Point(100, 250 - progress_count * height_scale - 10), f"{progress_count}")
    progress_count_label.draw(win)

    trailer_count_label = Text(Point(250, 250 - trailer_count * height_scale - 10), f"{trailer_count}")
    trailer_count_label.draw(win)

    retriever_count_label = Text(Point(400, 250 - retriever_count * height_scale - 10), f"{retriever_count}")
    retriever_count_label.draw(win)

    excluded_count_label = Text(Point(550, 250 - excluded_count * height_scale - 10), f"{excluded_count}")
    excluded_count_label.draw(win)

    # Outcomes of the histogram
    title = Text(Point(125, 320), "{} outcomes in total".format(total_credits))
    title.setSize(14)
    title.setStyle("bold")
    title.draw(win)

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
            print(progress_count)
            print(trailer_count)
            print(retriever_count)
            print(excluded_count)
            histogram_graph(progress_count, trailer_count, retriever_count, excluded_count)
            break

        else:
            print("Incorrect selection")
            continue


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Start code
# Part 1

while True:
    print("---Part 1---")
    validation()
    prompt_credits(pass_credits, defer_credits, fail_credits)
    store_progress()
    selection_choice()
