from django.core.management.base import BaseCommand
from book.models import Book, Category
from faker import Faker
import random

class Command(BaseCommand):
    help = "Xóa tất cả sách cũ và tạo mới 30 cuốn sách giả lập"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Xóa toàn bộ sách và thể loại cũ
        print("🗑️ XXa tất cả  thể loại cũ...")
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
            books.append(book)

        # Lưu tất cả sách cùng lúc (tăng tốc hiệu suất)
        created_books = Book.objects.bulk_create(books)

        # Gán thể loại cho từng sách sau khi tạo xong
        for book in created_books:
            book.categories.set(random.sample(categories, random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS("✅ Đã tạo 30 cuốn sách mới thành công!"))
