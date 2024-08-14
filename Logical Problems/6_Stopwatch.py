'''
@Author: Samadhan Thube
@Date: 2024-08-14
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-14
@Title: Stopwatch program
'''
import time

def stopwatch():
    """
    Description:
        This function waits for the user to press Enter to start and stop the stopwatch.
        It captures the current time at each event and calculates the elapsed time between
        the start and end. The elapsed time is then printed in seconds.
    Parameter:
        None
    Return:
        None
    """

    input("Press Enter to start the stopwatch...")
    start_time = time.time()  

    input("Press Enter to stop the stopwatch...")
    end_time = time.time() 

    elapsed_time = end_time - start_time  
    print(f"Elapsed time: {elapsed_time:.2f} seconds") 


if __name__ == "__main__":
    stopwatch()
