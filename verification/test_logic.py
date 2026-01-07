
import math

def calculate_read_time(content_word_count):
    if content_word_count < 360:
        return "1 min read"
    else:
        mins = content_word_count // 180
        return f"{mins} min read"

# Test cases
tests = [
    (0, "1 min read"),
    (100, "1 min read"),
    (359, "1 min read"),
    (360, "2 min read"),
    (400, "2 min read"),
    (539, "2 min read"),
    (540, "3 min read"),
    (1800, "10 min read")
]

for words, expected in tests:
    result = calculate_read_time(words)
    print(f"Words: {words}, Expected: {expected}, Got: {result}")
    assert result == expected

print("All logic tests passed.")
