from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Título do Post", validators=[DataRequired()])
    subtitle = StringField("Subtítulo", validators=[DataRequired()])
    img_url = StringField("URL da imagem", validators=[DataRequired(), URL()])
    body = CKEditorField("Conteudo do post", validators=[DataRequired()])
    submit = SubmitField("ENVIAR")


class CreteNewUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    name = StringField("Nome", validators=[DataRequired()])
    submit = SubmitField("REGISTRAR!")


class LoginUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("LOGIN")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comentário", validators=[DataRequired()])
    submit = SubmitField("COMENTAR")
