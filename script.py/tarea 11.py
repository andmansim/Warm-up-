import random 
iterations = 10000
variables =['salary', 'location', 'work hours', "job position", "services", "partners", "environment", "social benefits", "prestige", "transport"]

def Monte_Carlo(grade):
    final_results = []
    weight = [0.2, 0.15, 0.15, 0.07, 0.11, 0.03, 0.08, 0.10, 0.05, 0.06]
    for i in range(iterations):
        results = []
        for a in range(len(variables)):
            value = weight[a] * (random.uniform(grade[a][0], grade[a][1]))
            results.append(value)
        final_results.append(sum(results))
    return final_results

j = Monte_Carlo([[5,10], [3,6], [5.5,8], [4,8], [7.7,8], [6,8], [8,9], [1,5], [6,7.04], [4.68,8.01]])
k = Monte_Carlo([[2,6], [8.5,9.56], [7,9],[7,9], [5,8], [6,10], [3.45, 6.7], [8,10], [4.5,7], [6,9]])
p = Monte_Carlo([[6,8], [8,9], [2,6],[3,7], [6.89,8.65], [9,10], [7,9], [3,8], [4.03,7.1], [5.12, 8]])