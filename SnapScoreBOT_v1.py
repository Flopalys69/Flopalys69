import time
import pyautogui
import keyboard

pyautogui.FAILSAFE = True

print("Snapchat Farming - Mode Coordonnées")
print("Assure-toi que Snapchat est ouvert et visible")
print("Appuie sur ESC pour arrêter\n")


def main():
    count = int(input("Nombre de snaps à envoyer : ") or 50)

    time.sleep(8)  # Temps pour que tu puisses mettre Snapchat en avant

    # ================== TES COORDONNÉES ==================
    STARTING_BUTTON = (1100, 460)    # Bouton du milieu pour commencer
    CAMERA_BUTTON   = (1100, 807)    # Bouton appareil photo
    SEND_TO_BUTTON  = (1164, 944)    # Bouton "Envoyer à"
    FIRST_RESULT    = (1031, 236)    # Premier résultat (important !)
    SEND_FINAL      = (1195, 950)    # Bouton Envoyer final
    # ====================================================

    print(f"Démarrage - Envoi automatique de {count} snaps...")

    for i in range(count):
        if keyboard.is_pressed('esc'):
            print("Arrêt manuel...")
            break

        print(f"Snap #{i+1}")

        # === Cycle complet ===
        if i == 0:  # Initialisation seulement au premier snap
            pyautogui.click(STARTING_BUTTON)
            time.sleep(3)

        pyautogui.click(CAMERA_BUTTON)
        time.sleep(0.4)

        pyautogui.click(SEND_TO_BUTTON)
        time.sleep(0.1)

        # Clique directement sur le premier résultat
        pyautogui.click(FIRST_RESULT)
        time.sleep(0.1)

        pyautogui.click(SEND_FINAL)
        time.sleep(0.2)   # Pause entre les snaps

    print("Programme terminé !")


if __name__ == "__main__":
    main()
