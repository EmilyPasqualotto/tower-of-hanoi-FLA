#torre de hanoi----------------------------------------#
print ('-----t-o-w-e-r--o-f--h-a-n-o-i----')
print (' ')

#pilhas das torres-------------------------------------#
t1=[3,2,1]
t2=[]
t3=[]

#printar as torres-------------------------------------#
def print_torres():
   print ('║════════════════║')
   print (' T1','=',t1,)
   print (' T2','=',t2,)
   print (' T3','=',t3,)
   print ('║════════════════║')
print_torres()

#loop do jogo enquanto nao tem ganhador----------------#
while (t3)!=[3,2,1]:
    print ('')
    inp=input('move: ')
    print ('')
    inp=inp.split('-')
    house1=inp[0]
    house2=inp[1]
        
    if (house1)==('1'):
        a=t1[(len(t1)-1)]
        t1.pop(len(t1)-1)
        if (house2)==('2'):
            t2.append((a))
        elif (house2)==('3'):
            t3.append((a))

    elif (house1)==('2'):
        a=t2[(len(t2)-1)]
        t2.pop(len(t2)-1)
        if (house2)==('1'):
            t1.append((a))
        elif (house2)==('3'):
            t3.append((a))

    elif (house1)==('3'):
        a=t3[(len(t3)-1)]
        t3.pop(len(t3)-1)
        if (house2)==('2'):
            t2.append((a))
        elif (house2)==('1'):
            t1.append((a))
   
    print_torres()
    print('')

#depois de sair do loop, o programa finaliza e mostra--#

print ('▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽')
print ('        U       W I N ')
print ('△△△△△△△△△△△△△△△△')

