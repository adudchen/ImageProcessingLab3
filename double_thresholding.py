from numpy import zeros, max


def thresholding(im):
    thres = zeros(im.shape)
    strong = 1.0
    weak = 0.5
    mmax = max(im)
    lo, hi = 0.1 * mmax, 0.8 * mmax
    strongs = []
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            px = im[i][j]
            if px >= hi:
                thres[i][j] = strong
                strongs.append((i, j))
            elif px >= lo:
                thres[i][j] = weak
    return thres, strongs
