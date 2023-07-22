# for testing enter your full filename with ".txt"
test_file = "test0.txt"

# Task 1a
def insert_in_sorted(x, sorted_list: list) -> list:
    '''
    Inserts a value into a sorted list
    
    :param x: value to insert into a sorted list
    :type x: int, float
    :param sorted_list: sorted list of int/float values
    :param sorted_list: list 
    :returns: sorted list with the inserted value 
    :rtype: list of int/float
    '''
    if not sorted_list: # empty list
        sorted_list.append(x)
        return sorted_list
    
    length = len(sorted_list)
    for i in range(len(sorted_list)):
        # if last index is reached, 
        # and x is greater than last item in the list
        # then append it to the end of the list
        if i == length-1 and x >= sorted_list[-1]:
            sorted_list.append(x)
            break
        # if x is less than item at index i
        # then insert x to this index
        if x < sorted_list[i]:
            sorted_list.insert(i,x)
            break
        # if x is greater than current item at index i
        # continue looping through
        elif x > sorted_list[i]:
            continue
    return sorted_list

# Task 1b
def insertion_sort(my_list: list) -> list:
    '''
    Sorts a given list
    
    :param my_list: unsorted list of int/float
    :type my_list: list
    :returns: sorted list of int/float
    :rtype: list of int/float
    '''
    length = len(my_list)
    result = []
    # for each item in the unsorted list
    # call the sort function and return a sorted list
    for i in range(length): 
        result = insert_in_sorted(my_list[i], result)
    return result

# Task 2
def matrix_to_sparse(sparse_list: list) -> dict:
    '''
    Populates a list of coordinates from a list to dictionary
    
    :param sparse_list: sparse list of coordinates
    :type sparse_list: list
    :returns: dictionary represents the sparse list
    :rtype: dict of {tuple:int}
    '''
    result: dict= dict()
    y_coord=0
    for list in sparse_list:
        x_coord = 0
        for item in list:
            if item != 0: # ignore 0 values
                result[(y_coord,x_coord)] = item
            x_coord += 1
        y_coord += 1
    return result

# Task 3
def annotate(filename: str):
    '''
    Annotates a text file
    
    :param filename: name of the text file to annotate
    :type filename: str
    '''
    try:
        with open(filename, 'r') as file_to_read:
            lines = file_to_read.readlines()
    except FileNotFoundError:
        print("Invalid filename!")
        return 0

    
    with open(f'annotated_{filename}', 'w') as file_to_write:
        line_length = 0
        for count,line in enumerate(lines): # gives an index to the line
            line_length += len(line.split())
            to_write = f'{line.strip()} {count} {line_length}\n'
            file_to_write.write(to_write)
                
# Task 4a
def find_matching_lines(file_handle, string_to_match: str) -> list:
    '''
    Matches a given string inside a text file
    
    :param file_handle: text file to look into
    :type file_handle: file handle
    :param string_to_match: string to be matched
    :type string_to_match: string
    :returns: list of tuples that includes line number and text
    :rtype: list of tuples 
    '''
    string_to_match = str(string_to_match)
    result = []
    lines = file_handle.readlines()
    for count,line in enumerate(lines):
        if string_to_match in line:
            result.append((count,line))
    return result

# Task 4b
def find_lines():
    '''
    Matches a string inside a text file and prints out line number and text
    '''
    filename = str(input("Hello, which file do you want to search in? ")).strip()
    filename = filename if filename.endswith(".txt") else filename+".txt"
    try:
        file_handle = get_filehandle(filename,'r')
    except FileNotFoundError:
        print("Invalid filename!")
        return 0
    else:
        print(f'Ok, searching in "{filename}"')
    
    string_to_match = str(input("\nWhat do you want to search for? ")).strip()
    print(f'The result after searching for "{string_to_match}" is:\n')
    
    result = find_matching_lines(file_handle, string_to_match)
    for item in result:
        print(f'Line {item[0]}: {item[1]}',end="")
    file_handle.close()

# Task 5a
def save_rows(file_handle) -> dict:
    '''
    Saves lines of a text file into a dictionary
    
    :param file_handle: text file to save 
    :type file_handle: file handle
    :returns: dictionary of {line_no:line_text}
    :rtype: dict
    '''
    result = {}
    lines = file_handle.readlines()
    for count,line in enumerate(lines):
        result[count]=line.strip()
    return result


