class Compte:
    _prim = "210-"  # attribut statique
    
    def __init__(self, num_compte, solde):
        self.solde = solde
        self.num_compte = num_compte
    
    # Méthode d'accès pour le nombre de compte
    def get_numero(self):
        return self._prim + self.num_compte
    
    # Méthode mutateur pour modifier le nombre de compte
    def set_numero(self, new_num):
        if len(new_num) == 11 and new_num[3] == '-':
            self.num_compte = new_num
    
    def retire(self, montant):
        return self.solde - montant
    
    def verser(self, montant):
        """
        Retourne le nouveau solde après une opération de virement.
        Si l'argent n'est pas disponible, renvoie un message d'erreur.
        """
        if montant <= self.solde:
            self.solde -= montant
            return self.solde
        else:
            print("Erreur: Solde insuffisant.")
    
    def depot(self, montant):
        """ 
        Retourne le nouveau solde après une opération de dépose.
        Si la somme est inférieure ou égale à zéro, renvoie un message d'erreur. 
        """
        if montant > 0:
            self.solde += montant
            return self.solde
        else:
            print("Erreur: Montant incorrect.")
    
    def __str__(self):
        return "Compte {}:\nSolde={}".format(self.get_numero(), self.solde)

Compte1 = Compte("105-000000000", 500)
print(Compte1)
Compte1.set_numero("105-987654321")
print(Compte1)
Compte1.verser(200)
print(Compte1)
Compte1.verser(300)
print(Compte1)
