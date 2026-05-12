from beanie import Document

class Voiture(Document):
    marque: str          # Brand: "Toyota", "Renault"
    modele: str          # Model: "Corolla", "Clio"
    annee: int           # Year: 2022
    prix: float          # Price: 75000.5
    kilometrage: int     # Mileage: 15000
    type_carburant: str  # Fuel: "Essence", "Diesel", "Electrique"
    couleur: str         # Color: "Rouge"
    nombre_portes: int   # Doors: 4
    transmission: str    # "Manuelle" or "Automatique"
    options: list[str] = []     # ["GPS", "climatisation"]
    image_url: str = ""         # photo URL
    statut: str = "disponible"  # disponible / vendu / réservé

    class Settings:
        name = "voitures"  # MongoDB collection name