import sys  

# Get the current recursion limit
current_limit = sys.getrecursionlimit()
print(f'Current limit: {current_limit}')  

# Set a new recursion limit to 200
new_limit = 200
sys.setrecursionlimit(new_limit)  

# Get the new recursion limit
changed_current_limit = sys.getrecursionlimit()
print(f'Current limit after change: {changed_current_limit}')  

