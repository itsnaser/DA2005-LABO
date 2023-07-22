# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, -0.01, 17
# 2, 0.9, 0.82, 23
#
# Pretend this is taken from two (or more) different experiments:
# batch 1 and batch 2.
import matplotlib.pyplot as plt
import matplotlib.patches as plt_patches

# colors used to distinguish between batches
colors = {1: "blue", 2: "green",
          3: "red", 4: "purple", 5: "brown", 6: "pink"}


def get_filename() -> str:
    '''Get the filename of the data file

    :returns: data filename
    :rtype: str
    '''
    filename: str = str(input('Which csv file should be analyzed? '))
    return filename


def get_file_data(filename: str) -> list:
    '''Read and return data from file

    :param filename: filename of the data file
    :type filename: str

    :returns: list of file lines
    :rtype: list
    '''
    if ".csv" not in filename:
        filename = filename+".csv"
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    # if user gives an invalid text filename e.g. "video.mp4",
    # then print an error message and return empty list
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []


def populate_data(data_list: list, data_dict: dict) -> dict:
    '''Populate batches' data from a data file into a dictionary

    :param data_list: list of batches with their data
    :type data_list: list
    :param data_dict: dictionary to populate data into
    :type data_dict: dict
    :returns: populated dictionary
    :rtype: dict
    '''
    for line in data_list:
        four_vals: list = line.split(',')
        batch: int = four_vals[0]

        if batch not in data_dict:
            data_dict[batch] = []
        try:
            # Collect data from an experiment
            data_dict[batch] += [(float(four_vals[1]),
                                  float(four_vals[2]), float(four_vals[3]))]
        # if there is an invalid values in the line e.g. "string",
        # then just ignore it and print an error message
        except ValueError:
            print("Warning: wrong input format for entry: ", *four_vals)
        except IndexError:
            print(f"Warning: list index out of range: ",*four_vals)
    return data_dict


def is_empty(list_param: list) -> bool:
    return False if (list_param) else True


def get_average_data(batch: int, sample: list):
    '''Gets average value from batch's data

    :param batch: batch number in the data file
    :type batch: int

    :param sample: list of batch data samples
    :type sample: list of float

    :return: average value
    :rtype: float or None
    '''
    if not is_empty(sample):
        count = 0
        sum = 0
        for (x, y, val) in sample:
            if x**2 + y**2 <= 1:
                sum += val
                count += 1
        try:
            average = sum/count
        # if "x" and "y" are greater than "1"
        # in all lines, then "n" will be zero
        # if "count" is zero then print an error message and return None
        except ZeroDivisionError:
            print("Warning: division by zero:",*sample)
            return None
        else:
            return average


def output_data(data_dict: dict):
    '''Prints out the batch data in the given dictionary

    :param data_dict: dictionary containing batch number and its average value
    :type data_dict: dict
    '''
    print("Batch \t Average")
    for batch, sample in sorted(data_dict.items()):
        average = get_average_data(batch, sample)
        # average becomes None if the calculations
        # were divided by zero (the value of "n")
        # if average is not None then it should be float, so print it
        if average is not None:
            print(f"{batch} \t {average}")


def convert_to_float(data: list) -> list:
    '''
    Converts list of string to float

    :param data: list contains values to convert
    :type data: list
    :return: list of the converted values
    :rtype: list
    '''
    result: list = []
    for item in data:
        try:
            result.append([float(num.strip()) for num in item])
        except ValueError:
            print("Warning: value error:", *item)
            pass
    return result


def plot_data(data: dict, f: str):
    '''
    Plot list of batches by its x and y values,
    and saves the plot as a pdf file

    :param data: dict contains batches as keys and values as list of tuples to plot
    :type data: dict str:list of tuples. e.g. '1':[(1,4,3,23),(2,3,3,19),(4,2,2,51)]
    :param f: name of the generated pdf file
    :type f: str
    '''
    # make sure to includ .pdf in the filename
    f = f if f.endswith(".pdf") else f"{f}.pdf"
    # float_data: list = convert_to_float(data)

    # creating plot figure
    figure, ax = plt.subplots(figsize=(10, 10))

    for i in range(1,len(data)+1):
        if data.get(str(i)) is not None:
            # plotting x,y of each batch and choosing different colors
            ax.scatter([value[0] for value in data[str(i)]], [value[1] for value in data[str(i)]],color=colors[i])
        
    # annotate (the value of index 3 in the batch list)
    # to the same x,y position
    for batch, list_of_values in data.items():
        for values in list_of_values:
            ax.annotate(values[2],(values[0]+0.01,values[1]+0.01),fontsize=7,color=colors[int(batch)])
            
    # circle of radius 1 and middle point at 0
    circle = plt_patches.Circle((0, 0), 1, color="blue", fill=False)
    ax.set_aspect('equal', adjustable='datalim')
    ax.add_patch(circle)
    
    # save plot figure with the given filename "f"
    plt.savefig(f"{f}", format="pdf", bbox_inches="tight")
    print(f"A plot of the data can be found as {f} in the same directory")
    plt.show()


def main():
    '''
    This is the main body of the program.
    Here executes the objective of the program in sequence
    '''
    # 4.4.1 A: Better structure
    # 4.5 B: Error handling
    # 4.5.1 C: Sorted batch-data
    filename: str = get_filename()

    data_lines: list = get_file_data(filename)

    populate_data(data_lines, data)

    output_data(data)
    
    # 4.5.2 D: Plotting the values
    pdf_file: str = input("What do you want to name the generated pdf file? ")
    # create list of lists by splitting items by ","
    plot_data(data, pdf_file)


# Start the main program: This is idiomatic python
if __name__ == '__main__':
    data: dict = dict()
    main()

# The idea with this idiom is that if this code is loaded as a module,
# then the __name__ variable (internal to Python) is not __main__ and
# the body of the program is not executed. Consider what would happen
# if the main function was not in a function: an import statement (for
# example "import o4") would load the functions and then executed
# "filename = input(...)" and that is probably not what you want. The
# idiom is simply an easy way of ensuring that some code is only
# executed when run as an actual program.
#
# Try it out by importing this file into another project!
