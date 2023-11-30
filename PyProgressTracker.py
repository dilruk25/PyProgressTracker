from graphics import *

print("""***STUDENT PROGRESSION SYSTEM*** Developed by Dilruk""")

progress_count = trailer_count = retriever_count = excluded_count = 0

def range_check(credit):
    if credit not in range(0,130,20):
        return True
    return False

# validate inputs
def validation():
    global pass_credit
    global defer_credit
    global fail_credit

    # Prompt if it's not an integer.
    while True:
        try:
            pass_credit = int(input("Enter your total PASS credits: "))
        except ValueError:
            print("Integer required")
            continue

        # Pass credit - Out of Range indication
        if range_check(pass_credit):
            print("Out of range.")
            continue

        try:
            defer_credit = int(input("Enter your total DEFER credits: "))
        except ValueError:
            print("Integer required")
            continue

        # Defer credit - Out of Range indication
        if range_check(defer_credit):
            print("Out of range.")
            continue

        try:
            fail_credit = int(input("Enter your total FAIL credits: "))
        except:
            print("Integer required")
            continue

        # Fail credit - Out of Range indication
        if range_check(fail_credit):
            print("Out of range.")
            continue
        
        # Total incorrect
        if (pass_credit+defer_credit+fail_credit) != 120:
            print("Total Incorrect!")
            continue

def prompt_credits(pass_credit, defer_credit, fail_credit):
    if pass_credit == 120:
        print("Progress")
        global progress_count
        progress_count += 1
        return
        
    if (pass_credit + defer_credit) > 100:
        credit_result = "Progress (module trailer)"
        global trailer_count
        trailer_count += 1
        print(credit_result)
        print("---------------------------------")
        return trailer_count

    elif (pass_credit + defer_credit) > 60:
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
    return histogram_graph(credit_list)

# didn't touch anything inside this function
def histogram_graph(credit_list, height_scale = 25):
    win = GraphWin("Histogram", 715, 550)

    title = Text(Point(170, 30), "Histogram Results")
    title.setSize(20),title.setStyle("bold")
    title.draw(win)

    total_credits = sum(credit_list)
    # Rectangles for each credits
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
    line.draw(win)

    title = Text(Point(190, 510), "{} outcomes in total".format(total_credits))
    title.setSize(20),title.setStyle("bold")
    title.draw(win)
    
    win.getMouse()
    win.close()

# Start code
while True:
    validation()
    prompt_credits(pass_credit, defer_credit, fail_credit)
    store_progress()
    selection = input("Would you like to continue (y/n): ").strip()
    if selection.lower() == "n":
        break


# Hey, dilruk
# Quick TIP
# Try to reduce creating functions, and global things.
# If this changes okay with you accept the request. it will change automatically