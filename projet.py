import time
import datetime

# Spécification des tâches
class Task:
    def __init__(self, name, period, execution_time, work, resource):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.work = work
        self.resource = resource
        self.last_start_time = None

# Initialisation des tâches
pompe1 = Task("Pompe 1", 5, 2, 10, "Reservoir 1")
pompe2 = Task("Pompe 2", 15, 3, 20, "Reservoir 1")
machine1 = Task("Machine 1", 5, 5, 1, "Roues")
machine2 = Task("Machine 2", 5, 3, 1, "Moteurs")

# Réservoir
reservoir = 50
roues = 0
moteurs = 0

# Ordonnanceur
def schedule(tasks, reservoir, roues, moteurs):
    start_time = datetime.datetime.now()

    while True:
        for task in tasks:
            # Vérifier si la tâche peut être exécutée
            if (datetime.datetime.now() - task.last_start_time).seconds >= task.period:
                # Vérifier les ressources
                if task.name == "Pompe 1" or task.name == "Pompe 2":
                    if reservoir + task.work <= 50:
                        reservoir += task.work
                    else:
                        continue
                elif task.name == "Machine 1":
                    if reservoir >= 25:
                        reservoir -= 25
                        roues += 1
                    else:
                        continue
                elif task.name == "Machine 2":
                    if reservoir >= 5:
                        reservoir -= 5
                        moteurs += 1
                    else:
                        continue
                
                # Enregistrer le temps de début de la tâche
                task.last_start_time = datetime.datetime.now()
                # Exécuter la tâche
                time.sleep(task.execution_time)

        # Priorité
        if roues / 4 > moteurs:
            tasks[2], tasks[3] = tasks[3], tasks[2]
        elif roues / 4 < moteurs:
            tasks[2], tasks[3] = tasks[3], tasks[2]

        # Vérifier si 2 minutes sont écoulées
        if (datetime.datetime.now() - start_time).seconds >= 120:
            break
    
    return moteurs

# Exécuter l'ordonnanceur
moteurs = schedule([pompe1, pompe2, machine1, machine2], reservoir, roues, moteurs)
print("Nombre de moteurs produits : ", moteurs)
