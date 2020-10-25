from math import pi, cos, sin, atan2
from operator import itemgetter
EPS = 10**(-9)
INF = 10**16

def eq(value1, value2):
    return abs(value1-value2) <= EPS

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "{0:.8f} {1:.8f}".format(self.x, self.y)
        #return "{0} {1}".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scal):
        return Point(self.x*scal, self.y*scal)
    
    def __truediv__(self, scal):
        return Point(self.x/scal, self.y/scal)
    
    def __eq__(self, other):
        return eq(self.x, other.x) and eq(self.y, other.y)

    # 原点からの距離
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

    def arg(self):
        return atan2(self.y, self.x)
    
# 原点を中心にrad角だけ回転した点
def Rotation(vec: Point, rad):
    return Point(vec.x*cos(rad)-vec.y*sin(rad), vec.x*sin(rad)+vec.y*cos(rad))


class Circle():
    def __init__(self, p, r):
        self.p = p
        self.r = r


class Line():
    # 点a, bを通る
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "[({0}, {1}) - ({2}, {3})]".format(self.a.x, self.a.y, self.b.x, self.b.y)
    
    def arg(self):
        return (a-b).arg() % pi

    # pointを通って平行
    def par(self, point):
        return Line(point, point+(self.a-self.b))

    # pointを通って垂直
    def tan(self, point):
        return Line(point, point + Rotation(self.a-self.b, pi/2))


class Segment(Line):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def length(self):
        return abs(self.a-self.b)



# 符号付き面積
def cross(vec1: Point, vec2: Point):
    return vec1.x*vec2.y - vec1.y*vec2.x

# 内積
def dot(vec1: Point, vec2: Point):
    return vec1.x*vec2.x + vec1.y*vec2.y

# 点a->b->cの回転方向
def ccw(a, b, c):
    if cross(b-a, c-a) > EPS: return +1 # COUNTER_CLOCKWISE
    if cross(b-a, c-a) < -EPS: return -1 # CLOCKWISE
    if dot(c-a, b-a) < -EPS: return +2 # c -> a -> b
    if abs(b-a) < abs(c-a): return -2 # a -> b -> c
    return 0 # a -> c -> b


# pのlへの射影
def projection(l, p):
    t = dot(l.b-l.a, p-l.a) / abs(l.a-l.b)**2
    return l.a + (l.b-l.a)*t

# pのlによる反射
def reflection(l, p):
    return p + (projection(l, p) - p)*2

def isPararell(l1, l2):
    return eq(cross(l1.a-l1.b, l2.a-l2.b), 0)

def isVertical(l1, l2):
    return eq(dot(l1.a-l1.b, l2.a-l2.b), 0)


def Intersect_lp(l, p):
    return abs(ccw(l.a, l.b, p)) != 1

def Intersect_ll(l1, l2):
    return not isPararell(l1, l2) or Intersect_lp(l1, l2.a)

def Intersect_sp(s, p):
    return ccw(s.a, s.b, p) == 0

def Intersect_ss(s1, s2):
    return ccw(s1.a, s1.b, s2.a)*ccw(s1.a, s1.b, s2.b) <= 0 and ccw(s2.a, s2.b, s1.a)*ccw(s2.a, s2.b, s1.b) <= 0

def Intersect_ls(l, s):
    return cross(l.b - l.a, s.a - l.a) * cross(l.b - l.a, s.b - l.a) < EPS

def Intersect_cp(c, p):
    return abs(abs(c.p - p) - c.r) < EPS

def Intersect_cl(c, l):
    return distance_lp(l, c.p) <= c.r + EPS

def Intersect_cs(c, s):
    h = projection(s, c.p)
    if abs(h - c.p)**2 - c.r**2 > EPS: return 0 # 遠い
    d1 = abs(c.p - s.a); d2 = abs(c.p - s.b)
    if d1 < c.r - EPS and d2 < c.r - EPS: return 0 # どちらも内側
    if (d1 < c.r - EPS and d2 > c.r + EPS) or (d1 > c.r + EPS and d2 < c.r - EPS): return 1 # 片方だけ内側
    if dot(s.a-h, s.b-h) < 0: return 2 # 2点で交わる
    return 0


def Intersect_cc(c1, c2):
    if c1.r < c2.r:
        c1, c2 = c2, c1
    d = abs(c1.p - c2.p)
    if eq(c1.r + c2.r, d): return 3 # 内接
    if eq(c1.r - c2.r, d): return 1 # 外接
    if c1.r + c2.r < d: return 4 # 含まれてる
    if c1.r - c2.r < d: return 2 # 2交点持つ
    return 0 # 離れてる


def distance_pp(p1, p2):
    return abs(p1-p2)

def distance_lp(l, p):
    return abs(projection(l,p)-p)

