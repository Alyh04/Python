from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class Fenetre_Details:
    def __init__(self, root):
        # Votre code existant ici...

    def generer_facture(self):
        nom = "Nom Client"  # Récupérer le nom du client
        prenom = "Prenom Client"  # Récupérer le prénom du client
        adresse = "Adresse Client"  # Récupérer l'adresse du client
        numero = "Numéro Client"  # Récupérer le numéro du client
        email = "Email Client"  # Récupérer l'adresse e-mail du client
        prix_diner = "Prix du dîner"  # Récupérer le prix du dîner
        prix_total = "Prix total"  # Récupérer le prix total

        # Créer le document PDF
        doc = SimpleDocTemplate("facture.pdf", pagesize=letter)
        styles = getSampleStyleSheet()

        # Contenu de la facture
        content = []

        # Ajouter les informations du client
        content.append(Paragraph("<b>Facture</b>", styles['Title']))
        content.append(Paragraph(f"<b>Nom:</b> {nom}", styles['Normal']))
        content.append(Paragraph(f"<b>Prénom:</b> {prenom}", styles['Normal']))
        content.append(Paragraph(f"<b>Adresse:</b> {adresse}", styles['Normal']))
        content.append(Paragraph(f"<b>Numéro:</b> {numero}", styles['Normal']))
        content.append(Paragraph(f"<b>Email:</b> {email}", styles['Normal']))

        # Ajouter les détails du dîner et du prix total
        content.append(Paragraph(f"<b>Prix du dîner:</b> {prix_diner}", styles['Normal']))
        content.append(Paragraph(f"<b>Prix total:</b> {prix_total}", styles['Normal']))

        # Générer le PDF
        doc.build(content)
