from flask import session
from wtforms import PasswordField, SelectField, StringField
from wtforms.fields.html5 import DateField, URLField

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.forms.users import attach_custom_user_fields, build_custom_user_fields
from CTFd.utils.countries import SELECT_COUNTRIES_LIST


def SettingsForm(*args, **kwargs):
    class _SettingsForm(BaseForm):
        name = StringField("Имя пользователя")
        email = StringField("Email")
        password = PasswordField("Новый пароль")
        confirm = PasswordField("Текущий пароль")
        affiliation = StringField("Учреждение")
        website = URLField("Сайт")
        country = SelectField("Страна", choices=SELECT_COUNTRIES_LIST)
        submit = SubmitField("Подтвердить")

        @property
        def extra(self):
            return build_custom_user_fields(
                self,
                include_entries=True,
                fields_kwargs={"editable": True},
                field_entries_kwargs={"user_id": session["id"]},
            )

    attach_custom_user_fields(_SettingsForm, editable=True)

    return _SettingsForm(*args, **kwargs)


class TokensForm(BaseForm):
    expiration = DateField("Expiration")
    submit = SubmitField("Generate")
