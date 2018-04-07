for first in "ABCD":
    for second in "ABC":
        if second!=first:
            for third in "ABC":
                if third!=first and third!=second:
                    for fourth in "ABCD":
                        if fourth!=first and fourth!=second and fourth!=third:
                            print(first+second+third+fourth)
                
x = 1,2,3,4
for first in x:
    for second in x:
        if second!=first:
            for third in x:
                if third!=first and third!=second:
                    for fourth in x:
                        if fourth!=first and fourth!=second and fourth!=third:
                            print(first*second+third-fourth)
