def create_queue(items):
    queue = []

    for item in items:
        enqueue(queue, item)

    return queue


def enqueue(queue, item):
    queue.append(item)


def dequeue(queue):
    if is_queue_empty(queue):
        return None

    return queue.pop(0)


def is_queue_empty(queue):
    return len(queue) == 0


def queue_size(queue):
    return len(queue)
