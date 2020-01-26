from gaussian_filter import gaussian
from gradient import gradient
from nonmax_suppression import maximum
from double_thresholding import thresholding
from numpy import array, zeros
from PIL import Image
from matplotlib.pyplot import gray
import cv2

class tracking:
    def __init__(self, tr):
        self.im = tr[0]
        strongs = tr[1]

        self.vis = zeros(im.shape, bool)
        self.dx = [1, 0, -1,  0, -1, -1, 1,  1]
        self.dy = [0, 1,  0, -1,  1, -1, 1, -1]
        for s in strongs:
            if not self.vis[s]:
                self.dfs(s)
        for i in range(self.im.shape[0]):
            for j in range(self.im.shape[1]):
                self.im[i, j] = 1.0 if self.vis[i, j] else 0.0

    def dfs(self, origin):
        q = [origin]
        while len(q) > 0:
            s = q.pop()
            self.vis[s] = True
            self.im[s] = 1
            for k in range(len(self.dx)):
                for c in range(1, 16):
                    nx, ny = s[0] + c * self.dx[k], s[1] + c * self.dy[k]
                    if self.exists(nx, ny) and (self.im[nx, ny] >= 0.5) and (not self.vis[nx, ny]):
                        q.append((nx, ny))
        pass

    def exists(self, x, y):
        return x >= 0 and x < self.im.shape[0] and y >= 0 and y < self.im.shape[1]


if __name__ == '__main__':
    from sys import argv
    im = array(Image.open(argv[1]))

    im = im[:, :, 0]
    gim = gaussian(im)
    grim, gphase = gradient(gim)
    gmax = maximum(grim, gphase)
    thres = thresholding(gmax)
    edge = tracking(thres)

    gray()

    cv2.imshow("NonMax", gmax)
    cv2.imshow("Result", edge.im)
    cv2.waitKey(0)
