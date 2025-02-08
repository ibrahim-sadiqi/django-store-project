def list_group(lst, size: int = 4):
    grouped = []
    for i in range(0, len(lst), size):
        grouped.append(lst[i:i + size])
    return grouped

