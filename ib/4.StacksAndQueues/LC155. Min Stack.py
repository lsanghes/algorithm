'''
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
# calculate new min_val and push (x, min_val) to stack
# alternatively use two separate stacks for xs and min_vals
class MinStack(object):
    # @param x, an integer
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append((x, min(self.stack[-1][1], x)))
        else:
            self.stack.append((x, x))

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1][0] if self.stack else -1

    # @return an integer
    def getMin(self):
        return self.stack[-1][1] if self.stack else -1

# test
minStack = MinStack();
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.
