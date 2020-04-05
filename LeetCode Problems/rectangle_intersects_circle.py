class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx, cy, rx, ry, rw, rh = x_center, y_center, x1, y1, x2-x1, y2-y1
        testX = cx
        testY = cy

        if (cx < rx): testX = rx
        elif (cx > rx+rw): testX = rx+rw
        if (cy < ry): testY = ry
        elif (cy > ry+rh): testY = ry+rh
        distX = cx-testX
        distY = cy-testY
        distance = math.sqrt( (distX*distX) + (distY*distY) )

        if (distance <= radius):
            return True
          
        return False
