import sys

def main():
    input_file = sys.argv[2]
    output_file = f'{sys.argv[2][:3]}_book.txt'
    
    total_length = 0
    longest_line = ""
    longest_line_num = 0
    num_lines = 0

    lines = {}

    #read it once to get number of lines
    with open(input_file) as my_text:
        num_lines = len(my_text.readlines())
    
    #Open File to read
    with open(input_file) as my_text:

        #Loop through each line
        for line in my_text:
            current_line = line.split("|")       #String first element, line num second. if dict, do key, value as value, key (or something like that to get line num as key)
            
            #for the first line found/or if longest line is empty(will be by default)
            if not longest_line:
                current_line[0] = longest_line
                longest_line_num = int(current_line[1])     #assign the line number to a variable to check if future lines need to replace this one
                print(f'the line number of this line is: {longest_line_num} and {current_line[1]}')

            """
            Compare current line with existing line:
                if current line is greater than or equal to the longest:
                    check if the both lines are equal in length:
                    if true: compare line numbers
                    else: reassign both "longest variables"
                    
            """
            if(len(current_line[0]) >= len(longest_line)):
                if(len(current_line[0]) == len(longest_line)):
                    if(int(current_line[1]) > longest_line_num):
                        longest_line = current_line[0]
                        longest_line_num = int(current_line[1])
                else:
                    longest_line = current_line[0]
                    longest_line_num = int(current_line[1])

            #add the length of the line to total length
            total_length += len(current_line[0])
            lines[int(current_line[1])] = str(current_line[0])

    sorted_lines = dict(sorted(lines.items()))
    with open(output_file, "w") as of:
        of.write(f'{input_file[:3]}\n')
        of.write(f'Longest line ({longest_line_num}): {longest_line}\n')
        of.write(f'Average length: {round(total_length / num_lines)}\n')
        for line in sorted_lines.values():
            of.write(f'{line}\n')

if __name__ == "__main__":
    main()
