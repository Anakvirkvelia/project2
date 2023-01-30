'''
დავაინსტალირებთ pillow ბიბლიოთეკას, ინსტალაციის შემდეგ
ჩვენ შეგვიძლია პირდაპირ დავამატოთ იგი ჩვენს პროექტში import-ისგამოყენებით.

'''
from PIL import Image, ImageFilter, ImageColor, ImageEnhance




'''
ვქმნით Image კლას და ვიძახებთ init ფუნქციას 

'''
class Images:
    def __init__(self,name):
        self.name = name
        self.width = int()
        self.height = int()


    
    '''
ვქმნით ფუნქციას რომლის პირველი ხაზი კითხულობს სურათს, 
მეორე აჩვენებს ჩვენი სურათის ზომებს კონსოლზე, ხოლო მესამე აჩვენებს მას ეკრანზე

'''       
    def open_image(self):
        img = Image.open(self.name)
        self.width, self.height = img.size
        print(self.width, self.height)
        img.show()




    '''
ვქმნით ფუნქციას რომელიც გვაძლევს საშუალებას,
გამოსახულების ამოჭრის გზას მოცემული ზომების მიხედვით.

'''
    def crop_image(self, left, top, right, bottom):
        img = Image.open(self.name)
        right = self.width
        bottom = self.height / 2
        img = img.crop((left, top, right, bottom))
        img.save('cropped_pic.jpg')




    '''
შემდეგი ფუნქცია გვერდებისა ზოემბის ცვლილებით ცვლის ფოტოს საერთო ზომას

'''
    def resize_image(self, width, height):
        img = Image.open(self.name)
        newsize = (width, height)
        img_resized = img.resize(newsize)
        img_resized.save("resized.jpg")




    '''
მოცემული ფუნქცია გვაძლევს საშუალებას შევასრულოთ მარტივი გეომეტრიული გარდაქმნები, 
როგორიცაა ბრუნვა და ტრანსპოზირება.
'''
    def format_image(self):
        img = Image.open(self.name)
#ფოტოს მოტრიალება ვერტიკალურად
        image_horizontal = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        image_horizontal.save('horizontal_pic.jpg')

# ფოტოს ამოტრიალება
        image_vertical = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        image_vertical.save('vertical_pic.jpg')

# ფოტოს გვერდულად მოტრიალება ->
        image_transpose = img.transpose(Image.Transpose.TRANSPOSE)
        image_transpose.save('transpose_pic.jpg')

# ფოტოს გვერდულად მოტრიალება <-
        image_transverse = img.transpose(Image.Transpose.TRANSVERSE)
        image_transverse.save('transverse_pic.jpg')

# ბრუნვა
        image_rotate = img.rotate(60, expand = True, fillcolor = ImageColor.getcolor('green', 'RGB') )
        image_rotate.save('rotated_pic.jpg')





    '''
ეს ფუნქცია გვაძლევს საშუალებას რომ ფოტოს შევუცვალოთ ნაღება

'''
    def efect_image(self, X):
        image = Image.open(self.name)
# ნათება
        brightness_enhancer = ImageEnhance.Brightness(image)
        enhanced_image = brightness_enhancer.enhance(X)
        enhanced_image.save("br.jpg")
# ფერები
        color_enhancer = ImageEnhance.Color(image)
        enhanced_image = color_enhancer.enhance(X)
        enhanced_image.save("col.jpg")

# კონტრასტი
        contrast_enhancer = ImageEnhance.Contrast(image)
        enhanced_image = contrast_enhancer.enhance(X)
        enhanced_image.save('cont.jpg')

# სიმკვეთრე
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        enhanced_image = sharpness_enhancer.enhance(X)
        enhanced_image.save('shar.jpg')




    '''
მოცემულ ფუნქციაში შეგვიძლია pillow-ში ჩაშენებული ფილტების საშუალებით გავაუმკობესოთ ან უბრალოდ შევუცვალოთ გამოსახულება


'''
    def add_filters(self):
        img = Image.open(self.name)
# BLACK_WHItE
        img = img.convert('L')
        img.save("bleck_white.jpg")
# BLUR FILTER
        image_blur = img.filter(ImageFilter.BLUR)
        image_blur.save('blur_pic.jpg')
#CONTUR FILTER
        contour_image = img.filter(ImageFilter.CONTOUR)
        contour_image.save('Contour_pic.jpg')
# DETAIL FILTER
        detail_image = img.filter(ImageFilter.DETAIL)
        detail_image.save('detail_pic.jpg')
# EDGE ENHANCE FILTER
        edge_enhance_image = img.filter(ImageFilter.EDGE_ENHANCE)
        edge_enhance_image.save('edge_pic.jpg')
# SMOOTH FILTER
        smooth_image = img.filter(ImageFilter.SMOOTH)
        smooth_image.save('smooth_pic.jpg')
#FIND FILTER
        image_find = img.filter(ImageFilter.FIND_EDGES)
        image_find.save('find_pic.jpg')
#EMBOS FILTER
        image_emboss = img.filter(ImageFilter.EMBOSS)
        image_emboss.save('emboss_pic.jpg')
#SHARO FILTER
        image_sharp = img.filter(ImageFilter.SHARPEN)
        image_sharp.save('sharp_pic.jpg')
#SMOOTH FILTER
        image_smooth = img.filter(ImageFilter.SMOOTH)
        image_smooth.save('smooth_pic.jpg')

#Combine filters
        image_emboss = img.filter(ImageFilter.EMBOSS)
        image_embos_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius = 3))
        image_embos_blur.save('comb_pic.jpg')




'''
ვქმნით Picture ობიექტს და შემდგომ გამოვიძახებთ მეთოდს

'''
Picture = Images("picture.jpg")


Picture.open_image()
Picture.crop_image(left=5, top=10, right=4, bottom=6)
Picture.resize_image(300, 300)
Picture.format_image()
Picture.efect_image(20)
Picture.add_filters()




