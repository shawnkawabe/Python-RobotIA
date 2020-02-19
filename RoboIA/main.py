from tkinter import *
from tkinter import simpledialog

posx = 0
posy = 0
bpx = 0
bpy = 0 
mcampo = []
mcampo_m = []

def getpos():
    global posx 
    global posy
    pos  = simpledialog.askstring("Posição robô X,Y","Digite a posição da coordenada X,Y")
    posit =  pos.split(',')
    posx = int(posit[0])
    posy = int(posit[1])
    print(posit)
    
    

def mt():
    global mcampo
    global mcampo_m
    for i in range (6):
        mcampo.append([0] * 9 )
        
    for i in range (6):
        mcampo_m.append(['○'] * 9 )

def main():
    global mcampo
    global mcampo_m
    global posx
    global posy 
    
    posattx = 0
    posatty = 0
    print(posx,posy)
    mcampo_m[posx][posy] = '◙'
    ballposit()
    
def ballposit():
    global bpx 
    global bpy
    global mcampo_m
    cond = False
    while True:
        po  = simpledialog.askstring("Posição bola X,Y","Digite a posição da coordenada X,Y")
        posi =  po.split(',')
        bpx = int(posi[0])
        bpy = int(posi[1])
        
        if mcampo_m[bpx][bpy] == '◙':
            print()
        elif mcampo_m[bpx][bpy] == '○':
            break
        
    print(posi,bpx,bpy)
    mcampo_m[bpx][bpy]='•'
    print(posi)
    att()
    roboia()
    
def att():
    global mcampo_m
    
    lbl_prp['text'] = ""
    txt = ""
    for i in range(len(mcampo_m)):
        for x in range(len(mcampo_m[i])):
            txt = txt + mcampo_m[i][x] + " "
        txt = txt +"\n"
    
    lbl_prp['text']=txt
    print(mcampo_m)
    mainwd.after(1500,att)


def roboia():
    global mcampo_m 
    global posx
    global posy
    cd =  0
    conditx = 0
    condity  = 0
    for x in range(len(mcampo_m)):
        for y in range(len(mcampo_m[x])):
            if mcampo_m[x][y] == '•':
                conditx =  x 
                condity = y   
    print(conditx,condity)
    if conditx<=5  and condity<=9:
        if posx < conditx:  
            if posy<condity:
                if posx < conditx:
                    mcampo_m[posx][posy]='○' 
                    posx += 1
                    cd = 2500
                     
        elif posy < (condity-1):
            if posy < condity:
                mcampo_m[posx][posy]='○'
                posy=posy + 1     
                cd = 2500
        elif posx > conditx:  
            if posy<condity:
                if posx > conditx:
                    mcampo_m[posx][posy]='○' 
                    posx -= 1
                    cd = 2,
        else:   
            cd = 4500
            print("chegou") 
            
                  
    print(posx,posy)
    mcampo_m[posx][posy]= "◙"
    mainwd.after(cd,roboia)
    
     
mainwd = Tk()
mainwd.title('RoboIA')    
mainwd.geometry('1000x800')

lbl_prp = Label(mainwd)
lbl_prp.config(font=('Consolas',64), fg='#50FA7B',bg='#282A36')
mainwd.config(bg='#282A36')
lbl_prp.place(x=100,y=100)
getpos()
mt()
main()
mainwd.mainloop()

    
    
#while True: 
#    main()  
#if __name__ == "__main__":
#    main()