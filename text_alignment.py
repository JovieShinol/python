"https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true"


def text_align(n,s):

    w = n+(n-1)

    part_a(n,w,s)
    part_b(n,w,s)
    mid(n,s)
    part_b(n,w,s)
    end_h(n,w,s)




def part_a(n,width,s):

   
    j = 1
    for i in range(1,n+1):
        p_h = s*j
        
        print(p_h.center(width," "))
        width-+1
        j+=2
    
def part_b(n,width,s):

    for i in range(0,n):

        level_b1 = (s*n).center(width," ")
        level_bc_space = ' '*((n*2)+1)
    
        print(level_b1,level_bc_space,s*n)      

def mid(n,s):

    for i in range(0,3):

        level_c = (n*6)              # level_c_width = level_c
        count_c = n*5            # level_c_h_count = count_c
        level_c1 = ((s*count_c).center(level_c," "))
        print(level_c1)

def end_h(n,width,s):
    j = width
    
    for i in range(1,n+1):
        p_h = s*j
        print(' '*((4*n)-1),p_h.center(width," "))
        width-+1
        j-=2




n = 5
s = 'H'
text_align(n,s)





"""
    H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH  
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
                    HHHHHHHHH
                     HHHHHHH
                      HHHHH
                       HHH
                        H

 HHHHH                 HHHHH
  HHHHH                 HHHHH

"""