import statistics

def get_sum(num_list):
    '''
    Implement the sum function using the total/sum pattern
    '''
    return list(map(sum, num_list))

def get_stdev(num_list):
    '''
    Implement the standard deviation of a list of numbers
    '''
    return list(map(statistics.stdev, num_list))

def get_avg(num_list):
    '''
    Implement
    '''
    return list(map(lambda x : sum(x)/len(x), num_list))


def get_rows(data):
    '''
    Given a list of strings convert to list of lists
    where each sublist is a list of integers
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

