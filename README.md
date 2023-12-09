# PyProgressTracker

**Student Progression Tracking System**

PyProgressTracker is a Python application designed for tracking and analyzing student academic progress. The system facilitates input of credits earned in various modules, performs validation checks, and provides insights into the student's academic standing through a visual histogram representation.

## Features

- **Data Input:** Collects information on pass, defer, and fail credits from the user.
- **Validation:** Ensures accurate input by validating entered credit values.
- **Outcome Analysis:** Categorizes the student's academic outcome into progress, trailer, retriever, or excluded.
- **Histogram Visualization:** Presents a graphical representation of academic outcomes through a histogram.
- **User-Friendly Interface:** Prompts users for input and allows for multiple data entries.

## Working process

1. Run the application.
2. Input the total pass, defer, and fail credits as prompted.
3. Receive an immediate categorization of academic outcome.
4. Choose to enter another set of data or view the results.
5. Visualize academic outcomes through the histogram.

## Dependencies

- Python 3.12
- [Graphics Module](#) (Specify any external module or library used)

## Usage Example

```bash
# Run the PyProgressTracker application
python PyProgressTracker.py
```

## Contribution

Contributions are welcome! If you find a bug or have suggestions for improvement, please open an issue or submit a pull request.

The provided code seems to be a student progression system. It collects information about student credits, determines their progression outcome, stores the outcomes, and optionally displays a histogram of the progression results. Here are the instructions on how to use this code:

## How to Use

1. **Initialization:**
   - Execute the script.
   - Choose the mode: Student Mode (1) or Staff Member Mode (2).
   - Enter either 1 or 2 accordingly.

2. **Student Mode (Option 1):**
   - Enter Student Mode if you chose option 1.
   - Input total PASS, DEFER, and FAIL credits. Ensure valid integers.
   - The program determines the progression outcome.
   - Choose to exit (y) or try again (n).
   - If you try again, enter a new set of credits.

3. **Staff Member Mode (Option 2):**
   - Enter Staff Member Mode if you chose option 2.
   - Similar to Student Mode, input total PASS, DEFER, and FAIL credits.
   - The program determines the progression outcome and stores the outcomes.
   - After each student entry, decide to enter another set of data (y), quit and view results (q), or switch the mode (c).
   - If you view results, the program displays a progression report and a histogram of all entered data.

4. **Histogram Display:**
   - In Staff Member Mode, a histogram is displayed.
   - The histogram shows the distribution of progression outcomes.
   - Each bar represents a category (Progress, Trailer, Retriever, Excluded), and the height corresponds to the count of students.
   - The x-axis represents the categories, and the y-axis represents the count of students.

5. **Switching Modes:**
   - At any point in Staff Member Mode (Option 2), press 'c' to switch to Student Mode (Option 1).
   - You will be prompted to enter another set of data or exit as usual.

6. **Exiting the Program:**
   - In both modes, exit by entering 'y' when prompted.
   - Exiting terminates the program with a farewell message.

Note: Ensure that you enter valid integer values when prompted for credits. The program includes input validation to handle incorrect inputs.
