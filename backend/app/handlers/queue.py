import asyncio
import requests
import time
import os


def fetch(url):
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "request_time": request_time}


async def worker(name, queue, results):
    """ grabs request from queue and adds to to result list"""
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        future_result = loop.run_in_executor(None, fetch, url)

        result = await future_result
        results.append(result)

        queue.task_done()


async def distribute_work(url, requests, concurrency, results):
    queue = asyncio.Queue()

    for _ in range(requests):
        queue.put_nowait(url)

    tasks = [] #create a list to hold our task instances/workers
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at

    for task in tasks:
        task.cancel()

    return total_time


def entrypoint(url, requests, concurrency):
    results = []
    total_time = asyncio.run(distribute_work(url, requests, concurrency, results))
    return (total_time, results)