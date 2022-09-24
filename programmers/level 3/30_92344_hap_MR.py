def solution(board, skill):
    H = len(board)
    W = len(board[0])
    imosBoard = [[0 for i in range(W+1)] for j in range(H+1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        imosBoard[r1][c1] += degree
        imosBoard[r1][c2+1] -= degree
        imosBoard[r2+1][c1] -= degree
        imosBoard[r2+1][c2+1] += degree
    
    # 위아래휩쓸기
    for j in range(0,W+1):
        for i in range(1,H+1):
            imosBoard[i][j] += imosBoard[i-1][j]
    
    # 왼오른휩쓸기
    for i in range(0,H+1):
        for j in range(1,W+1):
            imosBoard[i][j] += imosBoard[i][j-1]
            
    # board 대입
    for i in range(H):
        for j in range(W):
            board[i][j] += imosBoard[i][j]
        
    # 결과
    result = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] > 0:
                result += 1
    return result