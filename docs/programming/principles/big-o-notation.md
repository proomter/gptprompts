
# BIG O analysis

You have to conduct Big O notation analysis of code:
Identify the Operations: The first step in analyzing an algorithm's time complexity is to identify the operations that the algorithm performs. Operations can be anything from arithmetic operations, comparisons, data assignments, or function calls.
*Count the Operations: Once you've identified the operations, the next step is to count how many times each operation is performed. This count should be expressed in terms of 'n', where 'n' is the size of the input to the algorithm.
Find the Dominant Term: As 'n' becomes very large, the term with the highest power of 'n' will dominate the running time of the algorithm. This term is used to express the algorithm's Big O notation.
The final step is to express the algorithm's time complexity in Big O notation. The goal is to describe how the algorithm's running time grows as the sizeof the input increases. Common time complexities include O(1) for constant time, O(n) for linear time, O(n^2) for quadratic time, O(log n) for logarithmic time, and so forth.For example, consider an algorithm that has a loop that runs 'n' times, and inside that loop, there is another loop that also runs 'n' times. Each iteration of the inner loop performs a constant time operation. In this case, the algorithm would perform the operation n * n = n^2 times, so we would say this algorithm has a time complexity of O(n^2).
When analyzing space complexity with Big O notation, the steps are similar, but instead of counting operations, we are interested in how much space (memory) is used relative to the size of the input.

