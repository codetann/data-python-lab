import matplotlib.pyplot as plt
import numpy as np

class Store:
    def __init__(self):
        self.individual_sales = []
        self.flavor_totals = {
            'Chocolate': 0,
            'Vanilla': 0,
            'Strawberry': 0,
        }
        self.day_total = 0

    # Methods
    def create_invoice(self, data):
        invoice = {
            'name': '{} {}'.format(data[0], data[1]),
            'type': data[2],
            'total': round(float(data[3]) * float(data[4]), 2)
        }

        # - set single sale data
        self.individual_sales.append(invoice)
        # - add total of flavor sold
        self.flavor_totals[invoice['type']] += invoice['total']
        # - add single total to day total
        self.day_total = round(self.day_total + invoice['total'], 2)

    def bar_graph(self):
        # - creates a bar graph based on the sales data
        x = ['Chocolate', 'Vanilla', 'Strawberry']
        y = [self.flavor_totals['Chocolate'], self.flavor_totals['Vanilla'], self.flavor_totals['Strawberry']] 

        plt.bar(x, y)
        plt.show()

cupcake_store = Store()
