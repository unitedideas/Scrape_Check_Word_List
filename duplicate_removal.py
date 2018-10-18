orig_file = 'top_used_words_com_from_2015.txt'
scrubbed_file = 'com_available_top_10000_used_words.txt'

file = open(orig_file, 'r+')
lines = file.readlines()
print(type(lines))
count = 0
with open(scrubbed_file, "w") as scrubbed_file:
    for line in lines:
        if count + 1 == len(lines):
            print('Done')
        else:
            if line not in lines[count + 1]:
                print('adding ' + line)
                scrubbed_file.write(line)
        count += 1
        print(count)
scrubbed_file.close()
file.close()
