def Chkodd(No):
    if No % 2 !=0:
        return True
    else:
        return False



def main():
    print("Enter the number to check whether the number is odd : ")
    No=int(input())

    Odd = Chkodd(No)

    if Odd == True:
        print(f"{No} is Odd")
    else:
        print(f"{No} is even")


if __name__ == "__main__":
    main()