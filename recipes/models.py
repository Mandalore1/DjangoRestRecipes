from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    """Рецепт"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes", verbose_name="Пользователь")
    favorited_by = models.ManyToManyField(User, related_name="favorite_recipes", verbose_name="Избран пользователями",
                                          blank=True, null=True)

    title = models.CharField(max_length=150, blank=False, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    content = models.TextField(blank=True, null=True, verbose_name="Рецепт")
    image = models.ImageField(upload_to="recipe_images", verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    views = models.PositiveIntegerField(default=1, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeIngredient(models.Model):
    """Ингредиент рецепта"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт", related_name="ingredients")

    name = models.CharField(max_length=150, blank=False, verbose_name="Название")
    quantity = models.IntegerField(verbose_name="Количество")
    # Варианты единиц измерения
    UNITS = [
        ("шт.", "шт."),
        ("г.", "г."),
        ("кг.", "кг."),
        ("л.", "л."),
        ("мл.", "мл."),
    ]
    unit = models.CharField(max_length=10, choices=UNITS, verbose_name="Единица измерения")

    def __str__(self):
        return self.recipe.title + " " + self.name

    class Meta:
        verbose_name = "Ингредиент рецепта"
        verbose_name_plural = "Ингредиенты рецептов"


class Comment(models.Model):
    """Комментарий рецепта"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="comments")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт", related_name="comments")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Родительский комментарий", null=True,
                               blank=True, related_name="replies")

    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return f"{self.recipe.title} ({self.user.username} {self.created_at})"

    class Meta:
        verbose_name = "Комментарий рецепта"
        verbose_name_plural = "Комментарии рецептов"
