def Process_File():
    d=dict()#To store goodie details
    input_file = open('input.txt','r')
    for line in input_file:
        #line=line.rstrip()
        if line != '\n':
            a = line.split(":")
            a[1]=a[1][1:]
            if a[1]!= "":
                if a[1][-1] == "\n":
                    a[1] = a[1][:-1]
                d[a[0]] = int(a[1])
    input_file.close()
    return d

def quicksort(data, left, right):
    if left+1 >= right:
        return
    ai, bi, ci = left, (left+right)//2, right-1
    a, b, c = data[ai], data[bi], data[ci]
    if a < b:
        if c < a:
            pos = ai
        elif c < b:
            pos = ci
        else:
            pos = bi
    else:
        if c < b:
            pos = bi
        elif c < a:
            pos = ci
        else:
            pos = ai
    pivot = data[pos]
    data[pos] = data[right-1]
    tail = left
    for i in range(left, right-1):
        if data[i] < pivot:
            data[tail], data[i] = data[i], data[tail]
            tail += 1
    data[right-1], data[tail] = data[tail], pivot
    quicksort(data, left, tail)
    quicksort(data, tail+1, right)

# mydict = { 'a': 1, 'b': 4, 'c': 9, 'd': 3, 'e': 1 }
# values = [value for key, value in mydict.items()]
# quicksort(values, 0, len(values))
#
# g = dict()
#
# # list out keys and values separately
# key_list = list(mydict.keys())
# val_list = list(mydict.values())
#
# # print key with val 100
# position = 0
# for a in values:
#     position = val_list.index(a)
#     g[key_list[position]] = a
# for k, v in mydict.items():

def Extract_Emplyee_Count(d):
    count=d["Number of employees"]
    del d["Number of employees"]
    return count

def Create_Output(l,data,count,sort_data):
    index=0
    min=sort_data[-1]-sort_data[0]
    for i in range((l-count)+1):
        k=sort_data[i+(count-1)]-sort_data[i]
        if k<min:
            min=k
            index=i

    output_file = open('output.txt', 'w')
    output_file.write("The goodies selected for distribution are:\n")
    output_file.write("\n")
    for i in range(index, index + count):
        for j in data.keys():
            if data[j] == sort_data[i]:
                output_file.write(j + ": ")
                output_file.write(str(data[j]))
                output_file.write("\n")
                break
    output_file.write("\n")
    output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
    output_file.write(str(min))
    output_file.close()

if __name__ == "__main__":
    data=dict()
    data=Process_File()
    count=Extract_Emplyee_Count(data)
    sort_data=sorted(data.values())
    l=len(sort_data)
    Create_Output(l,data,count,sort_data)
