import bcrypt
from script_db import get_users, search_user, load_ferias_from_db, save_to_excel
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def encrypt(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def verifi_exists_name(name):
    users = get_users()

    for user in users:
        if user[0] == name:
            return True

    return False


def check_credentials(name, password):
    user_log = search_user(name)
    if not user_log:
        return False

    verify = verify_password(password, user_log[1])

    if verify:
        return True

    return False


def generate_excel():
    df_vacation = load_ferias_from_db()
    if df_vacation.empty:
        return False
    save_to_excel(df_vacation)
    return True


def generate_pdf():
    df_vacation = load_ferias_from_db()
    name_pdf = "ferias.pdf"

    if df_vacation.empty:
        return False

    # Configuração do PDF
    doc = canvas.Canvas(name_pdf, pagesize=A4)
    height, width = A4  #width/largura, height/altura
    doc.setFont("Helvetica", 10)

    # Título do PDF
    doc.drawString(100, height - 50, "Tabela de Férias")

    # Configuração para a tabela
    x_offset = 50
    y_offset = height - 100
    line_height = 15

    # Adiciona os títulos das colunas no PDF
    columns = df_vacation.columns
    for i, column in enumerate(columns):
        doc.drawString(x_offset + i * 100, y_offset, str(column))

    # Adiciona as linhas de dados da tabela no PDF
    for index, line in df_vacation.iterrows():
        y_offset -= line_height
        for i, value in enumerate(line):
            doc.drawString(x_offset + i * 100, y_offset, str(value))

    # Salva o PDF
    doc.save()
    return True
