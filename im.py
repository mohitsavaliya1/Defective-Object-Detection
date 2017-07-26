import sys

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

def main():

file1, file2 = sys.argv[1:1+2]
img1 = to_grayscale(imread(file1).astype(float)) #grayscale image to reduce noise
img2 = to_grayscale(imread(file2).astype(float))
n_m, n_0 = compare_images(img1, img2)
print n_m/img1.size

def compare_images(img1, img2):

img1 = normalize(img1) #normalize image
img2 = normalize(img2)
diff = img1 - img2 #difference of two images
m_norm = sum(abs(diff)) #main logic of Manhattan Norm
z_norm = norm(diff.ravel(), 0)

return (m_norm, z_norm)

def to_grayscale(arr):

"If arr is a color image (3D array), convert it to grayscale (2D array)."
if len(arr.shape) == 3:
return average(arr, -1)
else:
return arr

def normalize(arr):
rng = arr.max()-arr.min()
amin = arr.min()
return (arr-amin)*255/rng
if __name__ == "__main__":
main()
