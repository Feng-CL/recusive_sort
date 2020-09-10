import random,time

def rsort(li=[]):

    if len(li)==0 or len(li)==1:
        return li
    else:
        pivot=random.choice(li)
        li.remove(pivot)
        left=0
        right=-1
        length=len(li)
        if  length==1:
            #the length of this li now become 1 
            if pivot <= li[right]:
                li.insert(0,pivot)
            else:
                li.append(pivot)
            return li
        else:
            #the length of this li now become 2 or longer 
            #move left pointer to the correct position until...
            while left<length+right:
                while li[left]<=pivot:
                    if left+1<length: 
                        left+=1
                    else:
                        break
                #move right pointer to the correct position until before out of index !!
                while li[right]>pivot:
                    if right-1>=-length:
                        if length+right>left: #right_pointer still is at the right of left 
                            right-=1
                        else:
                            break # |right| ==left now 
                    else:
                        break # right has reach the end of index.lowerbound
                swap(li,left,right)

            else:
                #insert pivot into the right position

                #test out where should we put pivot into and 'centralize' the variable: left
                if li[left]>pivot:
                    li.insert(left,pivot)
                else:
                    li.insert(left+1,pivot) 
                    left=left+1
                # left, pivot, right(left+2)
                # predict what will happen here
                length=len(li)     
                return rsort(li[0:left])+[pivot]+rsort(li[left+1:length])

def swap(li,i,j):
    if i!=j:
        li[i],li[j]=li[j],li[i]



        
#test 
origin_list=[]
random.seed(time.time())
for i in range(100):
    origin_list.append(random.randrange(-100,100))

for i in range(20):
    input_list=origin_list.copy()
    random.shuffle(input_list)
    output_list=rsort(origin_list)
    time.sleep(1)
    print("第{2:}次shuffle: \nbefore sort: {0:}\nafter sorting:{1:}".format(input_list,output_list,i))