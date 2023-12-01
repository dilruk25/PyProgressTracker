PyProgressTracker
Student Progression Tracking System
PyProgressTracker is a Python application designed for tracking and analyzing student academic progress. The system facilitates input of credits earned in various modules, performs validation checks, and provides insights into the student's academic standing through a visual histogram representation.

Features

- Data Input: Collects information on pass, defer, and fail credits from the user.
- Validation: Ensures accurate input by validating entered credit values.
- Outcome Analysis: Categorizes the student's academic outcome into progress, trailer, retriever, or excluded.
- Histogram Visualization: Presents a graphical representation of academic outcomes through a histogram.
- User-Friendly Interface: Prompts users for input and allows for multiple data entries.

How to Use

1. Run the application.
2. Input the total pass, defer, and fail credits as prompted.
3. Receive an immediate categorization of academic outcomes.
4. Choose to enter another set of data or view the results.
5. Visualize academic outcomes through the histogram.

Dependencies

- Python 3.x
- Graphics Module (Specify any external module or library used)
Usage Example

# Run the PyProgressTracker application
python PyProgressTracker.py

Contribution

Contributions are welcome! If you find a bug or have suggestions for improvement, please open an issue or submit a pull request.

How to Use?

1. Initialization:
   - Run the script.
   - It will prompt you to select the mode: Student Mode (1) or Staff Member Mode (2).
   - Enter either 1 or 2 accordingly.

2. Student Mode (Option 1)
   - You will enter the Student Mode if you choose option 1.
   - You will be prompted to enter the total PASS, DEFER, and FAIL credits. Make sure to enter valid integers.
   - Based on the entered credits, the program will determine the progression outcome.
   - After the outcome is displayed, you will be asked if you want to exit (y) or try again (n).
   - If you choose to try again, you can enter a new set of credits.

3. Staff Member Mode (Option 2):
   - You will enter the Staff Member Mode if you choose option 2.
   - Similar to Student Mode, you will enter the total PASS, DEFER, and FAIL credits.
   - The program will determine the progression outcome and store the outcomes.
   - After each student entry, you will be asked if you want to enter another set of data (y) or quit and view results (q).
   - If you choose to view results, it will display a progression report and a histogram of all entered data.

4. Histogram Display:
   - If you choose to view results in Staff Member Mode, a histogram will be displayed.
   - The histogram shows the distribution of progression outcomes.
   - Each bar represents a category (Progress, Trailer, Retriever, Excluded), and the height of the bar corresponds to the count of students in that category.
   - The x-axis represents the categories, and the y-axis represents the count of students.

5. Exiting the Program:
   - In both modes, you can exit by entering ‘y’ when prompted.
   - If you choose to exit, the program will terminate with a farewell message.

Note: Ensure that you enter valid integer values when prompted for credits. The program includes input validation to handle incorrect inputs.

