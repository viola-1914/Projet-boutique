
class Utilisateur:
     def __init__(self, nom, identifiant, mot_de_passe, role):
         self.nom = nom
         self.identifiant = identifiant
         self.mot_de_passe = mot_de_passe
         self.role = role
         
     def verifier_mot_de_passe(self, essai):
         return self.mot_de_passe == essai
         
     def  __str__(self):
         return f"nom: {self.nom} - role: {self.role}"

