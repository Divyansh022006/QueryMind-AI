from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


def generate_pdf(question, sql, dataframe, insights):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>QueryMind AI Report</b>", styles["Title"])
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(f"<b>Question:</b> {question}", styles["BodyText"])
    )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(f"<b>Generated SQL:</b><br/>{sql}", styles["BodyText"])
    )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph("<b>Top Results</b>", styles["Heading2"])
    )

    preview = dataframe.head(10)

    for row in preview.to_string(index=False).split("\n"):
        elements.append(
            Paragraph(row.replace(" ", "&nbsp;"), styles["Code"])
        )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph("<b>AI Insights</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(insights.replace("\n", "<br/>"), styles["BodyText"])
    )

    doc.build(elements)

    buffer.seek(0)

    return buffer