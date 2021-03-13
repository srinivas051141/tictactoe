from Modules import * ;
a='x';
i=[]

while True:
    
    
    print('Its your turn '+ a+'. Move to which place?');
    
    while True:
        
        x = int(input());
        if x not in i:
            if x<=9 and x>=1:
                i.append(x);
                break;
            else:
                print('Input should lie between 0 and 10');
        else:
            print('That place is already filled.');
    ttt.TTT[x]=a;
    
    if (ttt.TTT[7]==ttt.TTT[8]==ttt.TTT[9]!=' ') or (ttt.TTT[4]==ttt.TTT[5]==ttt.TTT[6]!=' ') or (ttt.TTT[1]==ttt.TTT[2]==ttt.TTT[3]!=' ') or (ttt.TTT[1]==ttt.TTT[4]==ttt.TTT[7]!=' ') or (ttt.TTT[2]==ttt.TTT[5]==ttt.TTT[8]!=' ') or (ttt.TTT[3]==ttt.TTT[6]==ttt.TTT[9]!=' ') or (ttt.TTT[7]==ttt.TTT[5]==ttt.TTT[3]!=' ') or (ttt.TTT[1]==ttt.TTT[5]==ttt.TTT[9]!=' ') :
        ttt.TicTacToe();
        print(a+' won');
        print('Game over!');
        break;
    
    elif len(i)==9:
       
        print('Its a Tie!!');
        break;
    
    else :
        
        ttt.TicTacToe();
        
        if a=='o':
            a='x';
        else:
            a='o';  
        