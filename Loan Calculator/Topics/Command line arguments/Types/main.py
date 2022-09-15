#import sys
args = sys.argv
length = len(args)
summary = 0
for i in range(1, length, 1):
    summary += int(args[i])
print(int(summary))
# further code of the script "add_four_numbers.py"
