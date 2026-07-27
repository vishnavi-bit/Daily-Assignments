def analyze_text(text, output_format='summary'):
    text = text.strip()

    if text == "":
        return "Empty text"

    words = text.split()
    word_count = len(words)

    clean_words = []
    for word in words:
        clean_words.append(word.strip(".,!?;:"))

    unique_words = set()
    for word in clean_words:
        unique_words.add(word.lower())

    unique_count = len(unique_words)

    total_length = 0
    for word in clean_words:
        total_length += len(word)

    average_length = total_length / word_count

    capitalized_count = 0
    for word in clean_words:
        if word and word[0].isupper():
            capitalized_count += 1

    if output_format == "detailed":
        return f"Total: {word_count} | Unique: {unique_count} | Avg: {average_length:.2f} | Caps: {capitalized_count}"

    return f"Words: {word_count} | Unique: {unique_count} | Avg Len: {average_length:.2f}"