import json

def generate_report(*data, **options):
    format_style = options.get("format", "text")
    header = options.get("header", True)
    footer = options.get("footer", True)

    lines = []

    if header:
        lines.append("=== REPORT ===")

    for item in data:
        if format_style == "text":
            lines.append(str(item))
        elif format_style == "json":
            lines.append(json.dumps(item))
        else:
            lines.append(str(item))

    if footer:
        lines.append("=== END ===")

    return '\n'.join(lines)