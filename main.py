from Modules import * ;
a='x';
i=[]

while True:
    
    
    print('Its your turn '+ a+'. Move to which place?');
    
    while True:
        
        x = input();
        
	if x.isnumeric():
            
            if int(x) not in i:
                if int(x)<=9 and int(x)>=1:
                    i.append(int(x));
                    break;
                else:
                    print('Input should lie between 0 and 10');
            else:
                print('That place is already filled.');
        else:
            print('Input should be positive integer');



    ttt.TTT[int(x)]=a;
    
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
        