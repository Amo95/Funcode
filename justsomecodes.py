number = [1,2,3,4,5,6,7,8,9,10]

def printt(lists):
    for num in range(1,len(number) + 1):
        print("""{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}"""
              .format(num, num * 2, num * 3, num * 4, num * 5, num * 6,
                      num * 7, num * 8, num * 9, num * 10))
              
printt(number)
