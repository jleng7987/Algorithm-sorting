elevations = {"Huilongguan": 5, "Chaoyang Park": 25, "National Stadium": 15, "Olympic Park": 20, "Tsinghua University": 10}
paths = {("Huilongguan", "Chaoyang Park"): 10,
         ("Huilongguan", "National Stadium"): 8,
         ("Huilongguan", "Olympic Park"): 15,
         ("Chaoyang Park", "Olympic Park"): 12,
         ("National Stadium", "Tsinghua University"): 10,
         ("Olympic Park", "Tsinghua University"): 5,
         ("Olympic Park", "Huilongguan"): 17,
         ("Tsinghua University", "Huilongguan"): 10
}
duiying = {"Huilongguan": 0, "Chaoyang Park": 1, "National Stadium": 2, "Olympic Park": 3, "Tsinghua University": 4}
list1 = []
df= [ #[0,1,2,3,4],
     [0, 10, 8, 15, 0],
     [0, 0, 0, 12, 0],
     [0, 0, 0, 0, 10],
     [17, 0, 0, 0, 5],
     [10, 0, 0, 0, 0],
     ]
def minpaths(df, i , sum, count1):
    if i==0 and sum !=0:
        count1 = max(count1, sum)
        list1.append(count1)
        return count1
    for j in range(0,len(df[0])):
        if df[i][j]>0:
            minpaths(df,j,sum+df[i][j],count1)
minpaths(df,0,0,0)
print(min(list1))