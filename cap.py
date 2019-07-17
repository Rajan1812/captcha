from captcha.image import ImageCaptcha  # pip install captcha
import random
import matplotlib.pyplot as plt # pip install matplotlib

number_list = ['1','2','3','4','5','6','7','8','9','0']
alpha_lower = ['a','b','c','d','e','f','g','h']
alpha_uppder = ['A','B','C','D','E','F','G','H'] 

total_string = number_list + alpha_uppder + alpha_lower

def create_random_string(char_string_size=10):
	c_string_list = []
	for i in range(char_string_size):
		char = random.choice(total_string)
		c_string_list.append(char)    

	c_string = ''
	for item in c_string_list:
		c_string += str(item) # converting the list as string 

	return c_string


def create_image_captcha(captcha_text):
	image_captcha = ImageCaptcha()
	image = image_captcha.generate_image(captcha_text)  # from captcha module calling function to create an image (blank image)
	image_captcha.create_noise_curve(image, image.getcolors()) # to create noise in the image
	image_captcha.create_noise_dots(image, image.getcolors())  # to create dot noise in the image
	image_file = "./captcha_"+captcha_text + ".png"        #saving the image as a png file
	image_captcha.write(captcha_text, image_file)			# writing the captcha text on to the generated image
	plt.imshow(image) 										# matplotlib.pyplot moduleto display the image
	plt.show()

if __name__ == '__main__':
	captcha_text = create_random_string()
	create_image_captcha(captcha_text)
