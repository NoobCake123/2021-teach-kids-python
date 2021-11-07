
def sort(sus):
    for i in range(0, len(sus)):
        smallest = i
        for index in range(i+1, len(sus)):
            if sus[index] < sus[smallest]:
                smallest = index
        a = sus[i]
        sus[i] = sus[smallest]
        sus[smallest] = a


    return sus

sus = [0,6,3]
susy = sort(sus)
print(susy)