def distance_ll(l1, l2):
    return 0 if Intersect_ll(l1, l2) else distance_lp(l1, l2.a)

def distance_sp(s, p):
    r = projection(s, p)
    if Intersect_sp(s, r): return abs(r-p)
    return min(abs(s.a-p), abs(s.b-p))

def distance_ss(s1, s2):
    if Intersect_ss(s1, s2): return 0
    return min([distance_sp(s1, s2.a), distance_sp(s1, s2.b), distance_sp(s2, s1.a), distance_sp(s2, s1.b)])

def distance_ls(l, s):
    if Intersect_ls(l, s): return 0
    return min(distance_lp(l, s.a), distance_lp(l, s.b))


def crosspoint_ll(l1, l2):
    A = cross(l1.b - l1.a, l2.b - l2.a)
    B = cross(l1.b - l1.a, l1.b - l2.a)
    if eq(abs(A), 0) and eq(abs(B), 0): return l2.a
    return l2.a + (l2.b - l2.a) * B / A

def crosspoint_ss(s1, s2):
    return crosspoint_ll(s1, s2)

def crosspoint_lc(l, c):
    p = projection(l, c.p)
    if eq(distance_lp(l, c.p), c.r): return [p]
    e = (l.b - l.a) / abs(l.b-l.a)
    dis = (c.r**2-abs(p-c.p)**2)**0.5
    return [p + e*dis, p - e*dis]

def crosspoint_sc(s, c):
    l = Line(s.a, s.b)
    if Intersect_cs(c, s) == 2: return crosspoint_lc(l, c)
    Points = crosspoint_lc(l, c)
    if len(Points) == 1:
        return Points
    if dot(s.a-Points[0], s.b-Points[0]) < 0: return [Points[0]]
    return [Points[1]]


def crosspoint_cc(c1, c2):
    d = abs(c1.p-c2.p)
    if not abs(c1.r-c2.r) <= d <= c1.r+c2.r:
        return []
    mid_p = (c2.p * (c1.r**2-c2.r**2+d**2) + c1.p * (c2.r**2-c1.r**2+d**2)) / (2*d**2)
    tanvec = Rotation(c1.p-c2.p, pi/2)
    return crosspoint_lc(Line(mid_p, mid_p+tanvec), c1)


# pからのcの接点
def tangent_cp(c, p):
    return crosspoint_cc(c, Circle(p, (abs(p-c.p)**2 - c.r**2)**0.5))

# 共通接線
def tangent_cc(c1, c2):
    pass


def isConvex(Points):
    n = len(Points)
    for i in range(n):
        if ccw(Points[i-1], Points[i], Points[(i+1)%n]) == -1: return False
    return True

def ConvexHull(Points):
    Points.sort(key=lambda p: p.y)
    Points.sort(key=lambda p: p.x)

    Qs = []
    for p in Points:
        while len(Qs) > 1 and ccw(Qs[-2], Qs[-1], p) == -1:
            Qs.pop()
        Qs.append(p)
        
    t = len(Qs)
    Qs.pop()
    for p in reversed(Points):
        while len(Qs) > t and ccw(Qs[-2], Qs[-1], p) == -1:
            Qs.pop()
        Qs.append(p)
    Qs.pop()

    return Qs

def contains(Points, p):
    inside = False
    for i in range(len(Points)):
        a = Points[i-1] - p
        b = Points[i] - p
        if a.y > b.y: a, b = b, a
        if a.y <= 0 and 0 < b.y and cross(a, b) < 0:
            inside = not inside
        if cross(a, b) == 0 and dot(a, b) <= 0:
            return 1 #辺上
    return 2 if inside else 0
    
# 多角形の面積
def area(Points):
    S = 0
    for i in range(len(Points)):
        S += cross(Points[i-1], Points[i])/2
    return S

# ソートしてから入れる
def ClosestPair(Points):
    l = len(Points)
    if l <= 1: return INF, Points
    d1, nearPoints1 = ClosestPair(Points[:l//2])
    d2, nearPoints2 = ClosestPair(Points[l//2:])
    retPoints = []
    ind = 0
    for p1 in nearPoints1:
        while ind != len(nearPoints2) and nearPoints2[ind].y < p1.y:
            retPoints.append(nearPoints2[ind])
            ind += 1
        retPoints.append(p1)
    while ind != len(nearPoints2):
        retPoints.append(nearPoints2[ind])
        ind += 1
    
    d = min(d1, d2)
    B = []
    border_x = Points[l//2].x
    for p in retPoints:
        if abs(border_x-p.x) > d + EPS: continue
        for b in reversed(B):
            if p.y - b.y > d: break
            d = min(d, abs(p-b))
        B.append(p)
    return d, retPoints
