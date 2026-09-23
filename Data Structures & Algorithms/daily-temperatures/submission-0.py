class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        results = [0] * len(temperatures) # every day needs a slot, and the default should mean "never warmer"
        stack = []      # holds days that are still waiting for a warmer day

        for i in range(len(temperatures)):
            
            # while there's something waiting AND today is warmer than it:
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]: 
                # pop the waiting day
                prev = stack.pop()
                # figure out its answer and put it in the right spot in results
                results[prev] = i - prev   # the popped day's slot = days between it and today

            stack.append(i) 

            # add today to the stack (what exactly do you push?)

        return results
            