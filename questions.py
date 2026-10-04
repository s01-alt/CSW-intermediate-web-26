# ---- Difficulty tags match the ranks: ------
#   "d" = Entry (D), "a" = Intermediate (A), "s" = Advanced (S)

# marks per correct answer
MARKS = {
    "D": 1, 
    "A": 2, 
    "S": 3
    }   
# 5 questions each -> max score = 5*1 + 5*2 + 5*3 = 30

questions = [
    # ---------- D: Entry (1 mark each) ----------
    {
        "difficulty": "D", 
        "question": "What does print('Hi') do?",
        "options": ["Saves Hi to a file", "Displays Hi on the screen", "Asks the user for input"],
        "answer": "Displays Hi on the screen"
        },

    {
        "difficulty": "D", 
        "question": "Which line correctly stores the number 5 in a variable called x?",
        "options": ["x = 5", "5 = x", "x == 5"],
        "answer": "x = 5"
        },

    {
        "difficulty": "D", 
        "question": "What data type is the value 3.14?",
        "options": ["int", "str", "float"],
        "answer": "float"
        },

    {
        "difficulty": "D", 
        "question": "What does len([4, 8, 15]) return?",
        "options": ["3", "15", "2"],
        "answer": "3"
        },

    {
        "difficulty": "D", 
        "question": "What is the index of the FIRST item in a Python list?",
        "options": ["1", "0", "-1"],
        "answer": "0"
        },

    # ---------- A: Intermediate (2 marks each) ----------
    {
        "difficulty": "A", 
        "question": "What does this print?\nfor i in range(3):\n    print(i)",
        "options": ["1 2 3", "0 1 2 3", "0 1 2"],
        "answer": "0 1 2"
        },

    {
        "difficulty": "A", 
        "question": "In an if / elif / else chain, how many branches run?",
        "options": ["All of them", "Only the first branch whose condition is True", "Only the else branch"],
        "answer": "Only the first branch whose condition is True"
        },

    {
        "difficulty": "A", 
        "question": "What does a function return if it has no return statement?",
        "options": ["None", "0", "An error is raised"],
        "answer": "None"
        },

    {
        "difficulty": "A", 
        "question": "Which of these creates a dictionary?",
        "options": ["[1, 2]", "(1, 2)", "{'a': 1}"],
        "answer": "{'a': 1}"
        },

    {
        "difficulty": "A", 
        "question": "What does 'hello'[1:3] return?",
        "options": ["he", "el", "ell"],
        "answer": "el"
        },

    # ---------- S: Advanced (3 marks each) ----------
    {
        "difficulty": "S", 
        "question": "What does this evaluate to?\n[x * 2 for x in range(4) if x % 2 == 0]",
        "options": ["[0, 2, 4, 6]", "[2, 6]", "[0, 4]"],
        "answer": "[0, 4]"
        },

    {
        "difficulty": "S", 
        "question": "Inside a class method, what does 'self' refer to?",
        "options": ["The specific object calling the method", "The class itself", "The file the class is in"],
        "answer": "The specific object calling the method"
        },

    {
        "difficulty": "S", 
        "question": "Given def f(a, b=2): return a + b, what does f(3) return?",
        "options": ["An error, because b is missing", "3", "5"],
        "answer": "5"
        },

    {
        "difficulty": "S", 
        "question": "What does this print?\nx = 10\ndef f():\n    x = 5\nf()\nprint(x)",
        "options": ["5", "10", "An error"],
        "answer": "10"
        },

    {
        "difficulty": "S", 
        "question": "What does this print?\na = [1, 2]\nb = a\nb.append(3)\nprint(a)",
        "options": ["[1, 2]", "[1, 2, 3]", "An error"],
        "answer": "[1, 2, 3]"
        },
]