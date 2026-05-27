def sort_records_by_id(records):
    return sorted(records, key=lambda record: record["id"])


def recursive_binary_search_by_id(records, target_id, start=0, end=None):
    if end is None:
        end = len(records) - 1

    if start > end:
        return None

    middle = (start + end) // 2
    middle_record = records[middle]

    if middle_record["id"] == target_id:
        return middle_record

    if target_id < middle_record["id"]:
        return recursive_binary_search_by_id(records, target_id, start, middle - 1)

    return recursive_binary_search_by_id(records, target_id, middle + 1, end)
