# Python Async Function

## Project Overview
This project focuses on asynchronous programming in Python, specifically utilizing coroutines and tasks to handle concurrent operations efficiently. The tasks involve creating coroutines that perform asynchronous operations, measuring their runtime, and managing multiple coroutines concurrently.

## Introduction
**Asynchronous programming** allows tasks to run concurrently, enabling efficient resource utilization and improving overall performance. **Coroutines**, introduced in Python 3.5, are specialized functions used in asynchronous programming. They allow suspension of execution at specific points, enabling other tasks to run while waiting for I/O operations or other asynchronous tasks to complete. 

**Tasks**, on the other hand, are wrappers around coroutines that enable scheduling and execution within an event loop. They represent units of work that can run concurrently with other tasks.

## Project Timeline
**Schedule for 1st and 2nd second deadline of submission:** Feb 19, 2024 6:00 AM to Feb 23, 2024 6:00 AM

## Project Tasks
### 0. The basics of async
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

**Requirement:** Use the random module.

To accomplish this task, an asynchronous coroutine named wait_random was created. This coroutine takes an integer argument max_delay, with a default value of 10. Within the coroutine, the random module was utilized to generate a random delay between 0 and max_delay seconds (inclusive). Then the delay is waited on to complete before returning the delay value.

### 1. Let's execute multiple coroutines at the same time with async
In this task, it is required to import wait_random from the previous file and define an async routine named wait_n. This routine takes two integer arguments: n and max_delay. Within wait_n, spawn wait_random n times with the specified max_delay, and returns a list of all the delays in ascending order without using sort() due to concurrency.

### 2. Measure the runtime
For this task, it is required to measure the runtime. To achieve this, wait_n was imported into 2-measure_runtime.py. A function measure_time with integers n and max_delay as arguments was created. This function measures the total execution time for wait_n(n, max_delay) and returns total_time / n. The time module was utilized to measure an approximate elapsed time.

### 3. Tasks
In this task, a regular function syntax task_wait_random is required that takes an integer max_delay and returns a asyncio.Task.
wait_random is imported from 0-basic_async_syntax. 

### 4. Tasks
For this task, the code from wait_n is modified into a new function named task_wait_n. This function is nearly identical to wait_n, except it calls task_wait_random.

## Conclusion

Through this project, several key concepts have been learned and applied:
- Understanding of asynchronous programming and its benefits in Python.
- Implementation of coroutines and tasks to perform asynchronous operations.
- Handling concurrency efficiently by executing multiple coroutines concurrently.
- Measuring runtime to evaluate the performance of asynchronous operations.
