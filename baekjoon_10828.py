
class stack_gener():
    my_stack = []
    def __init__(self) -> None:
        pass
    
    def push(self, val):
        self.my_stack.append(val)
    
    def pop(self):
        if self.my_stack:
            pop = self.top()
            self.my_stack = self.my_stack[:-1]
            return pop
        else: return -1
    
    def size(self):
        return len(self.my_stack)
    
    def empty(self):
        return 0 if self.my_stack else 1

    def top(self):
        return self.my_stack[-1]

my_stack_gener = stack_gener()

N = int(input())
for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push": my_stack_gener.push(cmd[1])
    elif cmd[0] == "pop": print(my_stack_gener.pop())
    elif cmd[0] == "size": print(my_stack_gener.size())
    elif cmd[0] == "empty": print(my_stack_gener.empty())
    elif cmd[0] == "top": print(my_stack_gener.top())