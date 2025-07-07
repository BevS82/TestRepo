def find_pattern_positions(text, pattern):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(str(i))
    return ' '.join(positions)

# Example usage
text = "AAACATAGGATCAAC"
pattern = "AA"
result = find_pattern_positions(text, pattern)
print(result)