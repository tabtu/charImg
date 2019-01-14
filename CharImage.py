from PIL import Image
import cv2

def resize():
	img = cv2.imread('0.jpg')
	width, height = img.shape[:2]
	img = cv2.resize(img, (int(height*0.25), int(width*0.25)), interpolation=cv2.INTER_AREA)
	cv2.imwrite('1.jpg', img)
	cv2.imshow('test', img)

def get_Text(img):
	img = img.convert("L")
	charlist = ''
	for h in range(0, img.size[1]):
		for w in range(0, img.size[0]):
			gray = img.getpixel((w, h))
			pos = gray / 256
			charlist = charlist + codelist[int((count - 1) * pos)]
		charlist = charlist + '\r'
	return charlist

def getImage():
	file = open('./1.jpg', 'rb')
	img = Image.open(file)
	return img

def trantxt():
	outfile = open('1.txt', 'w')
	outfile.write(get_Text(img))
	outfile.close

if __name__ == '__main__':
	resize()
	img = getImage()
	width, height = img.size[0], img.size[1]
	codelist = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/^|()l{}[]?-_+~<>i!I;:,."
	count = len(codelist)
	scale = width / height
	img = img.resize((int(width * 0.2), int(width * 0.1 / scale)))
	trantxt()
