import time

def bruteForce(goal: str):
    myStr = ""
    for c in range(len(goal)):
        for a in range(32, 127):
            print(myStr + chr(a))
            time.sleep(0.05)
            if chr(a) == goal[c]:
                myStr = myStr + chr(a)
                break

# bruteForce("Hello World!")

bruteForce("I am Iron Man!")