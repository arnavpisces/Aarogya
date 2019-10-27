poly=[[77.20454330209701, 28.596685859073208], [77.21039338317165, 28.631319730145332], [77.21186074548743, 28.63543965104233], [77.23451348961252, 28.634191612337467], [77.2550140848653, 28.630922209710928], [77.25472313028025, 28.622428709367533], [77.25970203686364, 28.61005773605071], [77.25510620732918, 28.60192323131927], [77.24475819728806, 28.59191284178785], [77.21336216280793, 28.584050852713638], [77.20454330209701, 28.596685859073208]]
# poly=[[0,0],[0,1],[1,1],[1,0]]

def checkInside(y=28.6255914, x=77.2341954):
    # for val in ultimateFinalCoords:
    num = len(poly)
    i = 0
    j = num - 1
    c = False
    
    for i in range(num):
        if ((poly[i][1] > y) != (poly[j][1] > y)) and \
                (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                                  (poly[j][1] - poly[i][1])):
            c = not c
        j = i
    return c

if __name__=='__main__':
    print(checkInside())