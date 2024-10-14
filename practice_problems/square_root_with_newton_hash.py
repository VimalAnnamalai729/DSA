"""
Find a guess
use this Newton hash formula to solve
new_est = current_est  - f(current_est) /f'(current_est)

f(current_est) =  current_est * current_est - N
f'(current_est) = 2*current_est
repeat until you get the result.
"""


# def square_root(x):
#     current_est = 1
#     while (x - current_est*current_est) > 0.001:
#         new_est = current_est - (current_est * current_est - x) / (2 * current_est)
#         current_est = new_est
#     return current_est
#     # return x*x

def square_root(n, l):
    current_est = n

    while True:
        new_est = current_est - (current_est * current_est - n) / (2 * current_est)
        if abs(new_est - current_est) < l:
            break
        current_est = new_est
    return new_est

    # return new_est


n = 327
l = 0.00001
print(square_root(n, l))


# def testpass():
#     inputs = [2, 4, 10]
#     expected_out = [1.414, 2.0, 3.162]  # Expected square roots
#     threshold = 0.001
#
#     for i in range(len(inputs)):
#         result = square_root(inputs[i])
#         print(f"Computed square root of {inputs[i]}: {result}")
#         if abs(square_root(inputs[i]) - expected_out[i]) > threshold:
#             print(f"Test failed for input {inputs[i]}")
#         else:
#             print(f"Test passed for input {inputs[i]}")


# Run the test cases
# testpass()
