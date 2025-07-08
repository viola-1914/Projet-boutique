
class produit:
    def __init__(self, nom, prix, stock_disponible, stock_limite, en_boutique=False):
        self.nom = nom
        self.prix = prix
        self.stock_disponible = stock_disponible
        self.stock_limite = stock_limite
        self.en_boutique = en_boutique
        
        
    def approvisionner(self, quantité):
        self.stock_disponible += quantité
        
    def est_critique(self):
          return self.stock_disponible <= self.stock_limite
      
    def ajouter_enboutique(self):
          self.en_boutique = True   
      
    def __str__(self):
      return f"{self.nom} - {self.prix} FCA - stock:{self.stock_disponible} - limite: {self.stock_limite} - en boutique: {self.en_boutique}"
 # ça appelle automatiquement __str__()

