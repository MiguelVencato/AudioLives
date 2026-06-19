def calculate_priority(message: str) -> int:
    text = message.strip()

    if not text:
        return 0

    word_count = len(text.split())
    if word_count <= 1:
        return 0
    if word_count <= 3:
        return 2
    if word_count <= 6:
        return 5
    if word_count <= 12:
        return 8
    return 10


def should_read(message: str) -> bool:
    return calculate_priority(message) >= 2