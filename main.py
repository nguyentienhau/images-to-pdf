from os import listdir, path, makedirs
from lib import save_images_to_pdf

if __name__ == "__main__":
	comics_dir = "D:/Privates"
	pdf_comics_dir = "D:/Downloads"

	if path.isdir(comics_dir):
		if not path.isdir(pdf_comics_dir):
			makedirs(pdf_comics_dir)

		image_size = (2378, 3363)

		for comic_name in listdir(comics_dir):
			comic_dir = path.join(comics_dir, comic_name)

			if path.isdir(comic_dir):
				print("Create Comic:", comic_name)

				pdf_comic_path = path.join(pdf_comics_dir, comic_name + ".pdf")
				save_images_to_pdf(comic_dir, image_size, pdf_comic_path)

				print("Finish")
