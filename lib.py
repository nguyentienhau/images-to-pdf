from os import path, listdir
from PIL import Image

def is_image_file(image_path = ""):
	image_extensions = (".png", ".jpeg", ".jpg", ".bmp", ".webp", ".tiff", ".gif", ".rgb", ".pbm", ".pgm", ".ppm", ".rast", ".xbm", ".exr")
	return path.isfile(image_path) and image_path.lower().endswith(image_extensions)

def load_image(image_path = "", image_size = (2378, 3363)):
	try:
		if is_image_file(image_path):
			return Image.open(image_path).convert("RGB").resize(image_size, Image.Resampling.LANCZOS)
		else:
			return None
	except:
		print("Error When Open Image:", image_path, KeyError, NameError)

def save_images_to_pdf(images_dir = "", image_size = (2378, 3363), pdf_path = ""):
	try:
		images = []
		image_names = listdir(images_dir)
		image_names.sort()

		for image_name in image_names:
			image_path = path.join(images_dir, image_name)
			image = load_image(image_path, image_size)
			print(image_path)

			if image:
				images.append(image)
			else:
				return False

		if len(images) > 0:
			images[0].save(pdf_path, "PDF", bitmap_format="png", save_all=True, optimize=True, append_images=images[1:])
	except:
		print("Error When Merge Images To PDF", pdf_path, KeyError, NameError)
