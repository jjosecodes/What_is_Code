

def birthday_match (students):
    '''
    find pair of sutdents with same birthday 
    Input : tuple of student (name, birthday) tuples
    Output : tuple of student names or None 
    '''

    n = len(studets)
    record = StaticArray(n)
    for k in range(n):
        (name1,bday1) = students[k]
        # return par if bday in record 
        for i in range(k):
            (name2, bday2) = record.get_at(i)
            if bday1 == bday2:
                return (name1, name2)
            record.set_at(k, (name1, bday1))
        return None
    
