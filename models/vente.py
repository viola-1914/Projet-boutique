

class Vente:
    def __init__(self, vendeur):
        self.articles = [] #liste de tuple (produit, quantité)
        self.total = 0
        self.vendeur = vendeur


    def ajouter_article(self, produit, quantite):
      print(f"DEBUG: en_boutique={produit.en_boutique}, stock_disponible={produit.stock_disponible}, quantite demandée={quantite}")

      if not produit.en_boutique:
            print(f"{produit.nom} n'est pas dans la boutique")
            return False

      if produit.stock_disponible < quantite:
            print(f"Stock insuffisant pour {produit.nom}")
            return False

        # Tout est bon
      produit.stock_disponible -= quantite
      self.articles.append((produit, quantite))
      self.total += produit.prix * quantite
      return True
    def facture(self):
     texte = "------- FACTURE -------\n"
     for prod, qte in self.articles:
        texte += f"{prod.nom} x {qte} = {prod.prix * qte} FCFA\n"
     texte += f"TOTAL À PAYER : {self.total} FCFA\n"
     return texte
 
            
            
class Statistique:
      def __init__(self) :
          self.liste_ventes = []
          
      def enregistre_vente(self, vente) :
           self.liste_ventes.append(vente)
           
      def total_ventes(self):
        return  len(self.liste_ventes)
    
      def revenu_total(self):
          return sum(vente.total for vente in self.liste_ventes)
      
      def total_produit_vendus(self):
          return sum(qte for vente in self.liste_ventes for (_, qte) in vente.articles)
      
      
      def utilisateurs_uniques(self):
          return set(vente.vendeur.identifiant for vente in self.liste_ventes)