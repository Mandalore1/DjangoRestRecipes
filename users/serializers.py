from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from users.models import UserAdditionalInfo


class AdditionalInfoSerializer(serializers.ModelSerializer):
    """Дополнительные сведения о пользователях"""
    class Meta:
        model = UserAdditionalInfo
        exclude = ["id", "user"]


class UserDetailSerializer(serializers.ModelSerializer):
    """Детальное представление пользователя"""
    additional_info = AdditionalInfoSerializer()

    def update(self, instance, validated_data):
        """Сохраняем дополнительную информацию"""
        additional_info = validated_data.pop("additional_info", None)
        if additional_info:
            try:
                instance.additional_info
            except ObjectDoesNotExist:
                # Если у пользователя еще нет дополнительных сведений
                instance.additional_info = UserAdditionalInfo.objects.create(**additional_info, user=instance)
            else:
                # Если у пользователя уже есть дополнительные сведения
                for k, v in additional_info.items():
                    setattr(instance.additional_info, k, v)
                instance.additional_info.save()

        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "date_joined", "last_login", "additional_info"]
