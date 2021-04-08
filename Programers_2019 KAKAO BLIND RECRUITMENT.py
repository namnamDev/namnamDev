import sys 
sys.setrecursionlimit(10 ** 6)

        

def solution(nodeinfo):
    board = [[0]*20 for _ in range(20)]
    cnt = 1
    top_h = 0
    bot_h = 1001
    top_w = 0
    bot_w = 1001 
    for i in nodeinfo:
        board[i[1]][i[0]] = cnt
        if top_h<i[1]:
            top_h = i[1]
        if bot_h>i[1]:
            bot_h=i[1]   
        if top_w < i[0]:
            top_w = i[0]
        if bot_w>i[0]:
            bot_w=i[0]
        cnt+=1
    real_board=[]
    width = top_w - bot_w
    cnt_zero = 0
    height = top_h-bot_h
    for i in range(top_h,bot_h-1,-1):
        if board[i][bot_w:top_w+1].count(0) != width+1:
            real_board+=[board[i][bot_w:top_w+1]]
        else:
            print('here')
            cnt_zero+=1
    print()

    for i in real_board:
        print(i)

    height -= cnt_zero
    tree = [[0]*4 for _ in range(len(nodeinfo)+1)]
    
    def do_tree(mother,start,end):
        # print(real_board[mother[0]][mother[1]])
        print(mother,start,end)
        level = mother[0]
        if level == height - 1:
            return
        else:
            children = []
            for gg in range(start,end):
                if real_board[level+1][gg]:
                    children += [[real_board[level+1][gg],level+1,gg]]
            print(children)
            for i in children:
                if i[2] < mother[1]:
                    do_tree([i[1],i[2]],start,mother[1])
                else:
                    do_tree([i[1],i[2]],mother[1],end)
    
    do_tree([0,7],0,13)
    # for i in range(height - 1):
    #     for g in range(width):
    #         if real_board[i][g]:
    #             mother = real_board[i][g]#엄마도느
    #             tree[i][0] = mother
    #             child_line = real_board[i+1]#자식노드의 라인
    #             children = []
                # for gg in range(width):
                #     if real_board[i+1][gg]:
                #         children += [[real_board[i+1][gg],i+1,gg]]
                # print(children)
                    # if gg < g:
                    #     tree[i][1] = gg # left
                    # elif gg>g:
                    #     tree[i][2]==gg #right
                        
    answer=[[]]
    return answer