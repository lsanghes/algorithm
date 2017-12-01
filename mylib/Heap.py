# heap invariant: A[i] <= A[i*2+1] and A[i] <= A[i*2+2]
import heapq

array = [1,2,6,4,3,5]
print(array)

# heappush take log(N) time and maintain heap invariant
heap = []
for a in array:
    heapq.heappush(heap, a)
print(heap)

# heapify only takes O(N) time
heapq.heapify(array) # array now is a heap
print(array)

# heappop takes log(N) time and maintain heap invariant
while heap:
    min_num = heapq.heappop(heap) # heappop takes log(N) time
    print(min_num)
