from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

from apps.shared.models import AbstractModel

from django.db.models import Model, CharField, DecimalField

# AES encryption settings
AES_KEY = b"your_AES_key_16b"  # Ensure the key length is 16 bytes
AES_MODE = AES.MODE_CBC


class Product(AbstractModel):
    price = DecimalField(max_digits=10, decimal_places=2)
    marja = DecimalField(max_digits=10, decimal_places=2)
    package_code = CharField(max_length=50)
    encrypted_price = CharField(max_length=200, blank=True, null=True)
    encrypted_marja = CharField(max_length=200, blank=True, null=True)

    def encrypt_field(self, value):
        cipher = AES.new(AES_KEY, AES_MODE)
        ct_bytes = cipher.encrypt(pad(value.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode("utf-8")
        ct = base64.b64encode(ct_bytes).decode("utf-8")
        return iv, ct

    def get_encrypted_price(self):
        return self.encrypt_field(str(self.price))

    def get_encrypted_marja(self):
        return self.encrypt_field(str(self.marja))

    def get_encrypted_package_code(self):
        return self.encrypt_field(self.package_code)

    def save(self, *args, **kwargs):
        self.encrypted_price, _ = self.get_encrypted_price()
        self.encrypted_marja, _ = self.get_encrypted_marja()
        self.package_code, _ = self.get_encrypted_package_code()
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.package_code

    class Meta:
        db_table = "products"
        verbose_name_plural = "Products"
