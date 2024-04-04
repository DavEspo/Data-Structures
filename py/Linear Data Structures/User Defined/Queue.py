# Importing deques
from collections import deque
# Function to find the max value(s) in the deque
def FindMaxDeque(Queue):
    # Shows the initial main queue
    print("Main Queue:", Queue)
    # Makes a max queue
    MaxQueue = deque()
    # Establishes the max element and adds it to the max queue
    # Starts 2 counter variables
    MaxElem = Queue.pop()
    MaxQueue.appendleft(MaxElem)
    count = 0
    length = 0
    # Finds length of the queue
    for i in Queue:
        length += 1
    # Test case for 1 item in the queue
    if length == 1:
        return print("Since there is only 1 element, final Max Queue is", Queue)
    # Loop that finds the max elements
    for i in range(length):
        # Sets current element and prints the queues every iteration
        count += 1
        print("Queue:",Queue)
        print("Max Queue:",MaxQueue)
        curr = Queue.pop()
        # Puts the current element of the main queue from 
        if curr < MaxElem:
            MaxQueue.appendleft(curr)
        # This executes if the current element in the main queue is greater than the max element from the max queue
        else:
            MaxElem = MaxQueue.popleft()
            # Puts the current element of the max queue and of the main queue to the max queue
            if curr < MaxElem:
                MaxQueue.appendleft(MaxElem)
                MaxQueue.appendleft(curr)
            # This adds the current element of the main queue
            else:
                MaxQueue.appendleft(curr)
        # Makes the maximum element the current element in the main queue
        MaxElem = curr
    # Prints the main queue and max queue for every iteration
    print("Queue:",Queue)
    print("Max Queue:",MaxQueue)
    # Returns the final max queue
    return print("Final Max Queue:", MaxQueue)
# Makes a main queue
MainQueue = deque()
# Places elements to the Main Queue
MainQueue.appendleft(1)
MainQueue.appendleft(4)
MainQueue.appendleft(2)
MainQueue.appendleft(3)
# Calls the function to find the maximums in the queue
FindMaxDeque(MainQueue)
