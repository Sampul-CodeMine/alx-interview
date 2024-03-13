# 0x01. Lockboxes

## Must Know

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

### Concepts Needed:

- #### Lists and List Manipulation:

> - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
> - <a href="https://docs.python.org/3/tutorial/datastructures.html" target="_blank">Python Lists (Python Official Documentation)</a>

- #### Graph Theory Basics:

> - Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
> - <a href="https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs" target="_blank">Graph Theory (Khan Academy)</a>

- #### Algorithmic Complexity:

> - Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
> - <a href="https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/" target="_blank">Big O Notation (GeeksforGeeks)</a>

- #### Recursion:

> - Some solutions might require a recursive approach to traverse through the boxes and keys.
> - <a href="https://realpython.com/python-recursion/" target="_blank">Recursion in Python (Real Python)</a>

- #### Queue and Stack:

> - Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
> - <a href="https://www.geeksforgeeks.org/queue-in-python/" target="_blank">Python Queue and Stack (GeeksforGeeks)</a>

- #### Set Operations:

> - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
> - <a href="https://docs.python.org/3/tutorial/datastructures.html#sets" target="_blank">Python Sets (Python Official Documentation)</a>

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

- #### Additional Resources

> - <a href="https://www.youtube.com/watch?v=V8DGdPkBBxg" target="_blank">Mock Technical Interview</a>

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3 (version 3.4.3)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the `PEP 8 style (version 1.7.x)`
- All your files must be executable

## Tasks

### 0. Lockboxes (mandatory)

> You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
>
> Write a method that determines if all the boxes can be opened.
> 
> Prototype: `def canUnlockAll(boxes)`
> - boxes is a list of lists
> - A key with the same number as a box opens that box
> - You can assume all keys will be positive integers
> - There can be keys that do not have boxes
> - The first box boxes[0] is unlocked
> - Return True if all boxes can be opened, else return False
>
> ```bash
> carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
> #!/usr/bin/python3
> 
> canUnlockAll = __import__('0-lockboxes').canUnlockAll
> 
> boxes = [[1], [2], [3], [4], []]
> print(canUnlockAll(boxes))
> 
> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
> print(canUnlockAll(boxes))
> 
> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
> print(canUnlockAll(boxes))
> 
> carrie@ubuntu:~/0x01-lockboxes$
> carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
> True
> True
> False
> carrie@ubuntu:~/0x01-lockboxes$
> ```

---

Dukeson Ehigboria