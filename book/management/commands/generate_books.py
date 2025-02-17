from django.core.management.base import BaseCommand
from book.models import Book, Category
from faker import Faker
import random

class Command(BaseCommand):
    help = "Xóa tất cả sách cũ và tạo mới 20 cuốn sách giả lập"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Xóa toàn bộ sách và thể loại cũ
        print("🗑️ Xoá tất cả  thể loại cũ...")
        Book.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING("🔄 Đã xóa toàn bộ sách và thể loại cũ."))

        # Danh sách thể loại mặc định
        default_categories = [
            "Khoa học", "Văn học", "Lịch sử", "Công nghệ", "Kinh doanh", 
            "Kinh dị", "Trinh thám", "Võ hiệp", "Tu tiên", "Truyện ngắn", "Hồi ký"
        ]

        # Tạo lại danh sách thể loại
        categories = [Category.objects.create(name=name) for name in default_categories]

        # Tạo 30 cuốn sách mới
        books = []
        for _ in range(30):
            book = Book(
                title=fake.sentence(nb_words=4).rstrip('.'),
                author=fake.name(),
                price=round(random.uniform(5, 50), 2),
                description=fake.paragraph(),
                publisher=fake.company(),
                publication_year=random.randint(1990, 2024),
            )
            book.save()  # Lưu sách vào cơ sở dữ liệu trước khi gán thể loại
            books.append(book)

        # Gán thể loại cho từng sách sau khi đã lưu vào cơ sở dữ liệu
        for book in books:
            book.categories.set(random.sample(categories, random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS("✅ Đã tạo 20 cuốn sách mới thành công!"))
