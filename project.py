from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
import random
import sys

def spin_wheel_button_click(label: QLabel, color_box: QWidget):
    # Генерируем случайный цвет из ВСЕГО RGB-пространства (0x000000 → 0xFFFFFF)
    color = f"#{random.randint(0, 0xFFFFFF):06x}"
    label.setText(f"Выпавший вариант: {color.upper()}")
    color_box.setStyleSheet(f"background-color: {color}; border-radius: 40px;")

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Колесо ВСЕХ цветов 💥")
    window.resize(400, 250)

    button = QPushButton("Крутить!", window)
    button.setGeometry(150, 40, 100, 40)
    button.clicked.connect(lambda: spin_wheel_button_click(label, color_box))

    label = QLabel("Результат прокрутки колеса", window)
    label.setGeometry(50, 110, 300, 30)
    label.setStyleSheet("font-size: 14px; color: #00ff00;")

    color_box = QWidget(window)
    color_box.setGeometry(160, 150, 80, 80)
    color_box.setStyleSheet("background-color: #000; border-radius: 40px;")

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()