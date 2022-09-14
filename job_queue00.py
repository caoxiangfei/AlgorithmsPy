# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def shiftdown(H, j):
    minindex = j
    size = len(H)
    l = 2*j + 1
    r = 2*j + 2

    if l<size and H[l] < H[minindex]:
        minindex = l
    if r<size and H[r] < H[minindex]:
        minindex = r
    if j != minindex:
        H[j], H[minindex] = H[minindex], H[j]
        return shiftdown(H, minindex)
    else:
        return H

def shiftdown1(H, j):
    minindex = j
    size = len(H)
    l = 2*j + 1
    r = 2*j + 2

    if l<size and H[l][1] < H[minindex][1]:
        minindex = l
    if r<size and H[r][1] < H[minindex][1]:
        minindex = r
    if j != minindex:
        H[j], H[minindex] = H[minindex], H[j]
        return shiftdown1(H, minindex)
    else:
        return H

def shiftup(H, i):
    parent = (i-1) // 2

    while i > 0 and H[parent] > H[i]:
        H[i], H[parent] = H[parent], H[i]
        i = parent
        return shiftup(H, i)
    return H


def shiftup1(H, i):
    parent = (i-1) // 2

    while i > 0 and H[parent][1] > H[i][1]:
        H[i], H[parent] = H[parent], H[i]
        i = parent
        return shiftup1(H, i)
    return H

def insert(H, p):
    H.append(p)
    i = len(H)-1
    shiftup(H, i)
    return H

def insert1(H, p):
    H.append(p)
    i = len(H)-1
    shiftup1(H, i)
    return H

def extractmin(H):
    if len(H) == 0:
        return "Herror"
    result = H[0]
    H[0] = H[-1]
    H.pop()
    shiftdown(H, 0)
    return result

def extractmin1(H, result):
    result.append(H[0])
    H[0] = H[-1]
    #print(result)
    H.pop()
    #print(H)
    shiftdown1(H, 0)
    if len(H) > 0 and H[0][1] == result[-1][1]:
        return extractmin1(H, result)

    return result
def build_heap1(data):
    n = len(data)
    a = list(range(0, n // 2))
    a.reverse()
    for i in a:
        shiftdown1(data, i)
    return data

def changepriority(H, i, p):









def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    H = list(range(n_workers ))
    glock = 0
    assign = []
    jobtimer = []
    lj = len(jobs)
    if lj <= n_workers :
        for i in range(lj):
            assign.append([H[i], 0])
    else:
        for i in range(n_workers ):
            assign.append([extractmin(H), 0])
            jobtimer.append([assign[i][0], jobs[i]])
        j = n_workers
        #print(jobtimer)
        while j < lj:
            #glock += 1
            po = []
            build_heap1(jobtimer)
            extractmin1(jobtimer, po)
            if len(jobtimer)>0:
                for a in jobtimer:
                    a[1] = a[1] - po[0][1]
            glock = glock + po[0][1]
            for b in po:
                insert(H, b[0])
                #print(b)
            for b in po:
                if j<lj:
                    assign.append([extractmin(H), glock])
                    insert1(jobtimer, [assign[-1][0], jobs[j]])
                    j = j+1



                #for a in range(len(jobtimer)):
                #jobtimer[a][1] = jobtimer[a][1] - 1
                #if jobtimer[a][1] == 0:
                    #po.append(a)
                    #insert(H, jobtimer[a][0])
            #print(H)
            #print(po)
            #if len(po) > 0:
                #for b in po:
                    #if j < lj:
                        #assign.append([extractmin(H), glock])
                        #jobtimer[b] = [assign[j][0], jobs[j]]
                        #j = j + 1








    return assign



    #result = []
    #next_free_time = [0] * n_workers
    #for job in jobs:
        #next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        #result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        #next_free_time[next_worker] += job

    #return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for i, j in assigned_jobs:
        print(i, j)


if __name__ == "__main__":
    main()

#H = [[0, 1], [1, 1], [2, 1], [3, 3], [4, 2]]
#j = 0
#result = []
#print(extractmin1(H, result))
#print(H)
#n = 4
#jobs = []
#for i in range(20):
    #jobs.append(1)
    #jobs.append(2)
    #jobs.append(3)
    #jobs.append(4)
#print(jobs)
#for i, j in assign_jobs(n, jobs):
    #print(i, j)

#n = 10
#st = '124860658 388437511 753484620 349021732 311346104 235543106 665655446 28787989 706718118 409836312 217716719 757274700 609723717 880970735 972393187 246159983 318988174 209495228 854708169 945600937 773832664 587887000 531713892 734781348 603087775 148283412 195634719 968633747 697254794 304163856 554172907 197744495 261204530 641309055 773073192 463418708 59676768 16042361 210106931 901997880 220470855 647104348 163515452 27308711 836338869 505101921 397086591 126041010 704685424 48832532 944295743 840261083 407178084 723373230 242749954 62738878 445028313 734727516 370425459 607137327 541789278 281002380 548695538 651178045 638430458 981678371 648753077 417312222 446493640 201544143 293197772 298610124 31821879 46071794 509690783 183827382 867731980 524516363 376504571 748818121 36366377 404131214 128632009 535716196 470711551 19833703 516847878 422344417 453049973 58419678 175133498 967886806 49897195 188342011 272087192 798530288 210486166 836411405 909200386 561566778'
#jobs = st.split()
#jobs1 = []
#for job in jobs:
    #jobs1.append(int(job))


#for i, j in assign_jobs(n, jobs1):
    #print(i, j)

