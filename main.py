def min_max(array):
    min_num= array[0]
    max_num = array[0]
    for i in range(1,len(array)):
        if min_num > array[i]:
            min_num = array[i]     
    
   
    for i in range(1,len(array)):
        if max_num< array[i]:
            max_num = array[i]

    return(max_num - min_num) 

def main():
    numbers = [15, 22, 84, 14, 88, 23]
    difference = min_max(numbers)


if __name__ == "__main__":
    main()