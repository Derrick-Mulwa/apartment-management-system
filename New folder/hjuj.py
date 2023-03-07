import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import mysql.connector


class DatabaseViewer(QTableWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Database Viewer')
        self.resize(500, 300)
        self.show()

        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='apartment_name'
        )
        cursor = conn.cursor()

        # Execute a SQL query to retrieve data from the database
        cursor.execute('SELECT * FROM messages')

        # Create table headers
        headers = [description[0] for description in cursor.description]
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        # Populate table with data
        row = 0
        for row_data in cursor.fetchall():
            self.insertRow(row)
            for column, item in enumerate(row_data):
                self.setItem(row, column, QTableWidgetItem(str(item)))
            row += 1

        # Close database connection
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    database_viewer = DatabaseViewer()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import mysql.connector


class DatabaseViewer(QTableWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Database Viewer')
        self.resize(500, 300)
        self.show()

        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='example_db'
        )
        cursor = conn.cursor()

        # Execute a SQL query to retrieve data from the database
        cursor.execute('SELECT * FROM my_table')

        # Create table headers
        headers = [description[0] for description in cursor.description]
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        # Populate table with data
        row = 0
        for row_data in cursor.fetchall():
            self.insertRow(row)
            for column, item in enumerate(row_data):
                self.setItem(row, column, QTableWidgetItem(str(item)))
            row += 1

        # Close database connection
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    database_viewer = DatabaseViewer()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import mysql.connector


class DatabaseViewer(QTableWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Database Viewer')
        self.resize(500, 300)
        self.show()

        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='example_db'
        )
        cursor = conn.cursor()

        # Execute a SQL query to retrieve data from the database
        cursor.execute('SELECT * FROM my_table')

        # Create table headers
        headers = [description[0] for description in cursor.description]
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        # Populate table with data
        row = 0
        for row_data in cursor.fetchall():
            self.insertRow(row)
            for column, item in enumerate(row_data):
                self.setItem(row, column, QTableWidgetItem(str(item)))
            row += 1

        # Close database connection
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    database_viewer = DatabaseViewer()
    sys.exit(app.exec_())
