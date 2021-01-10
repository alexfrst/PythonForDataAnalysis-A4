from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import math, pandas, sklearn, numpy
import pickle

class Record(models.Model):
    profit_on_operating_activities = models.FloatField(validators=[MinValueValidator(0)],default=1)
    financial_expenses = models.FloatField(validators=[MinValueValidator(1)],default=1)
    sales_of_the_year = models.FloatField(validators=[MinValueValidator(1)],default=1)
    sales_of_the_previous_year = models.FloatField(validators=[MinValueValidator(1)],default=1)
    operating_expenses = models.FloatField(validators=[MinValueValidator(0)],default=1)
    total_liabilities = models.FloatField(validators=[MinValueValidator(1)],default=1)
    current_assets = models.FloatField(validators=[MinValueValidator(0)],default=1)
    inventory = models.FloatField(validators=[MinValueValidator(0)],default=1)
    short_term_liabilities = models.FloatField(validators=[MinValueValidator(0)],default=1)
    total_assets = models.FloatField(validators=[MinValueValidator(1)],default=1)
    profit_on_sales = models.FloatField(validators=[MinValueValidator(0)],default=1)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    Prediction = models.CharField(max_length=20,blank=True)

    def GetVariables(self):
        return {
            26: self.profit_on_operating_activities / self.financial_expenses,
            20: self.sales_of_the_year / self.sales_of_the_previous_year,
            33: self.operating_expenses / self.total_liabilities,
            46: (self.current_assets - self.inventory) / self.short_term_liabilities,
            21: self.profit_on_operating_activities / self.total_assets,
            28: math.log(self.total_assets),
            8: self.sales_of_the_year / self.total_assets,
            38: self.profit_on_sales / self.sales_of_the_year,
            34: self.profit_on_sales / self.total_assets,
        }

    def Predict(self):
        values = self.GetVariables()
        medianvalues = pickle.load(open("saves/medianyear{}.save".format(self.year), "rb"))
        variables = numpy.array([medianvalues[i] if i not in values.keys() else medianvalues[i] for i in range(64)]).reshape(1, -1)
        model = pickle.load(open("saves/modelyear{}.save".format(self.year), "rb"))
        pred = model.predict(variables)
        print("Probability of no bankruptcy / bankruptcy",model.predict_proba(variables))
        self.Prediction = "No bankruptcy" if pred[0] == 0 else "bankruptcy"
        self.save()

    def GetValues(self):
        return [
            self.profit_on_operating_activities,
        self.financial_expenses,
        self.sales_of_the_year,
        self.sales_of_the_previous_year,
        self.operating_expenses,
        self.total_liabilities,
        self.current_assets,
        self.inventory,
        self.short_term_liabilities,
        self.total_assets,
        self.profit_on_sales,
        self.year,
        self.Prediction]

    def GetHeader(self):
        return[
            'profit_on_operating_activities',
            "financial_expenses",
            "sales_of_the_year",
            "sales_of_the_previous_year",
            "operating_expenses",
            "total_liabilities",
            "current_assets",
            "inventory",
            "short_term_liabilities",
            "total_assets",
            "profit_on_sales",
            "year",
            "Prediction"
        ]

class Data(models.Model):
    X1 = models.FloatField(default=0)
    X2 = models.FloatField(default=0)
    X3 = models.FloatField(default=0)
    X4 = models.FloatField(default=0)
    X5 = models.FloatField(default=0)
    X6 = models.FloatField(default=0)
    X7 = models.FloatField(default=0)
    X8 = models.FloatField(default=0)
    X9 = models.FloatField(default=0)
    X10 = models.FloatField(default=0)
    X11 = models.FloatField(default=0)
    X12 = models.FloatField(default=0)
    Class = models.CharField(max_length=15)
    Year = models.IntegerField()






