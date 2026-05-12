from models.voiture import Voiture
from services.voiture_service import get_voitures as service_get_voitures


def register_tools(mcp):

    # =========================================================
    # TOOL : GET ALL CARS
    # =========================================================
    @mcp.tool()
    async def get_voitures():
        """Returns all cars in the database"""
        result = await service_get_voitures()
        return [v.model_dump() for v in result]

    # =========================================================
    # TOOL : BEST CAR BY BUDGET
    # =========================================================
    @mcp.tool()
    async def get_voiture_by_budget(budget: float):
        """
        Returns the best car recommendation within a given budget.

        How the scoring works:
        - Prefers newer cars (higher year = higher score)
        - Prefers cars closer to the budget (less leftover money = better use of budget)
        - Combines both into a single score and picks the winner
        """
        # 1. Get all cars from DB
        voitures = await Voiture.find_all().to_list()

        # 2. Keep only cars within budget
        candidates = [v for v in voitures if v.prix <= budget]

        if not candidates:
            return {
                "message": "Aucune voiture disponible dans ce budget",
                "budget": budget
            }

        # 3. Scoring function
        def score(voiture):
            score_year = voiture.annee * 10       # newer = better
            score_price = (budget - voiture.prix) # closer to budget = better
            return score_year - score_price

        # 4. Pick the best
        best = max(candidates, key=score)

        # 5. Return structured result
        return {
            "budget": budget,
            "voiture": {
                "id": str(best.id),
                "marque": best.marque,
                "modele": best.modele,
                "annee": best.annee,
                "prix": best.prix,
                "kilometrage": best.kilometrage,
                "type_carburant": best.type_carburant,
            }
        }