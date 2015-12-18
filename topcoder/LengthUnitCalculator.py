class LengthUnitCalculator:

    def calc(self, amount, fromUnit, toUnit):
        if fromUnit == toUnit:
            return amount
        to_in = {'in': 1, 'ft': 12, 'yd': 3 * 12, 'mi': 1760 * 3 * 12}
        return (float(amount) * to_in[fromUnit]) / to_in[toUnit]
