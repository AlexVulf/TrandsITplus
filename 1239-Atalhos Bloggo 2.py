def convert_bloggo_to_html(text):
    italic = bold = False
    result = []
    
    for char in text:
        if char == '_':
            result.append("<i>" if not italic else "</i>")
            italic = not italic
        elif char == '*':
            result.append("<b>" if not bold else "</b>")
            bold = not bold
        else:
            result.append(char)
    
    return "".join(result)

try:
    while True:
        line = input().strip()
        print(convert_bloggo_to_html(line))
except EOFError:
    pass