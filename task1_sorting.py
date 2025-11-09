# Task 1: Sort a list of dictionaries by a specific key
# Manual implementation

def sort_dicts_manual(data, key):
    """
    Sorts a list of dictionaries by the specified key using a lambda function.
    """
    return sorted(data, key=lambda x: x[key])

# AI-suggested implementation (example Copilot output)
def sort_dicts_ai(data, key):
    """
    Sorts a list of dictionaries by the specified key using operator.itemgetter.
    More efficient for large datasets.
    """
    from operator import itemgetter
    return sorted(data, key=itemgetter(key))

# Sample data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Testing both functions
print("Manual Sort by age:", sort_dicts_manual(data, "age"))
print("AI Sort by age:", sort_dicts_ai(data, "age"))
