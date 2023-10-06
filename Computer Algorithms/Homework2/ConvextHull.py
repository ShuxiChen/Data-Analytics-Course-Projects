# Reference: https://github.com/zifanw/ConvexHull2D

import numpy as np
import matplotlib.pyplot as plt

def divide_area(start, end, points):

    S1, S2 = [], []
    for _, point in enumerate(points):
        dis =  compute_distance(start, end, point)
        if dis > 0:
            S1.append(point)
        else:
            S2.append(point)
    S1 = np.vstack(S1) if len(S1) else None
    S2 = np.vstack(S2) if len(S2) else None
    return S1, S2


def triangle_partition(points, P, C, Q):

    S1, S2 = [], []
    for _, point in enumerate(points):
        disPC = compute_distance(P, C, point) # determine which side the point is on
        disCQ = compute_distance(C, Q, point)
        if disPC > 0 and disCQ < 0:
            S1.append(point)
        elif disPC < 0 and disCQ > 0:
            S2.append(point)
    S1 = np.vstack(S1) if len(S1) else None
    S2 = np.vstack(S2) if len(S2) else None
    return S1, S2    
    
def compute_distance(start, end, point, eps=1e-8):

    return np.cross(end-start,point-start)/(np.linalg.norm(end-start)+eps) # prevent from dividing by 0

def clock_sort(x):
    
    x0, y0 = x[:,0].mean(), x[:,1].mean()
    theta = np.arctan2(x[:,1] - y0, x[:,0] - x0)
    index = np.argsort(theta)
    x = x[index]
    
    return x

class ConvexHull2D:

    def __init__(self):
        self.points = None
        self.convext_hull = []

    def __call__(self, point_set):
        return self.forward(point_set)

    def reset(self):
        self.points = None
        self.convext_hull = []

    def forward(self, point_set):

        self.reset()          
        self.points = np.unique(point_set, axis=0) # remove duplicates
        return self._quickhull()

    def _quickhull(self):        
        self.points = self.points[np.lexsort(np.transpose(self.points)[::-1])]  # sort x, and then y
        left_most, right_most = self.points[0], self.points[-1]
        self.points = self.points[1:-1]     # the rest points
        self.convext_hull.append(left_most)     # add the left-most point into the output
        self.convext_hull.append(right_most)    # add the right-most point into the output

        self.right_points, self.left_points = divide_area(start=left_most, 
                                                          end=right_most, 
                                                          points=self.points)

        self._findhull(self.right_points, left_most, right_most)
        self._findhull(self.left_points, right_most, left_most)

        self.convext_hull = np.stack(self.convext_hull)
        self.convext_hull = clock_sort(self.convext_hull)
                     
        return self.convext_hull

    def _findhull(self, points, P, Q):
        
        if points is None:
            return

        distance = 0.0
        C, index = None, None
        for i, point in enumerate(points):
            current_dis = abs(compute_distance(P, Q, point))
            if current_dis > distance: # find a maximun point among all the points
                C = point
                index = i
                distance = current_dis
        if C is not None:
            self.convext_hull.append(C)
            points = np.delete(points, index, axis=0) # delete C from original points
            
        S1, S2 = triangle_partition(points, P, C, Q) # interate this process for S1 and S2
        self._findhull(S1, P, C)
        self._findhull(S2, C, Q)
    

## test 
model = ConvexHull2D()
points = np.random.random((100,2)) * 100 # normal distribution and scaled
points -= np.random.random() * 100 # positive and negative data points
plt.plot(points[:,0], points[:,1], 'o')
convex_hull = model(points)

# Close the hull during plot by making the head and tail as the same point
convex_hull = np.vstack([convex_hull, convex_hull[0]])

# Draw the lines between adjacent points in the convex hull
for i in range(len(convex_hull)):
    plt.plot([convex_hull[i,0], convex_hull[i+1,0]], [convex_hull[i,1], convex_hull[i+1,1]], 'k-')

plt.show()
print ("The vertices of convex hull are")
print (convex_hull)
