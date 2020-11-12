from wtforms import MultipleFileField, SelectField, StringField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField


class ChallengeSearchForm(BaseForm):
    field = SelectField(
        "Search Field",
        choices=[
            ("name", "Название"),
            ("id", "ID"),
            ("category", "Категория"),
            ("type", "Тип"),
        ],
        default="name",
        validators=[InputRequired()],
    )
    q = StringField("Параметр", validators=[InputRequired()])
    submit = SubmitField("Поиск")


class ChallengeFilesUploadForm(BaseForm):
    file = MultipleFileField(
        "Upload Files",
        description="Attach multiple files using Control+Click or Cmd+Click.",
        validators=[InputRequired()],
    )
    submit = SubmitField("Upload")
