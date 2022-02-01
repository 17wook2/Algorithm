from collections import defaultdict
answer = 0
def solution(info, edges):
    graph = defaultdict(list)
    for edge in edges:
        a,b = edge
        graph[a].append(b)
        graph[b].append(a)
    v = [0]*len(info)
    v[0] = 1
    tracking(graph,v,info,1,0)
    return answer

def tracking(graph,visited,info,sheep,wolf):
    global answer
    answer = max(answer,sheep)
    if sheep <= wolf:
        return
    for i in range(len(visited)):
        if visited[i]:
            for e in graph[i]:
                if not visited[e]:
                    visited[e] = 1
                    if info[e] == 1:
                        tracking(graph,visited,info,sheep,wolf+1)
                        visited[e] = 0
                    else:
                        tracking(graph,visited,info,sheep+1,wolf)
                        visited[e] = 0