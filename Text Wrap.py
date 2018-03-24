def wrap(string, max_width):
    result=[]
    counterBegin=0
    CounterEnd=max_width
    flag=0;
    while counterBegin<len(string):
        string=string[0:CounterEnd]+"\n"+string[CounterEnd:]
        counterBegin = counterBegin + max_width
        if CounterEnd+max_width < len(string):
            CounterEnd = CounterEnd+max_width+1
        else:
            CounterEnd=len(string)
    return string