def solution(babbling):
    numSet = set(["0","1","2","3"])
    
    result = 0
    for st in babbling:
        st = st.replace("aya", "0")
        st = st.replace("ye", "1")
        st = st.replace("woo", "2")
        st = st.replace("ma", "3")
        
        before = "@"
        for s in st:
            if (s not in numSet) or s==before :
                break
            before = s
        else:
            result += 1
    return result