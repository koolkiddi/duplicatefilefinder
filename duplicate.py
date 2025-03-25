import os
import hashlib
import concurrent.futures

def calculate_md5(file_path):
    """Calcule le hash MD5 d'un fichier."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def process_file(file_path, hash_map):
    """Calcule le hash d'un fichier et vérifie les doublons."""
    try:
        print(f"Vérification du fichier : {file_path}")  # Journal en temps réel
        file_hash = calculate_md5(file_path)
        if file_hash in hash_map:
            return (file_path, hash_map[file_hash])
        else:
            hash_map[file_hash] = file_path
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path} : {e}")
    return None

def find_duplicates(paths):
    """Trouve les fichiers en double dans les chemins donnés."""
    hash_map = {}
    duplicates = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for path in paths:
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    futures.append(executor.submit(process_file, file_path, hash_map))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                duplicates.append(result)

    return duplicates

def main():
    # Chemins à analyser (modifiables ici)
    paths_to_check = [
        "/home/sexe/with_gay/",
        "/home/sexe/with_trans/"
    ]

    # Recherche des doublons
    print("\nAnalyse en cours...")
    duplicates = find_duplicates(paths_to_check)

    if duplicates:
        print("\nDoublons trouvés :")
        for duplicate, original in duplicates:
            print(f"Doublon : {duplicate}\nOriginal : {original}\n")

        # Demande confirmation avant suppression
        confirm = input("Voulez-vous supprimer tous les fichiers en double et garder les originaux ? (o/n) : ").strip().lower()

        if confirm == 'o':
            for duplicate, _ in duplicates:
                try:
                    os.remove(duplicate)
                    print(f"Supprimé : {duplicate}")
                except Exception as e:
                    print(f"Erreur lors de la suppression de {duplicate} : {e}")
            print("\nTous les doublons ont été supprimés.")
        else:
            print("\nAucune suppression n'a été effectuée.")
    else:
        print("\nAucun doublon trouvé.")

if __name__ == "__main__":
    main()
