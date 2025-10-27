def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def count_words(path_to_file):
    return len(get_book_text(path_to_file).split())

def count_symbols(path_to_file):
    counts = {}
    for ch in get_book_text(path_to_file).lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def sort_characters(counts):
    items = []
    for ch, n in counts.items():
        if ch.isalpha():
            items.append({"char": ch, "num": n})
    items.sort(reverse=True, key=sort_on)
    return items
