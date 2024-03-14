def add_h_tag(text):
    """
    Adds a h tag to the text
    """
    return f"<h2>{text}</h2>"

def make_table(my_list):
    """
    Transforms a dict in a HTML Table
    """
    headers = list(my_list[0].keys())
    text = '<table style="width:100%"><tr>'
    for header in headers:
        text += f'<th>{header}</th>'
    text += '</tr>'
    for obj in my_list:
        text += '<tr>'
        for index in obj:
            text += f'<th>{obj[index]}</th>'
        text += '</tr>'
    text += '</table>'
    return text
