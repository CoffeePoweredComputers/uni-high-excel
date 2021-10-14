import statistics

def get_sum(num_list):
    '''
    Takes a list of lists and returns a list of the sums 
    of each sublist.
    '''
    return list(map(sum, num_list))

def get_stdev(num_list):
    '''
    Takes a list of lists and returns a list of the stdevs 
    of each sublist.
    '''
    return list(map(statistics.stdev, num_list))

def get_avg(num_list):
    '''
    Takes a list of lists and returns a list of the average 
    of each sublist.
    '''
    return list(map(lambda x : sum(x)/len(x), num_list))


def get_rows(data):
    '''
    Convert a list of csv strings to a list of integers
    '''
    return [list(map(int, y)) for y in map(lambda x : x.split(","), data)]

def get_cols(data):
    '''
    Given a list of strings convert to list of lists
    where each sublist is a list of integers from the 
    columns of the original csv. (e.g., for a csv with
    three columns, you should have three sublist)
    '''
    int_data = [list(map(int, y)) for y in map(lambda x : x.split(","), data)]
    return list(zip(*int_data))

