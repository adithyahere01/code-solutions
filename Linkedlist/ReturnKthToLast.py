#CTCI
def kth_to_last(li,k):
    runner = current = li.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current
