import csv

def readData(path):
    """
    Reads lines from a file and returns them as an array.
    
    Args:
        path: The path to the file from the perspective of main.py.

    Returns:
        An array containing each line from the file.
    """
    content = []
    try:
        match getFileType(path):
            case 'txt':
                file = open(path, "r")
                for line in file:
                    content.append(line.rstrip('\n').split(','))
                file.close()

            case 'csv':
                with open(path, mode='r') as file:
                    reader = csv.reader(file)
                    next(reader) # Skip the header line
                    for row in reader:
                        content.append(row)
    except FileNotFoundError:
        print(f"Error: File not found: {path}")        
    return content

def getFileType(path):
    """
    Returns the file extension.
    """
    if path.endswith('.txt'):
        return 'txt'
    if path.endswith('.csv'):
        return 'csv'