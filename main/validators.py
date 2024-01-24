from rest_framework.exceptions import ValidationError


def prohibition_change_debt(new_debt, old_debt):
    if old_debt is not None and old_debt != new_debt:
        raise ValidationError("Запрещено изменять это поле!")