# Task 5b
def lookup(dictionary: dict,row: int,column: int) -> str:
    '''
    Gets the letter at some position inside a dictionary
    
    :param dictionary: dictionary to look up into
    :type dictionary: dict
    :param row: row that represents a key in the dictionary
    :type row: int
    :param column: column that represents the index of the letter in the string "key's value"
    :type column: int
    :returns: letter at the given row, column
    :rtype: string
    '''
    coords = tuple((row, column)) 
    try:
        text = dictionary[coords[0]]
        result = text[coords[1]] if text[coords[1]].strip() != "" else "Space"
    except:
        result = "Warning: Out of bounds, try again!"
    return result
    

def main():
    '''
    Small program that asks the user for a text file, row and column 
    and prints the letter at the given position
    '''
    running: bool = True
    while running:
        filename: str = get_filename()
        on: bool  = False
        try:
            filehandle = get_filehandle(filename, 'r')
        except FileNotFoundError:
            print("Invalid filename")
        else: 
            saved_dict: dict = save_rows(filehandle)
            on = True
        
        while on:
            print('\nAt any point type "exit" to quit.\n')
            
            row = input("provide row: ")
            if row.lower() == 'exit':
                filehandle.close()
                running = False
                break

            column = input("provide column: ")
            if column.lower() == 'exit':
                filehandle.close()
                running = False
                break
            try:
                letter = lookup(saved_dict,int(row),int(column))
            except ValueError:
                print("\nInvalid value!")
            else:
                print(f'\n{letter}')

# Extras
def get_filename() -> str:
    '''
    Asks the user for a filename
    
    :returns: filename given by the user
    :rtype: string
    '''
    filename = str(
        input("\nPlease enter the filename (must be in same directory) : "))
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

def get_filehandle(filename: str,access: str):
    '''
    Gets the file handle for the given filename
    
    :param filename: name of the file
    :type filename: string
    :param access: type of access to the file
    :type access: string
    :returns: file handle
    :rtype: file
    '''
    try:
        f = open(filename, access)
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        return f

# Tests ?
def run_tests():
    '''
    Runs all tests from the lab examples
    '''
    # Task 1a
    print("\n[Task 1a]")
    print("insert_in_sorted(2,[]) : ", insert_in_sorted(2, []))
    print(" insert_in_sorted(5,[0,1,3,4]) : ",insert_in_sorted(5, [0, 1, 3, 4]))
    print(" insert_in_sorted(2,[0,1,2,3,4]) : ",
          insert_in_sorted(2, [0, 1, 2, 3, 4]))
    print(" insert_in_sorted(2,[2,2]) : ", insert_in_sorted(2, [2, 2]))
   
    # Task 1b
    print("\n[Task 1b]")
    print("insertion_sort([12,4,3,-1]) : ", insertion_sort([12, 4, 3, -1]))
    print("insertion_sort([]) : ", insertion_sort([]))
    
    # Task 2
    print("\n[Task 2]")
    print("matrix_to_sparse([[1,0,0,2],[0,8,0,0],[0,0,0,5]]) : ", matrix_to_sparse([[1, 0, 0, 2], [0, 8, 0, 0], [0, 0, 0, 5]]))
    print("matrix_to_sparse([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) : ", matrix_to_sparse([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    print("matrix_to_sparse([[0,0],[0,0],[0,0],[0,10]]) : ",
          matrix_to_sparse([[0, 0], [0, 0], [0, 0], [0, 10]]))
    
    # Task 3
    print("\n[Task 3]")
    annotate(test_file)
    print(f"Annotated file: annotated_{test_file}")
    
    # Task 4a
    print("\n[Task 4a]")
    hinfile = open(test_file)
    print(f"find_matching_lines({test_file}, 'the mob') : ",
          find_matching_lines(hinfile, 'the mob'))
    hinfile.close()
    
    hinfile = open(test_file)
    print(f"find_matching_lines({test_file}, 'the') : ",
          find_matching_lines(hinfile, 'the'))
    hinfile.close()

    with open(test_file) as h:
        print(f"find_matching_lines({test_file}, 'sommar') : ", find_matching_lines(
            h, 'sommar'))
    
    # Task 4b
    print("\n[Task 4b]")
    find_lines()
    
    # Task 5a
    print("\n[Task 5a]")
    with open(test_file) as hinfile:
        print("save_rows(hinfile) : ",save_rows(hinfile))

    # Task 5b
    print("\n[Task 5b]")
    with open(test_file) as hinfile2:
        d = save_rows(hinfile2)
        print("lookup(d, 0, 0) : ", lookup(d, 0, 0))
        print("lookup(d, 2, 9) : ", lookup(d, 2, 9))
        print("lookup(d, 2, 10) : ", lookup(d, 2, 10))
        
if __name__ == '__main__':
    run_test: bool = True if(str(input("Do you want to run the tests ? (y/n) ")).lower()=="y") else False
    if run_test:
        run_tests()
    else:
        main()
    print("\nQuitting..")
