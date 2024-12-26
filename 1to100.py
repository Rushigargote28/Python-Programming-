def LargeNo(list):
    max = list[0]       #[0,1,2,3,4]
    for i in list:      #[1,2,3,4,5]
        if i > max:
            max = i
    print("Largest numnber is : ",max)

def SmallNo(list):
    min = list[0]       #[0,1,2,3,4]
    for i in list:      #[1,2,3,4,5]
        if i < min:
            min = i
    print("Smallest numnber is : ",min)


def main():
    Array = [] 

    print("Enter the size of an array")
    size =int(input())

    for i in range(size):
        print("Enter the Number : ",i+1)
        Data = int(input())

        Array.append(Data)

    LargeNo(Array)

    SmallNo(Array)


if __name__ == "__main__":
    main()