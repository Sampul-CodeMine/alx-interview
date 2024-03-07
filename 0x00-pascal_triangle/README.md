# PASCAL's TRIANGLE

## Resources

<a href="https://www.cuemath.com/algebra/pascals-triangle/" target="_blank">What is Pascal’s triangle</a>
<br>
<a href="https://www.youtube.com/watch?reload=9&feature=shared&v=0iMtlus-afo" target="_blank">Pascal’s Triangle - Numberphile</a>
<br>
<a href="https://builtin.com/data-science/python-algorithms" target="_blank">What are Python Algorithms</a>
<br>

## Additional Resources

<a href="https://www.youtube.com/watch?feature=shared&v=1qw5ITr3k9E" target="_blank">Mock Technical Interview</a>

## Must Know

- To successfully complete this project, you should revise the following Python concepts:
- Lists and List Comprehensions:
- Understand how to create, access, modify, and iterate over lists.
- Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.

### Functions

- Know how to define and call functions.
- Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.

### Loops

- Use `for` and `while` loops to iterate through sequences.
- Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.

### Conditional Statements

- Apply `if`, `elif`, and `else` conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).

### Recursion (Optional)

- While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
- Recognize base cases and recursive cases for a function that generates the triangle’s rows.

### Arithmetic Operations

- Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.

### Indexing and Slicing

- Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.

### Memory Management

- Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.

### Error and Exception Handling (Optional)

- Use try-except blocks as needed to handle potential errors, such as invalid input types or values.

### Efficiency and Optimization

- Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
- Evaluate and apply optimizations to improve the performance of the solution.

By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal’s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.

## What is Pascal's Triangle?

<strong>Pascal's Triangle</strong> named after the <em>"French Mathematician - <strong>Blaise Pascal</strong>"</em>, is an arrangement of numbers in a triangular array such that the numbers at the end of each row are 1 and the remaining numbers are the sum of the nearest two numbers in the above row. This concept is used widely in probability, combinatorics, and algebra. Pascal's triangle is used to find the likelihood of the outcome of the toss of a coin, coefficients of binomial expansions in probability, etc.

## Pascal Triangle's Logic

The formula to fill the number in the nth column and mth row of Pascal's triangle we use the Pascals triangle formula. The formula requires the knowledge of the elements in the (n-1)<sup>th</sup> row, and (m-1)<sup>th</sup> and n<sup>th</sup> columns. The elements of the nth row of Pascal's triangle are given by:

<sup>n</sup>C<sub>0</sub>, <sup>n</sup>C<sub>1</sub>, <sup>n</sup>C<sub>2</sub>, ..., <sup>n</sup>C<sub>n</sub>. 

The formula for Pascal's triangle is:

<sup>n</sup>C<sub>m</sub> = <sup>n-1</sup>C<sub>m-1</sub> + <sup>n-1</sup>C<sub>m</sub>

where:

nCm represents the (m+1)th element in the nth row.
n is a non-negative integer, and
0 ≤ m ≤ n.
Let us understand this with an example. If we want to find the 3rd element in the 4th row, this means we want to calculate 4C2. Then according to the formula, we get

4C2 = 4-1C2-1 + 4-1C2

⇒ 4C2 = 3C1 + 3C2

So, this means we need to add the 2nd element in the 3rd row (i.e. 3) with the 3rd element in the 3rd row (i.e. 3.). So our answer will be 4C2 = 3 + 3 = 6

---

Dukeson Ehigboria
