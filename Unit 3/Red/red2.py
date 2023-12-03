def tNums(num):
    nums = []
    for n in range(num):
        print(n, ":", int( (n*(n+1)) / 2 ))
        nums.append(int( (n*(n+1)) / 2 ))
    return nums

def synth_alg (funct, root):
    result = [funct[0]]
    for x in range(1, len(funct)):
        result.append((result[-1]*root) + funct[x])
    for i in range(len(result)-1):
        if (result[i] == 0):
            continue
        elif (len(funct) - 2 - i == 1):
            result[i] = str(result[i]) + 'x'
        elif (len(funct) - 2 - i < 1):
            continue
        else:
            if (result[i] == 1):
                result[i] = 'x^' + str(len(funct) - 2 - i)
            else:
                result[i] = str(result[i]) + 'x^' + str(len(funct) - 2 - i)
    for elm in result:
        if elm == 0:
            result.remove(elm)
    return " + ".join(str(x) for x in result)