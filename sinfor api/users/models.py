from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, nome, cnpj, telefone, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório')
        if not nome:
            raise ValueError('O campo nome da empresa é obrigatório')
        if not cnpj:
            raise ValueError('O campo CNPJ é obrigatório')
        if not telefone:
            raise ValueError('O campo telefone é obrigatório')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nome=nome,
            cnpj=cnpj,
            telefone=telefone,
            **extra_fields              # usado para mais flexibilidade na criação dos usuarios
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cnpj, telefone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nome, cnpj, telefone, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)  # formato XX.XXX.XXX/XXXX-XX
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, )           # formato armazenar apenas os numeros
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cnpj', 'telefone']

    def __str__(self):
        return self.nome

