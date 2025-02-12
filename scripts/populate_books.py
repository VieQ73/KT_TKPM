import os
import django
import random
from faker import Faker
from book.models import Book, Category

# Cấu hình Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ldquy_project1.settings")
django.setup()

fake = Faker()  # Ngôn ngữ mặc định là tiếng Anh

# Danh sách thể loại sách
categories = ["Literature", "Science", "Mystery", "History", "Economics", "Technology"]
category_objects = [Category.objects.get_or_create(name=cat)[0] for cat in categories]

# Xóa toàn bộ sách trước khi thêm mới (Tùy chọn, nếu muốn reset database)
Book.objects.all().delete()

# Tạo dữ liệu sách
for _ in range(30):
    title = fake.sentence(nb_words=4).rstrip('.')  # Xóa dấu chấm cuối tiêu đề
    author = fake.name()
    publisher = fake.company()
    price = round(random.uniform(15, 68), 2)  # Giá từ $15 đến $68, làm tròn 2 số thập phân
    description = fake.paragraph(nb_sentences=3)
    
    book = Book.objects.create(
        title=title,
        author=author,
        publisher=publisher,
        price=price,  # Giá tiền là số thực, làm tròn đến 2 chữ số sau dấu thập phân
        description=description
    )

    # Gán ít nhất 1 thể loại cho sách
    book.categories.set(random.sample(category_objects, random.randint(1, 3)))

print("✅ 30 books have been added to the database with prices in USD and proper categories!")
