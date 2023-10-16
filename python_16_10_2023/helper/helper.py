def getArrayTime(up_time):
    resultArr=[]
    temp=""
    for char in up_time:
        if char.upper() != char.lower():
            resultArr.append(int(temp))
            temp=""
        else:
            temp+=char
    return resultArr