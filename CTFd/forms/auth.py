from wtforms import PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.forms.users import attach_custom_user_fields, build_custom_user_fields


def RegistrationForm(*args, **kwargs):
    class _RegistrationForm(BaseForm):
        name = StringField("Пользователь", validators=[InputRequired()])
        email = EmailField("Почта", validators=[InputRequired()])
        password = PasswordField("Пароль", validators=[InputRequired()])
        submit = SubmitField("Зарегистрироваться")

        @property
        def extra(self):
            return build_custom_user_fields(
                self, include_entries=False, blacklisted_items=()
            )

    attach_custom_user_fields(_RegistrationForm)

    return _RegistrationForm(*args, **kwargs)


class LoginForm(BaseForm):
    name = StringField("Пользователь или почта", validators=[InputRequired()])
    password = PasswordField("Пароль", validators=[InputRequired()])
    submit = SubmitField("Войти")


class ConfirmForm(BaseForm):
    submit = SubmitField("Повторить отправку")


class ResetPasswordRequestForm(BaseForm):
    email = EmailField("Почта", validators=[InputRequired()])
    submit = SubmitField("Отправить")


class ResetPasswordForm(BaseForm):
    password = PasswordField("Пароль", validators=[InputRequired()])
    submit = SubmitField("Отправить")
