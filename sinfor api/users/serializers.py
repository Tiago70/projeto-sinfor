from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializerNew(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    cnpj = serializers.CharField(max_length=18,
                                validators=[
                                    UniqueValidator(
                                        queryset=User.objects.all(),
                                        message="Este cnpj já está cadastrado."
                                    )
                                ])
    email = serializers.EmailField(validators=[
                                    UniqueValidator(
                                        queryset=User.objects.all(),
                                        message="Este email já está cadastrado"
                                    )]
                                )

    class Meta:
        model = User
        fields = ('nome', 'cnpj', 'email', 'telefone', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializerLogin(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email':'email ou senha inválidos'})

        if not user.check_password(password):
            raise serializers.ValidationError({'email':'email ou senha inválidos'})
        
        # colocar verificação de conta ativa aqui (se houver)

        data['user'] = user
        return data
