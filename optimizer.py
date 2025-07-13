from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

def optimize_risol():
    model = LpProblem("Optimasi_Produksi_Risol", LpMaximize)

    x = LpVariable("Risol_Mayo", lowBound=0, cat='Integer')
    y = LpVariable("Risol_Sayur", lowBound=0, cat='Integer')

    model += 4000 * x + 2500 * y

    model += x + y <= 100
    model += 80 * x + 50 * y <= 6000
    model += 6 * x + 4 * y <= 480

    model.solve()

    return {
        "status": LpStatus[model.status],
        "risol_mayo": int(x.varValue),
        "risol_sayur": int(y.varValue),
        "total_keuntungan": int(value(model.objective))
    }
