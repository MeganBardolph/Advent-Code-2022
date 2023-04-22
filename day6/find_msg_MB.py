# For Part 2, change marker_size to 14

marker_size = 4
message_str = ''

with open("input06") as f:
    for line in f:
        for idx, char in enumerate(line):
            long_str    = message_str + char
            message_str = long_str[-marker_size:]

            if len(message_str) >= marker_size:
                if len(set(message_str)) == marker_size:
                    print(message_str)
                    print(idx+1)
                    break